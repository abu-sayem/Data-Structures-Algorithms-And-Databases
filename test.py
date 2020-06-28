import requests

endpoint_url = "https://api.spotify.com/v1/search?"

# OUR FILTERS
query = 'john lenon'
type = 'artist'
limit = 1
offset = 1
market = ''
token='BQC9q4ESGq62MuIhzjuyIzZVk9cNbyo-yga93h_bOB7rc3NqCyfHAibB8Bi4ht0PXu_rvfQguudSlbG8cLFiKEhHg4aYQhAwjTsBPD2_-WwbSiwurVRtNXbV6zBF0g4us5yYlzrYzoFS'

query = f'{endpoint_url}&query={query}&type={type}&offset={offset}&limit={limit}'

response = requests.get(query,
                        headers={"Content-Type": "application/json",
                                 "Authorization": token})
json_response = response.json()
