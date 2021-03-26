import os
import shutil
import requests
import json
import time
import sys
import subprocess as sp
from github import Github
from requests.auth import HTTPBasicAuth

root='.'
hostname = 'https://api.github.com/users/wasuaje'
token = "623d8270373a34eb956090b2efb1adb19d6ba2ff"
code= "385876a2329b824c656e"

CLIENT_ID = os.environ['CLIENT_ID']
CLIENT_SECRET = os.environ['CLIENT_SECRET']

# remove .git folder
def remove_dotgit():
    for item in os.listdir(root):
        if os.path.isdir(os.path.join(root, item)):
            to_remove = os.path.join(root, item, '.git')
            if os.path.isdir(to_remove):
                print(f"Removing: {to_remove}")
                shutil.rmtree(to_remove)                

def add_fotgitignore():
    src = os.path.join(root, 'gitignore_template')
    dst = '.gitignore'
    for item in os.listdir(root):
        folder = os.path.join(root, item)
        if os.path.isdir(folder):
            dest = os.path.join(folder, dst)            
            print(f"Copying .gitignore from {src} to {dest}")
            shutil.copy(src, dest)                        

    
def git_login():    
    # req=requests.get(hostname, auth=HTTPBasicAuth('wasuaje', access_token))
    # print(req.json())
    # print(CLIENT_ID, CLIENT_SECRET)
    print("GRAB de CODE FROM HERE NEXT URL PASTED IN URL")
    print(f"https://github.com/login/oauth/authorize?scope=public_repo&client_id={CLIENT_ID}")
    print("UPDATE CODE VARIABLE AND RUN AGAIN, UPDATE TOKEN")
    response = requests.get(f"https://github.com/login/oauth/authorize?scope=user:email&client_id={CLIENT_ID}")
    # print(response, response.text)
    data = {"client_id": CLIENT_ID,
            "client_secret": CLIENT_SECRET,
            "code": code}
    response = requests.post('https://github.com/login/oauth/access_token', data= data)
    print(response,response.text)
           
def get_repos():    
    req=requests.get(f"{hostname}/repos")    
    return req.json()

def repo_exists(repo_list, repo_name):    
    repo_list_name = [repo["name"] for repo in repo_list]
    if repo_name in repo_list_name:
        return True
    else:
        return False

def create_repos(repo_name):  
    _hostname = 'https://api.github.com/user/repos'
    headers = {"Accept": "application/vnd.github.v3+json", "Authorization": f"Bearer {token}" }
    data = {"name": repo_name, "private": False}
    response = requests.post(f"{_hostname}", json=data, headers=headers)    
    return response

def push_repo(path, repo_name):
    os.chdir(path)

    cmds = ["git init",
            f"git remote add origin https://github.com/wasuaje/{repo_name}.git",
            "git add .",
            "git commit -m first_commit",
            "git branch -M main",
            "git push -u origin main"]
    for cm in cmds:        
        try:
            output = sp.check_output(cm, shell=True )
            # p = sp.Popen(cm, stdout=sp.PIPE, shell=True)
            output = output.decode("utf-8")
            # proc = sp.Popen(cm, shell=True)
            # returncode = proc.wait()
            print(output)
        except sp.CalledProcessError as grepexc:                                                                                                   
            print("error code", grepexc.returncode, grepexc.output)
            sys.exit(1)        
    os.chdir("../")    
    return

def run():    
    for item in os.listdir(root):            
        print(f"#########{ os.curdir, item } #########{ os.path.isdir(os.path.join(root, item)) }")
        if os.path.isdir(os.path.join(root, item)):            
            rtn = process_folders(root, item)                        

def process_folders(root, item):        
    to_process = os.path.join(root, item)
    item_name = item.replace("./","")
    print(f"Processing: {item_name} - Existe {repo_exists(repos, item_name)}")
    if not repo_exists(repos, item):
        print("Creating Repo...")
        response = create_repos(item_name)
        if response.status_code == 201:                    
            print("Success at GIT level")                    
            print("Pushing repo data")
            rtn = push_repo(to_process, item_name)                    
            print("Finished")            
        else:
            print("FAILED")
            print(response, response.text)
    return True


# Following 2 just to standardize        
# remove_dotgit()
# add_fotgitignore()
# LOGIN only to get code and token
# git_login()
# ALwyas get repos
repos = get_repos()
# for repo in repos:
#     print(repo["name"])
#     # repo.edit(has_wiki=False)
#     # to see all the available attributes and methods
#     # print(dir(repo))
#Always process folders
run()

