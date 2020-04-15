import os, subprocess

# builds build.py
#os.system("python build.py")

# sets up containers
#os.system("docker-compose build")

#install gnome terminal
os.system("sudo apt-get -f install gnome-terminal")

print("downloaded gnome-terminal")      # Debugging

# Opens two seperate "terminals" using gnome-terminal.
# this is essential because we need to run the dbsetup while the db containers
# are spinning.
proc1 = subprocess.Popen(['gnome-terminal', '--', 'python', 'special.py'])
proc2 = subprocess.Popen(['gnome-terminal', '--', 'python', 'other_special.py'])