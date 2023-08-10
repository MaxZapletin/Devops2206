import requests
response = requests.get("https://api.github.com/users/avielb/repos")
repositories = response.json()

for repo in repositories:
    if "DEVOPS" in repo["name"].upper():
        print(repo["name"].upper())


# import requests
# response = requests.get("https://github.com/012ddasdasdasdasdasd")
# if response.status_code == 200:
#     print("github is up and running")
# else:
#     print("Github is Down" + str(response.status_code))

