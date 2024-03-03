import os

# Check if the script is run as root
if os.geteuid() == 0:
    print("This script is running as root")
else:
    print("This script must be run as root")
    exit(1)
    
# Continue with other commands if running as root
os.system('mkdir user')
