import setuptools

# Reads the content of your README.md into a variable to be used in the setup below
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='pandas_llm',                           # should match the package folder
    packages=['pandas_llm'],                     # should match the package folder
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
    install_requires=['requests'],                  # list all packages that your package uses
    keywords=["pypi", "pandas-llm", "pandas", "llm", "ai", "openai", "chatgpt"], #descriptive meta-data
    classifiers=[                                   # https://pypi.org/classifiers
        'Development Status :: 1 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Artificial Intelligence',
        'License :: MIT License',
        'Programming Language :: Python :: 3.9',
    ],
    
    download_url="https://github.com/DashyDashOrg/pandas-llm/",
)