import requests

# define the API endpoint
url = "http://34.122.151.95/generate"

# define the processed data for text generation
# this is a sample text, you can change it later
text = "One day"

data = {
    "processed_data": f"{text}"
}

# make the POST request to the FastAPI endpoint
response = requests.post(url, json=data)

# check if the request was successful
if response.status_code == 200:
    # print the generated text from the response
    generated_text = response.json()
    print(f"Generated Text: {generated_text['generated_text']}")
else:
    print(f"Error: {response.status_code}, {response.text}")