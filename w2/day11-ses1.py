import requests
import json
print("="*60)
print("API BASICS PRACTICE")
print("="*60 + "\n")
print("--- 1. Fetching Random Quote ---\n")
try:
    response = requests.get("https://zenquotes.io/api/random")
    print(f"Status Code: {response.status_code}")
    if response.status_code == 200:
        data = response.json()
        quote = data[0]
        print(f"Success!")
        print(f"\nQuote: \"{quote['q']}\"")
        print(f"Author: {quote['a']}")
        print(f"Length: {len(quote['q'])} characters")
    else:
        print(f"Error: {response.status_code}")
except Exception as e:
    print(f"Error occurred: {e}")
print("\n" + "="*60)
print("--- 2. Fetching Motivational Quote ---\n")
try:
    params = {"tags": "inspirational"}
    response = requests.get("https://zenquotes.io/api/random", params=params)
    if response.status_code == 200:
        data = response.json()
        quote = data[0]
        print(f"Motivational Quote:")
        print(f"\"{quote['q']}\"")
        print(f"- {quote['a']}")
except Exception as e:
    print(f"Error: {e}")
print("\n" + "="*60)
print("--- 3. Fetching Multiple Quotes ---\n")
try:
    for i in range(1, 4):
        response = requests.get("https://zenquotes.io/api/random")
        if response.status_code == 200:
            data = response.json()
            quote = data[0]
            print(f"{i}. \"{quote['q']}\" - {quote['a']}")
        else:
            print(f"{i}. Error fetching quote")
except Exception as e:
    print(f"Error: {e}")
print("\n" + "="*60)
print("--- 4. Understanding API Response ---\n")
try:
    response = requests.get("https://zenquotes.io/api/random")
    print("Response Details:")
    print(f"Status Code: {response.status_code}")
    print(f"Headers: {dict(list(response.headers.items())[:3])}...")
    print(f"\nRaw JSON Response:")
    print(response.text[:200] + "...")
    data = response.json()
    quote = data[0]
    print(f"\nPython Dictionary:")
    print(f" Type: {type(data)}")
    print(f" First item type: {type(quote)}")
    print(f" Keys in first item: {list(quote.keys())}")
    print(f" Content: {quote['q'][:50]}...")
except Exception as e:
    print(f"Error: {e}")
    print("\n" + "="*60)
    print("--- 5. Handling Errors ---\n")
try:
    response = requests.get("https://zenquotes.io/api/nonexistent")
    print(f"Status Code: {response.status_code}")
    if response.status_code == 404:
        print("Endpoint not found!")
    elif response.status_code == 200:
        print("Success!")
    else:
        print(f"Unexpected status: {response.status_code}")
except requests.exceptions.RequestException as e:
    print(f"Network error: {e}")
print("\n" + "="*60)
print("--- 6. Working with JSON ---\n")
study_data = {
    "group": "Python Warriors",
    "members": ["Alex", "Jordan", "Sam"],
    "total_hours": 25.5,
    "active": True
}
json_string = json.dumps(study_data, indent=2)
print("Python dict converted to JSON:")
print(json_string)
parsed_data = json.loads(json_string)
print(f"\nParsed back to Python: {parsed_data['group']}")
print("\n" + "="*60)
print("--- 7. Building API Requests ---\n")
base_url = "https://zenquotes.io/api/random"
params1 = {
    "maxLength": 100,
    "tags": "wisdom"
}
response = requests.get(base_url, params=params1)
if response.status_code == 200:
    data = response.json()
    quote = data[0]
    print(f"Short wisdom quote: \"{data[0]['q']}\"")
url_with_params = "https://zenquotes.io/api/random?tags=friendship"
response = requests.get(url_with_params)
if response.status_code == 200:
    data = response.json()
    quote = data[0]
    print(f"\nFriendship quote: \"{quote['q']}\"")
print("\n" + "="*60)
print("Practice Complete!")
print("="*60 + "\n")




        