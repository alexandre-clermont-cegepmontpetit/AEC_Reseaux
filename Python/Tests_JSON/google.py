import requests

def query_google_doh(domain, record_type="A"):
    # Target endpoint
    url = "https://dns.google/resolve"
    
    # Query arguments
    params = {
        "name": domain,
        "type": record_type
    }
    
    # Send secure HTTPS request
    response = requests.get(url, params=params)
    
    if response.status_code == 200:
        data = response.json()
        if "Answer" in data:
            for answer in data["Answer"]:
                print(f"Type {answer['type']} Record found: {answer['data']}")
        else:
            print("No records found or error in resolution.")
    else:
        print(f"HTTP Error: {response.status_code}")

# Run sample execution
query_google_doh("web3.aclermont.com", "DS")
