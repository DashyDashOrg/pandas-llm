from setuptools import setup, find_packages

# Reads the content of your README.md into a variable to be used in the setup below
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='pandas_llm',                           # should match the package folder
    # packages=['pandas_llm'],                     # should match the package folder
    version='0.0.1',                                # important for updates
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
        'Development Status :: 1 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Artificial Intelligence',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
        'aiohttp',
        'aiosignal',
        'async-timeout',
        'attrs',
        'certifi',
        'charset-normalizer',
        'frozenlist',
        'idna',
        'multidict',
        # 'numpy==1.24.3',
        'numpy',
        'openai>=0.27.6',
        # 'pandas==2.0.1',
        'pandas',
        'python-dateutil',
        'pytz',
        'requests',
        'RestrictedPython==6.0',
        'six',
        'tqdm',
        'tzdata',
        'urllib3',
        'yarl'
    ],   
    download_url="https://github.com/DashyDashOrg/pandas-llm/",
)