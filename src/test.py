import os

import requests
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# API Configuration
try:
    api_key = os.getenv("LANGFLOW_API_KEY")
    print("API KEY loaded:", repr(api_key))
    if not api_key:
        raise ValueError("LANGFLOW_API_KEY is not set or is empty.")
except Exception as e:
    print(f"Error loading environment variables: {e}")
    exit(1)

# The complete API endpoint URL for this flow
url = "http://localhost:7860/api/v1/run/3766dbcb-b830-4c53-beaa-0b4d1421ca41"

# Request payload configuration
payload = {
    "output_type": "chat",
    "input_type": "chat",
    "input_value": "Quanto é 2 + 2?",
}

# Request headers
headers = {
    "Content-Type": "application/json",
    # Authentication key from environment variable
    "Authorization": f"Bearer {api_key}",
}

try:
    # Send API request
    response = requests.request("POST", url, json=payload, headers=headers)
    print("Status code:", response.status_code)
    print("Response headers:", response.headers)
    print("Response body:", response.text)
    response.raise_for_status()  # Raise exception for bad status codes

    # Print response
    print(response.text)

except requests.exceptions.RequestException as e:
    print(f"Error making API request: {e}")
except ValueError as e:
    print(f"Error parsing response: {e}")
