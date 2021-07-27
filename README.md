# How to Set up Elastic Beanstalk Command Line Interface for deploying as web application in AWS Elastic Beanstalk<br/>

1. ```cd path/to/project``` # cd to the directory where requirements.txt is located.<br/>
2. ```python -m venv path/to/project``` # creates a virtual in where requirements.txt is located.<br/>
3. ```.\Scripts\activate``` #activates the virtual environment<br/>
4. ```pip install -r requirements.txt``` #installs the required packages<br/>
5. Clone this repository<br/>
In another directory from requirements.txt. Clone the following github repo:<br/>
```git clone https://github.com/aws/aws-elastic-beanstalk-cli-setup.git```<br/>
6. Install/Upgrade the EB CLI<br/>
Running as Administrator, in PowerShell or in a Command Prompt window:<br/>
```.\aws-elastic-beanstalk-cli-setup\scripts\bundled_installer```<br/>
7. Troubleshooting<br/>
For Windows:<br/>
In PowerShell, if you encounter an error with the message "execution of scripts is disabled on this system", set the execution policy to "RemoteSigned" and then rerun bundled_installer.<br/>
```Set-ExecutionPolicy RemoteSigned```<br/>
If you encounter an error with the message "No module named 'virtualenv'", use the following commands to install virtualenv and the EB CLI:<br/>
```pip uninstall -y virtualenv```<br/>
```pip install virtualenv```<br/>
```python .\aws-elastic-beanstalk-cli-setup\scripts\ebcli_installer.py```<br/>
8. In file explorer, navigate to C:\Users\<type-your-account-name>\.ebcli-virtual-env\executables<br/>
There will be 4 files.<br/>
Hover over the VBScript Script File named path_exporter.vbs and right click > create shortcut.<br/>
Change the shortcut to name "eb.vbs"<br/>
Right click the shortcut > cut.<br/>
Navigate to the location of the requirements.txt and right click > paste.<br/>
You should have a shortcut called eb.vbs in same directory as requirements.txt<br/>
9. Using your command line, setup a new EB application by entering the following command:<br/>
```eb init```<br/>
10. You will be prompted to select a Region you'd like to deploy the application in. Select a region near you. Type ap-southeast-1 for Asia Pacific (Singapore).<br/>
```ap-southeast-1```
11. Now in your browser, type in the following url and login to AWS.<br/>
```https://console.aws.amazon.com/iam/home?#/security_credentials```<br/>
12. Under Your Security Credentials tab,<br/>
Select Access keys (access key ID and secret access key) tab<br/>
Select Create New Access Key<br/>
Copy the Access key id and Secret access key for later use.<br/>
13. Now navigate back to your command line and paste the access key id and secret access key.<br/>
```(aws-access-id): AKIAJOUAASEXAMPLE```<br/>
```(aws-secret-key): 5ZRIrtTM4ciIAvd4EXAMPLEDtm+PiPSzpoK```</br>
14. Now select a platform to use. You should choose Python. Type the number that corresponds to your choice and press Enter.<br/>
```
Select a platform.
1) Node.js
2) PHP
3) Python
4) Ruby
5) Tomcat
6) IIS
7) Docker
8) Multi-container Docker
9) GlassFish
10) Go
11) Java
(default is 1): 1
```
15. Now select the Python 3.8 version.<br/>
16. You won't need to SSH into your instances for this tutorial. For the "Do you want to set up SSH for your instances?" prompt, answer No. This concludes the setup of your application.<br/>
```
Do you want to set up SSH for your instances?
(y/n): n
```
This concludes the setup of your application. <br/>
17. Go to your browser, type in https://ap-southeast-1.console.aws.amazon.com/elasticbeanstalk/home?region=ap-southeast-1#/environments<br/>
Select create a new environment.<br/>
18. You will be prompted to select environment tier.<br/>
Select Web server environment<br/>
19. Under Create a web server environment tab, you will have to fill up Application name.<br/>
Under Environment information tab, you will have to fill Environment name and Domain.<br/>
20. Under the Platform, select Python for Platform options.<br/>
Under the Platform branch, ensure that Python 3.8 running on 64bit Amazon Linux 2 is selected.<br/>
Under the Platform version, ensure that 3.3.3 (Recommended) is selected.<br/>
21. Under the Application code tab, you will have to select upload your code.<br/>
Under Source code origin, ensure that Local file is selected.<br/>
Select Choose file and upload the compressed file of the root directory of requirements.txt<br/>
Ensure that the compressed file does not exceed the maximum size 512 MB.<br/>
22. Wait for the environment to be created in a few minutes.<br/>
23. Navigate to the dashboard page of your environment or click on your environment on the left side of your page.<br/>
24. Copy the domain name of your environment for later.<br/>
```For example: myflaskappenv.eba-example.ap-southeast-1.elasticbeanstalk.com```<br/>
25. Type in the browser https://github.com/wangzksit/NutriCare/blob/main/app/src/main/java/com/example/nutricare/ImageRecognitionUtil/ImageRecognitionSingleton.kt and navigate to the page.<br/>
26. Change the line 47.<br/>
```val postUrl = "http://myflaskappenv.eba-example.ap-southeast-1.elasticbeanstalk.com" #Change to your own environment domain```
<br/>
<br/>
For full documentation of how to install AWS EB CLI: https://github.com/aws/aws-elastic-beanstalk-cli-setupk/<br/>
