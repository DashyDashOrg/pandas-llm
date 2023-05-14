import os
import pandas as pd

import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent))
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
