import os
import shutil
import subprocess

def download_github_repo(repo_url, folder_path):
    # Attempt to delete the folder if it exists
    try:
        shutil.rmtree(folder_path)
    except PermissionError as e:
        print(f"Failed to delete {folder_path}: {e}")
        pass

    # Clone the GitHub repo
    subprocess.run(["git", "clone", repo_url, folder_path])

if __name__ == "__main__":
    repo_url = "https://github.com/Episode353/joepack"
    folder_path = "joepack"

    download_github_repo(repo_url, folder_path)



# to build use command
# pyinstaller joepack-updater.py --onefile