import requests
print("**Commit Loger**")
owner = input("Enter repo owner: ")
repo_name = input("Enter repo name: ")
r = requests.get(f"https://api.github.com/repos/{owner}/{repo_name}/commits")
data = r.json()
for commit in data:
    print("commit #", commit['sha'], sep='')
    print("Author:", commit['commit']['author']['name'])
    print("Message:", commit['commit']['message'])
print("done")


'''
#Adam's aside on dictionaries
data = {
    'First Name': 'Adam'
}
data['Last Name'] = 'Carter'
data['role'] = "Developer"
data[0] = "asdfsdfd"
for key in data:
    print("key:", key, "value: ", data[key])
'''