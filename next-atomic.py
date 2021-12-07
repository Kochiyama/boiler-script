import sys
import os

user = str(sys.argv[1])
project_name = str(sys.argv[2])

print("=-" * 20)
print("Initializing Next App with Typescript")
print("Git user: " + user)
print("Project name: " + project_name)
print("=-" * 20)

os.system('npx create-next-app@latest --typescript ' + project_name)
os.chdir('./' + project_name)
os.system('mkdir ./src')
os.system('mv ./pages ./src/pages ')
os.system('mv ./styles ./src/styles')
os.system('mkdir ./src/components')
os.system('mkdir ./src/components/atoms')
os.system('mkdir ./src/components/molecules')
os.system('mkdir ./src/components/organisms')
os.system('mkdir ./src/components/templates')

os.system('git branch master')
os.system('git checkout master')
os.system('git branch -d main')
os.system('git add .')
os.system('git commit -m "Chore: Initialized Next with boiler script!"')
os.system('gh repo create {} -y --private'.format(project_name))
os.system('git remote add origin https://github.com/{}/{}.git'.format(user, project_name))
os.system('git push origin master')

os.system('code .')