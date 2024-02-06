import requests

# Example: Fetch a list of posts
response = requests.get('https://jsonplaceholder.typicode.com/posts')

if response.status_code == 200:
    # Print the first post in the response
    print(response.json()[0])
else:
    print(f"Error: {response.status_code}")
