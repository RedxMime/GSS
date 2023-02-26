import subprocess

dir = "Spam"

for token in open(f"{dir}emailpass.txt","r").read().splitlines():
    subprocess.Popen(['python3',f'{dir}bot.py',token.split(':')[0],token.split(':')[1]])
