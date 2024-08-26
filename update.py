"""
@Author: Icingworld
@Description: Push the latest version to github or pull from github
@Usage: python update.py [push/pull]
@Github: https://github.com/Icingworld
"""

import sys
import os


yes = ['y', 'Y', 'yes', 'Yes']
no = ['n', 'N', 'no', 'No']

def updateList():
    folders = ['easy', 'moderate', 'hard']
    all_files = []

    with open('List.md', 'w', encoding='utf-8') as f:
        f.write('# Leetcode Log\n\n')
        for folder in folders:
            if os.path.exists(folder):
                f.write(f'## {folder}\n\n')
                files = os.listdir(folder)
                for file in files:
                    filename = file[:-3]
                    order, name = filename.split('.')
                    all_files.append({"order": order, "name": name})

            all_files.sort(key=lambda x: x['order'])
            for file in all_files:
                f.write(f'+ [{file["order"]}.{file["name"]}]({folder}/{file["order"]}.{file["name"]}.md)\n\n')

            all_files.clear()

    print("List.md updated successfully.")

def isChanged():
    status = os.popen('git status --porcelain').read().strip()
    return len(status) > 0

cmd = sys.argv[1]
if cmd == 'pull':
    ans = input('This will pull the latest version from github, continue?[y/n]')
    if ans in yes:
        print('Pulling from github...')
        os.system('git pull')
    else:
        print('Abort')

elif cmd == 'push':
    if not isChanged():
        print('No changes to commit. Abort.')
    else:
        ans = input('This will push the latest version to github, continue?[y/n]')
        if ans in yes:
            print('Update List.md...')
            updateList()
            print('Pushing to github...')
            os.system('git add .')
            os.system('git commit -m "update"')
            os.system('git push -u origin main')
        else:
            print('Abort')
