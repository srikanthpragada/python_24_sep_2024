import requests

# Call GITHUB Rest API
resp = requests.get("https://api.github.com/users/srikanthpragada/repos")
if resp.status_code  != 200:
   print("Sorry! Could not get details!")
   exit(1)

repos = resp.json() # response converted to dict

for repo in repos:
   print(f"Name        {repo['name']}")
   print(f"Location    {repo['created_at']}")

