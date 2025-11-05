## Overview
Here is a sample code for using AI (Ollama) to describe images for further use e.g. selling art platforms.
Ollama and the used model from Ollama library must be installed in advance.
Images used in this sample code are all AI generated for simulation purposes.
SEO enorm title, description and tags for each image are generated.
All information about the images is saved in an Excel file.

## Required libraries - requirements.txt
-> LangChain: 
```
langchain
```
-> Ollama: Execute LLMs on local device (Ollama und model used from Ollama Library must be installed)
```
langchain_ollama
```
-> Pydantic: For using prompt templates
```
pydantic
```
-> XLSWriter: For simple writing to Excel file (no append)
```
xlsxwriter
```

## Virtual environment setup
-> Create folder for venv virtual environment 
```
python -m venv venv
```
-> Activate venv 
Windows:
```
./venv/Scripts/activate
```
-> Install required libraries in current virtual environment
```
pip install -r .\requirements.txt
```


