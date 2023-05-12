from setuptools import setup, find_packages

# Reads the content of your README.md into a variable to be used in the setup below
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='pandas_llm',                           # should match the package folder
    version='0.0.2',                                # important for updates
    license='MIT',                                  # should match your chosen license
    description='Conversational Pandas Dataframes',
    long_description=long_description,              # loads your README.md
    long_description_content_type="text/markdown",  # README.md is of type 'markdown'
    author='DashyDash',
    author_email='alessio@dashydash.com',
    url='https://github.com/DashyDashOrg/pandas-llm', 
    project_urls = {                                # Optional
        "Bug Tracker": "https://github.com/DashyDashOrg/pandas-llm/issues"
    },
    keywords=["pypi", "pandas-llm", "pandas", "llm", "ai", "openai", "chatgpt"], #descriptive meta-data
    packages=find_packages(),
    classifiers=[                                   # https://pypi.org/classifiers
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
        "aiohttp>=3.8.4",
        "aiosignal>=1.3.1",
        "async-timeout>=4.0.2",
        "attrs>=23.1.0",
        "certifi>=2023.5.7",
        "charset-normalizer>=3.1.0",
        "frozenlist>=1.3.3",
        "idna>=3.4",
        "multidict>=6.0.4",
        "numpy>=1.24.3",
        "openai>=0.27.6",
        "pandas>=2.0.1",
        "python-dateutil>=2.8.2",
        "pytz>=2023.3",
        "requests>=2.30.0",
        "RestrictedPython>=6.0",
        "six>=1.16.0",
        "tqdm>=4.65.0",
        "tzdata>=2023.3",
        "urllib3>=2.0.2",
        "yarl>=1.9.2",
    ],   
    download_url="https://github.com/DashyDashOrg/pandas-llm/releases/tag/v0.0.2",
)