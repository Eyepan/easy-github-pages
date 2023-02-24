import os

if not os.path.exists(".git"):
    print("Initializing Git repository...")
    os.system("git init")
    os.system("git add .")

status = os.system("git remote -v")
if status != 0:
    repo_name = input("Enter the URL of the remote repository: ")
    os.system(f"git remote add origin {repo_name}")


commit_message = input("Enter a commit message: ")
print(f"Comitting with message {commit_message}")
os.system(f'git add .')
os.system(f'git commit -m "{commit_message}"')
print("Pushing to master")
os.system("git push origin master")
