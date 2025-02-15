# check Ip address for for the VM machine using below command in both VM 
ip a 

# check two Virtual Machines (VMs) are properly connected using ping and their respective IP addresses.
# for VM1 
ping 192-168.1.5
# for VM2 
ping 192-168.1.4

#Install python and Python flask using below commands in both VM:
sudo apt update
sudo apt install python3-pip
pip3 install flask

#after installing Python and Flask in both the VM’s
# execute the below command to create file

nano shivani.py

#Now write below code in the VM1 terminal

from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, I am shivani'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
  
#Now press below shortcut to save the file
#Press Ctrl + x
#The give Y
#Then Press Enter

# To execute a Python script run below mentioned command
python3 shivani.py

#Now In VM2 install curl using below commands

sudo snap install curl

# Then execute below commands to check the final

curl http://192.168.1.4:5000
