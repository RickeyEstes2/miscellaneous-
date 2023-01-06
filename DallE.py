import os
import openai

openai.api_key = ('API_KEY_GOES_HERE')


prompt = input("What do you want to draw? ")

response = openai.Image.create(
  prompt=prompt,
  n=1,
  size="1024x1024"
)
image_url = response['data'][0]['url']
#print(image_url)

import urllib.request

# Download the file from `url` and save it locally under `file_name`:
url = image_url

#file_name = 'dalleimage.png'

#
#
#
#

import os

# Set the file name
filename = "image.jpg"

# Keep checking if the file exists
while os.path.exists(filename):
    # Split the file name and get the number
    name, ext = os.path.splitext(filename)
    num = name.split("_")[-1]

    # Check if the last part of the name is a number
    if num.isdigit():
        # Increment the number
        num = int(num) + 1
        filename = name[:-len(str(num))] + str(num) + ext
    else:
        # If the last part of the name is not a number, add _1
        filename = name + "_1" + ext

# Save the file
with open("DallE.txt", "w") as f:
    f.write(prompt)
    f.write(filename)
    
#
#
#
#
file_name = filename

urllib.request.urlretrieve(url, file_name)
print("Saved as: ", file_name)
