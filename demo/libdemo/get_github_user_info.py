import requests

# Call GITHUB Rest API
resp = requests.get("https://api.github.com/users/gvanrossum")
if resp.status_code  != 200:
   print("Sorry! Could not get details!")
   exit(1)

details = resp.json() # response converted to dict

print(f"Name        {details['name']}")
print(f"Location    {details['location']}")
print(f"Company     {details['company']}")
print(f"Followers   {details['followers']}")
