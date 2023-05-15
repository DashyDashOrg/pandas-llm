# pandas-LLM

## Introduction
pandas-llm is a lightweight Python library that extends pandas to allow querying datasets using OpenAI prompts. This powerful tool leverages the natural language processing capabilities of OpenAI to offer intuitive, language-based querying of your Pandas dataframes.

## Key Features
- **Natural Language Querying**: With pandas-llm, you can execute complex Pandas queries using natural language prompts. Instead of writing code, you can express your query in plain language and obtain the desired results.

- **Seamless Integration**: The library seamlessly integrates with your existing Pandas workflow. You can continue using normal Pandas functions and syntax while leveraging the added capability of natural language queries.

- **Efficiency and Performance**: pandas-LLM is designed to deliver efficient and performant querying capabilities. It uses OpenAI's language model to process queries quickly and accurately, providing rapid insights from your data.

- **Flexible and Expressive**: Whether you need to filter, aggregate, sort, or transform your data, pandas-LLM allows you to express your requirements flexibly and expressively. You can perform complex operations on your dataframes with ease using human-readable language.

- **Intelligent Results**: The library returns the results of your queries in a concise and understandable format. You can extract valuable insights from your data without complex code or manual analysis.

With pandas-llm, you can unlock the power of natural language querying and effortlessly execute complex pandas queries. Let the library handle the intricacies of data manipulation while you focus on gaining insights and making data-driven decisions.

## Installation

Install pandas-llm using pip:

```shell
pip install pandas-llm
```

## Features
- Query pandas dataframes using natural language prompts.
- Leverage the power of OpenAI's language models in your data analysis.
- Seamless integration with existing pandas functions.

## Usage
Here's a quick [example](https://github.com/DashyDashOrg/pandas-llm/blob/main/pandas_llm/example.py) of how to use pandas-llm:

```python
import os
import pandas as pd
from pandas_llm import PandasLLM

# Data
# Please note that these names, ages, and donations are randomly generated 
# and do not correspond to real individuals or their donations.
data = [('John Doe', 25, 50), 
        ('Jane Smith', 38, 70),
        ('Alex Johnson', 45, 80),
        ('Jessica Brown', 60, 40),
        ('Michael Davis', 22, 90),
        ('Emily Wilson', 30, 60),
        ('Daniel Taylor', 35, 75),
        ('Sophia Moore', 40, 85),
        ('David Thomas', 50, 65),
        ('Olivia Jackson', 29, 55)]
df = pd.DataFrame(data, columns=['name', 'age', 'donation'])

conv_df = PandasLLM(data=df, llm_api_key = os.environ.get("OPENAI_API_KEY"))
result = conv_df.prompt("What is the average donation of people older than 40 who donated more than $50?")
code = conv_df.code_block

print(f"Executing the following expression of type {type(result)}:\n{code}\n\nResult is:\n {result}\n")
# Executing the following expression of type <class 'numpy.float64'>:
# result = df.loc[(df['age'] > 40) & (df['donation'] > 50), 'donation'].mean()

# Result is:
#  72.5

```

There is also a chatbot available in the repository using the same dataset. 
Look at [Chatbot example](https://github.com/DashyDashOrg/pandas-llm/blob/main/pandas_llm/example-chatbot.py)

## PandasLLM Class Constructor

The constructor for the PandasLLM class has been enhanced in this release to provide more flexibility and control over the language model interaction. The constructor accepts the following arguments:

**data** (mandatory): The data to be used. It can be a Pandas DataFrame, a list of lists, tuples, dictionaries, a dictionary, a string, or a list.

**llm_engine** (optional): The name of the LLM engine to use. Currently, only OpenAI is supported. Defaults to "openai".

**llm_params** (optional): A dictionary of parameters to be used with the OpenAI API. This allows customization of the LLM behavior. Defaults to model=gpt-3.5-turbo and temperature=0.2.

**prompt_override** (optional): A boolean that determines whether or not the prompt is overridden. If set to True, the custom prompt becomes the main prompt. Defaults to False.

**custom_prompt** (optional): A string that can be provided if prompt_override is False. The custom prompt will be added to the default pandas_llm prompt. Defaults to an empty string.

**path** (optional): The path to the file where the debug data will be saved. If not specified, debug data files will not be generated.

**verbose** (optional): A boolean determines whether debugging information will be printed. If set to True, additional debugging info will be displayed. Defaults to False.

**data_privacy** (optional): A boolean determines whether the data is treated as private. If set to True, the function will not send the data content to OpenAI. Defaults to True.

**llm_api_key** (optional): The OpenAI API key to be used. The library will attempt to use the default API key configured if not provided.

**force_sandbox** (optional): A boolean determining the fallback behaviour if the sandbox environment fails. If set to False and the sandbox fails, the library will retry using eval, which is less safe. Defaults to False.


## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change. Please make sure to update tests as appropriate.

## License
MIT
