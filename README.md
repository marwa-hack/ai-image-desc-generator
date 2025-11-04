## Overview

# Here is a sample code for using AI (Ollama) to describe images for further use e.g. selling art platforms.
# Ollama and the used nodel from Ollama library must be installed in advance.
# Images used in this sample code are all AI generated for simulation purposes.
# SEO enorm title, description and tags for each image are generated.
# All information about the images is saved in an Excel file.

## Required libraries - requirements.txt
-> LangChain: 
langchain 

-> Ollama: For running LLMs on local device
langchain_ollama

-> OpenAI: Needs registration and an API Key (Check costs/request!)
langchain-openai

-> Anthropic/Claude: Needs registration and an API Key (Check cost/request!)
langchain-anthropic

-> Pydantic: For using prompt templates
pydantic

-> XLSWriter: For simple writing to Excel file (no append)
xlsxwriter

## Virtual environment setup
-> Create folder for venv virtual environment 
python -m venv venv
-> Activate venv 
Windows:
```
./venv/Scripts/activate
```
-> If activate does not work on Windows, you may need to change the execution policy, e.g. set to unrestricted in the current PowerShell session as follows:
```
Set-ExecutionPolicy Unrestricted -Scope Process
```
-> Install required libraries in current virtual environment
```
pip install -r .\requirements.txt
```

## Get more advanced Infos on my Channel [@marwahack](https://www.youtube.com/@marwahack)