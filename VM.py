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

#Create a Python Script

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

# Run the Flask Application
python3 shivani.py

#Install Curl on VM2 and Test the Microservice

sudo snap install curl

# execute the following command in VM2 to test microservice is accessible

curl http://192.168.1.4:5000
