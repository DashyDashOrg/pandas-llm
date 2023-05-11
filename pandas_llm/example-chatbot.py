import os
import pandas as pd

import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent))

from pandas_llm import PandasLLM

# Data
data = [('John Doe', 25, 50), 
        ('Jane Smith', 38, 70),
        ('Alex Johnson', 45, 80),
        ('Jessica Brown', 60, 40),
        ('Michael Davis', 22, 90),
        ('Emily Wilson', 30, 60),
        ('Daniel Taylor', 35, 75),
        ('Sophia Moore', 40, 85),
        ('David Thomas', 50, 65),
        ('Olivia Jackson', 29, 55),
        ('Carlos García', 22, 50),
        ('Ana Rodriguez', 38, 70),
        ('Luis Hernandez', 45, 80),
        ('Sofia Martinez', 60, 40),
        ('Miguel Lopez', 22, 90),
        ('Isabella Gonzalez', 30, 60),
        ('Diego Perez', 35, 75),
        ('Maria Sanchez', 40, 85),
        ('Juan Pena', 50, 65),
        ('Gabriela Ramirez', 29, 55),
        ('Giovanni Rossi', 22, 50),
        ('Maria Bianchi', 38, 70),
        ('Luca Ferrari', 45, 80),
        ('Sofia Russo', 60, 40),
        ('Francesco Romano', 22, 90),
        ('Isabella Colombo', 30, 60),
        ('Alessandro Ricci', 35, 75),
        ('Giulia Marino', 40, 85),
        ('Antonio Greco', 50, 65),
        ('Gabriella Bruno', 29, 55)]

# Create DataFrame
df = pd.DataFrame(data, columns=['name', 'age', 'donation'])

# Print DataFrame
print(df)


def main():

    # Set the OpenAI API key
    openai_key = os.environ.get("OPENAI_API_KEY")
    if openai_key is None:
        print("No OpenAI API key provided. Exiting.")
        return

    config = {
        "openai_api_key":openai_key
    }

    conv_df = PandasLLM(data=df, config=config)
    print()
    banner = """
    Welcome to the Donation Data CLI.
    The donation dataset has three columns (name, age, donation)
    Please note that these names, ages, and donations are randomly generated and do not correspond to real individuals or their donations.
    
    You can ask questions like:
    - show me the name of donators
    - What is the average age of people who donated?
    - What is the average donation amount?
    - What is the average donation of people older than 30?
    - What is the average donation of people older than 30 who donated more than $50?
    """
    print(banner)

    while True:
        prompt = input("Enter your query (or 'exit' to quit): ")
        if prompt.lower() == "exit":
            break

        result = conv_df.prompt(prompt)
        print(f"Result ({type(result)}):\n {result}")

if __name__ == "__main__":
    main()
