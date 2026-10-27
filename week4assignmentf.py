import requests
import sys
import json

if len(sys.argv)<2:
    print("Missing command line argument")

else:
    try:
        amt=float(sys.argv[1])

    except ValueError:
        sys.exit("Command line argument is not a number")
API_KEY=""   # i am removing the api key for now; if you want to generate api key go to coincap api management for bitcoin;; and if you want new api keys you need to access those api keys specifially from individual companies;
url=f"https://rest.coincap.io/v3/assets/bitcoin?apiKey={API_KEY}"
try:
    response=requests.get(url)  ; # response in json formmat; neither a dictinary nor a string so convert it to dcitionary in the next line;; this is just an object containing various things
    json_data=response.json() ; #now it is converted to dictionary which can be accessed by me

    print (response) # prints just response and nothing like this; because it is an object ; to access the text inside it; response.text
    print(json.dumps(json_data,indent=2))  #now; json.dumps convert the dictionary back into the string; because to access the dictionary first i should know what are the contents inside of it;;  also now i have the power to format that string;; using string manipulations
    price_string = json_data["data"]["priceUsd"] # accessing the dictionary key vaue pairs;  this is a case of nested dictionary where inside one dictionary there is a key data; and inside that data there is another dictionary having key as price usd;
    bitcoin_rate = float(price_string)
        
except requests.RequestException:
    sys.exit("API request failed")

    # 4. Perform the conversion math and output the exact currency structure
total_cost = amt * bitcoin_rate
print(f"${total_cost:,.4f}")
    
     