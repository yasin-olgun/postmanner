import json

# Your array containing URL, request method, and body dictionary
requests_array = [
    {
        "url": "http://example.com/api/endpoint1",
        "method": "POST",
        "body": {"key1": "value1"}
    },
    {
        "url": "http://example.com/api/endpoint2",
        "method": "GET",
        "body": {"key2": "value2"}
    }
]

# Initialize an empty list to store request items
collection_items = []

# Loop through the requests array and construct collection items
for request_data in requests_array:
    request_item = {
        "name": "Request: " + request_data["url"],
        "request": {
            "method": request_data["method"],
            "url": request_data["url"],
            "body": {
                "mode": "raw",
                "raw": json.dumps(request_data["body"])  # Convert body dictionary to JSON string
            },
            "header": [
                {
                    "key": "Content-Type",
                    "value": "application/json"
                }
            ]
        },
        "response": []
    }
    collection_items.append(request_item)

# Define the Postman collection structure
postman_collection = {
    "info": {
        "name": "Dynamic Collection",
        "schema": "https://schema.getpostman.com/json/collection/v2.1.0/collection.json"
    },
    "item": collection_items
}

# Save the Postman collection to a JSON file
with open("dynamic_collection.json", "w") as f:
    json.dump(postman_collection, f, indent=4)
