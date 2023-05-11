import pandas as pd
import datetime
import numpy as np
import time
import openai
import os
from sandbox import Sandbox
import re
import json

class PandasLLM(pd.DataFrame):

    code_blocks = [r'```python(.*?)```',r'```(.*?)```']
    model = "gpt-3.5-turbo"
    temperature = 0.2
    privacy = True
    presentation = False
    prompt_bulletpoint = ""
    save_path = ""
    verbose = False

    def __init__(self, data=None, config=None, *args, **kwargs):
        super().__init__(data, *args, **kwargs)
        
        self.config = config or {}

        # Set up OpenAI API key from the environment or the config
        self.openai_api_key = os.environ.get("OPENAI_KEY") or self.config.get("openai_api_key", "your_openai_api_key")

        self.model = self.config.get("model", self.model)
        self.temperature = self.config.get("temperature", self.temperature)
        self.privacy = self.config.get("privacy", self.privacy)
        self.presentation = self.config.get("presentation", self.presentation)
        self.prompt_bulletpoint = self.config.get("prompt_bulletpoint", self.prompt_bulletpoint)
        self.save_path = self.config.get("save_path", self.save_path)
        self.verbose = self.config.get("verbose", self.verbose)

    def buildPromptForRole(self):
        prompt_role = f"""
I want you to act as a data scientist and Python coder. I want you code for me. 
I have a dataset of {len(self)} rows and {len(self.columns)} columns.
Columns and their type are the following:
        """

        for col in self.columns:
            col_type = self.dtypes[col]
            prompt_role += f"{col} ({col_type})\n"

        return prompt_role

    def buildPromptForProblemSolving(self, request):

        prompt_problem = f"""

Given a DataFrame named 'df', write a Python code snippet that addresses the following request:
{request}

While crafting the code, please follow these guidelines:
1. When comparing or searching for strings, use lower case letters, ignore case sensitivity, and apply a "contains" search.
2. Ensure that the answer is a single line of code without explanations, comments, or additional details. 
3. If a single line solution is not possible, multiline solutions or functions are acceptable, but the code must end with an assignment to the variable 'result'.
4. Assign the resulting code to the variable 'result'.
5. Avoid importing any additional libraries than pandas and numpy.
"""

        return prompt_problem

    def extractPythonCode(self, text: str, regexp: str) -> str:
        # Define the regular expression pattern for the Python code block
        pattern = regexp
        
        # Search for the pattern in the input text
        match = re.search(pattern, text, re.DOTALL)
        
        # If a match is found, return the extracted code (without the markers)
        if match:
            return match.group(1).strip()
        
        # If no match is found, return an empty string
        return ""

    def print(self,  *args, **kwargs):
        if self.verbose:
            print(*args, **kwargs)

    def variable_to_string(self, variable):
        if variable is None: return None
        try:

            if isinstance(variable, pd.Series):
                # convert to dataframe
                variable = variable.to_frame()

            if isinstance(variable, pd.DataFrame):
                variable = variable.drop_duplicates()
                if len(variable) == 0: return None
                return str(variable)

            elif isinstance(variable, np.ndarray):
                if len(variable) == 0: return None
                return  np.array2string(variable)
            else:
                # Convert the variable to a string
                return str(variable)
        except Exception as e:
            return str(variable)
        

    def save(self,name,value):
        if len(self.save_path) == 0:
            return  
        try:
            with open(f"{self.save_path}/{name}", 'w') as file:
                file.write(value)
        except Exception as e:
            self.print(f"error {e}")
        return

    def execInSandbox(self, df, generated_code:str):

        # Create a Sandbox instance and allow pandas to be imported
        sandbox = Sandbox()
        sandbox.allow_import("pandas")
        sandbox.allow_import("numpy")

        # Define the initial code to set up the DataFrame
        initial_code = f"""
import pandas as pd
import datetime
from pandas import Timestamp
import numpy as np

        """

        # Combine the initial code and the generated code
        full_code = initial_code + "\n" + generated_code

        self.save("temp/prompt_code.py",full_code)
        # Execute the combined code in the Sandbox
        sandbox_result = sandbox.execute(full_code, {"df":df})

        # Get the result from the local_vars dictionary
        result = sandbox_result.get("result")
        return result



    def prompt(self, request: str):
        # Set up OpenAI API key
        openai.api_key = self.openai_api_key

        messages=[
                {"role": "system", 
                "content": self.buildPromptForRole()},
                {"role": "user", 
                "content": self.buildPromptForProblemSolving(request)
                }
            ]

        response = None
        for times in range(0,3):
            try:
                response = openai.ChatCompletion.create(
                model=self.model,
                temperature=self.temperature,
                messages = messages
                )
                break;
            except Exception as e:
                self.print(f"error {e}")
                continue

        if response is None:
            return "Please try later"

        self.save("temp/prompt_cmd.json",json.dumps(messages, indent=4))

        generated_code = response.choices[0].message.content
        if generated_code == "" or generated_code is None:
            return None
        
        results=[]
        for regexp in self.code_blocks:
            cleaned_code = self.extractPythonCode(generated_code,regexp)
            if cleaned_code == "" or cleaned_code is None:
                continue
            results.append(cleaned_code)
        results.append(generated_code)

        if len(results) == 0:
            return None

        for cleaned_code in results:

            result = None
            try:
                result = self.execInSandbox(self, cleaned_code)
            except Exception as e:
                self.print(f"error {e}")
                try:
                    expression = re.sub(r"^\s*result\s*=", "", cleaned_code).strip()
                    result = eval(expression, {'df': self, 'pd': pd, 'np': np, 'datetime': datetime, 'result': result})
                except Exception as e:
                    self.print(f"error {e}")
                    pass

            if result is not None and str(result) != "":
                break

        if self.privacy == True:
            # non formatted result
            return result

        return None