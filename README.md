# pandas-llm

pandas-llm is a lightweight Python library that extends pandas to allow querying datasets using OpenAI prompts. This powerful tool leverages the natural language processing capabilities of OpenAI to offer intuitive, language-based querying of your pandas dataframes.

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
Here's a quick example of how to use pandas-llm:

```python
import os
import pandas as pd

# import sys
# from pathlib import Path
# sys.path.append(str(Path(__file__).resolve().parent.parent))
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

conv_df = PandasLLM(data=df, llm_api_key = os.environ.get("OPENAI_API_KEY"), verbose=True)
result = conv_df.prompt("What is the average donation of people older than 30 who donated more than $50?")

print(f"Result ({type(result)}):\n {result}")
# Result (<class 'numpy.float64'>):
#  75.0
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change. Please make sure to update tests as appropriate.

## License
MIT