import requests

# Replace 'YOUR_BEARER_TOKEN' with your actual Bearer Token
bearer_token = "AAAAAAAAAAAAAAAAAAAAAIZAywEAAAAA0wOdZqCtMy3CRCgQ%2BVTL0rO0yLM%3DjNxxLb7sAQL1KUCk1iPkUU6WwNVpjEvsXW9KNe3JDFnFqie7t0"

url = "https://api.twitter.com/2/tweets/search/stream"  # Correct Twitter API endpoint

headers = {
    "Authorization": f"Bearer {bearer_token}"  # Properly formatted Authorization header
}

response = requests.request("GET", url, headers=headers)

if response.status_code == 200:
    print("Streaming data:")
    for line in response.iter_lines():
        if line:
            print(line.decode("utf-8"))
else:
    print(f"Error: {response.status_code}")
    print(response.text)
