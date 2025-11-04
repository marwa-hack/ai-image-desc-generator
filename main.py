# Import module
import base64

import os
import xlsxwriter
from pydantic import BaseModel, Field
from langchain_core.output_parsers import PydanticOutputParser
from langchain_core.prompts import ChatPromptTemplate
#from langchain_core.messages import SystemMessage, HumanMessage
from langchain_core.output_parsers import StrOutputParser

from langchain_ollama import ChatOllama

class ImageDescResponse(BaseModel):
    title: str = Field(description="image title")
    description: str = Field(description="image description")
    tags: str = Field(description="List the SEO relevant comma separated tags")

# Parse ai output in the defined response 
parser = PydanticOutputParser(pydantic_object=ImageDescResponse)

# Function to encode the image
def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")

# Model must be downloaded from Ollama library  
llm = ChatOllama(
    model="gemma3:4b",
    temperature=0,
)

msg_content = ("You are a POD marketing expert, experienced in social media marketing and SEO. "
    "You will help a print on demand shop to analyze the new design and generate exactly one title, "
    "one engaging description and 15 unique comma separated tags of two or more words, "
    "that are to 90 percent specific tags, to have a high customer reach and sells. "
    "This is for {text}. Wrap the output in this format and provide no other text\n{format_instructions}")

prompt = ChatPromptTemplate.from_messages(
    messages = [
        {
            "role": "system",
            "content": msg_content,
        },
        {
            "role": "user",
            "content": [
                {
                    "type": "image",
                    "source_type": "base64",
                    "data": "{image}",
                    "mime_type": "image/png",
                },
            ],
        }
    ]
).partial(format_instructions=parser.get_format_instructions())

chain = prompt | llm 

# Assign directory to grab images from
directory = r"designs"

# Images file path list  
images_path_list = []

# Traverse whole directory
for root, dirs, files in os.walk(directory):
    # Select file name
    for file in files:
        # Check the extension of files
        if file.endswith('.png'):
            # Test: print whole path of files
            image_path = os.path.join(root, file)
            print(image_path)
            
            # Encode the image
            base64_image = encode_image(image_path)
            
            response = chain.invoke(
                {
                    "text":"POD shop",
                    "image":base64_image,
                }
            )

            # Add each found image and title, description and tags to list
            images_path_list.append([
                (parser.parse(response.content)).title,
                (parser.parse(response.content)).description,
                (parser.parse(response.content)).tags,
                image_path])
            
            # Test: print images list
            print(images_path_list)
            print("\n\n")
            

# Write file information to excel
workbook = xlsxwriter.Workbook('designImages.xlsx')
worksheet = workbook.add_worksheet()

for row, (path) in enumerate(images_path_list):
    # Write to excel file (title, description, tags, path)
    worksheet.write(row, 0, path[0])  
    worksheet.write(row, 1, path[1])
    worksheet.write(row, 2, path[2])
    worksheet.write(row, 3, path[3])
    
    # Autofit the worksheet.
    worksheet.autofit()
workbook.close()

