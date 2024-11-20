# Deploying Flask Web Application on Ec2 Instance 
This project shows how to deploy existing flask web application on Ec2 instance 
## Requirements
+ Python 3.x - https://www.python.org/downloads/
+ Flask - sudo pip install flask 
## Steps to deploy 
1. Clone the Repository
   + use git clone command to clone source code - git clone https://github.com/phaneendra300/Flask-Web-app.git
2. Start the web sever and run the Application
   + Execute the below commands to start the web server and run the application
   + cd flask-web-app
   + pyhton3 app.py 
3. Open the port 5000 using security groups
   + Create new security group and add port 5000 in the inbound rules of security group  
7. Access the Application
   + http://<public_ip>:50000
