# How to Set up Elastic Beanstalk Command Line Interface for deploying as web application in AWS Elastic Beanstalk<br/>

1. Clone this repository<br/>```git clone https://github.com/zhiwebby/ImagePredictionFoodSG.git```
2. ```cd path/to/project``` # cd to the directory where requirements.txt is located.<br/>
3. ```python -m venv path/to/project``` # creates a virtual in where requirements.txt is located.<br/>
4. ```.\Scripts\activate``` #activates the virtual environment<br/>
5. ```pip install -r requirements.txt``` #installs the required packages<br/>
6. Clone another Github repository (https://github.com/aws/aws-elastic-beanstalk-cli-setup) in another directory from the ImagePredictionFoodSG repository.<br/>
```git clone https://github.com/aws/aws-elastic-beanstalk-cli-setup.git```<br/>
6. Install/Upgrade the EB CLI<br/>
By running as Administrator, in PowerShell or in a Command Prompt window, run the following line:<br/>
```.\aws-elastic-beanstalk-cli-setup\scripts\bundled_installer```<br/>
7. Troubleshooting<br/>
For Windows:<br/>
In PowerShell, if you encounter an error with the message "execution of scripts is disabled on this system", set the execution policy to "RemoteSigned" and then rerun bundled_installer.<br/>
```Set-ExecutionPolicy RemoteSigned```<br/>
If you encounter an error with the message "No module named 'virtualenv'", use the following commands to install virtualenv and the EB CLI:<br/>
```pip uninstall -y virtualenv```<br/>
```pip install virtualenv```<br/>
```python .\aws-elastic-beanstalk-cli-setup\scripts\ebcli_installer.py```<br/>
8. Running steps 6 - 8 on my powershell looked like the following:
```
PS D:\aws-elastic-beanstalk-cli-setup-master\aws-elastic-beanstalk-cli-setup-master\scripts> Set-ExecutionPolicy RemoteSigned

Execution Policy Change
The execution policy helps protect you from scripts that you do not trust. Changing the execution policy might expose
you to the security risks described in the about_Execution_Policies help topic at
https:/go.microsoft.com/fwlink/?LinkID=135170. Do you want to change the execution policy?
[Y] Yes  [A] Yes to All  [N] No  [L] No to All  [S] Suspend  [?] Help (default is "N"): y
PS D:\aws-elastic-beanstalk-cli-setup-master\aws-elastic-beanstalk-cli-setup-master\scripts> .\bundled_installer
.\bundled_installer : File
D:\aws-elastic-beanstalk-cli-setup-master\aws-elastic-beanstalk-cli-setup-master\scripts\bundled_installer.ps1 cannot
be loaded. The file
D:\aws-elastic-beanstalk-cli-setup-master\aws-elastic-beanstalk-cli-setup-master\scripts\bundled_installer.ps1 is not
digitally signed. You cannot run this script on the current system. For more information about running scripts and
setting execution policy, see about_Execution_Policies at https:/go.microsoft.com/fwlink/?LinkID=135170.
At line:1 char:1
+ .\bundled_installer
+ ~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : SecurityError: (:) [], PSSecurityException
    + FullyQualifiedErrorId : UnauthorizedAccess
PS D:\aws-elastic-beanstalk-cli-setup-master\aws-elastic-beanstalk-cli-setup-master\scripts> python .\ebcli_installer.py

***********************************
1. Locating virtualenv installation
***********************************

******************************************
2. Creating exclusive virtualenv for EBCLI
******************************************
created virtual environment CPython3.9.1.final.0-64 in 1205ms
  creator CPython3Windows(dest=C:\Users\Zhiwen\.ebcli-virtual-env, clear=False, no_vcs_ignore=False, global=False)
  seeder FromAppData(download=False, pip=bundle, setuptools=bundle, wheel=bundle, via=copy, app_data_dir=C:\Users\Zhiwen\AppData\Local\pypa\virtualenv)
    added seed packages: PyYAML==5.4.1, awsebcli==3.20.0, botocore==1.20.112, cement==2.8.2, certifi==2021.5.30, charset_normalizer==2.0.3, colorama==0.4.3, future==0.16.0, idna==3.2, jmespath==0.10.0, pathspec==0.5.9, pip==21.1.1, pip==21.1.3, pypiwin32==223, python_dateutil==2.8.2, pywin32==301, requests==2.26.0, semantic_version==2.8.5, setuptools==56.0.0, setuptools==57.0.0, setuptools==57.4.0, six==1.14.0, termcolor==1.1.0, urllib3==1.25.11, wcwidth==0.1.9, wheel==0.36.2
  activators BashActivator,BatchActivator,FishActivator,PowerShellActivator,PythonActivator,XonshActivator

************************
3. Activating virtualenv
************************

*******************
4. Installing EBCLI
*******************
Requirement already satisfied: awsebcli in c:\users\zhiwen\.ebcli-virtual-env\lib\site-packages (3.20.0)
Requirement already satisfied: pypiwin32==223 in c:\users\zhiwen\.ebcli-virtual-env\lib\site-packages (from awsebcli) (223)
Requirement already satisfied: future<0.17.0,>=0.16.0 in c:\users\zhiwen\.ebcli-virtual-env\lib\site-packages (from awsebcli) (0.16.0)
Requirement already satisfied: botocore<1.21.0,>=1.19.0 in c:\users\zhiwen\.ebcli-virtual-env\lib\site-packages (from awsebcli) (1.20.112)
Requirement already satisfied: semantic-version==2.8.5 in c:\users\zhiwen\.ebcli-virtual-env\lib\site-packages (from awsebcli) (2.8.5)
Requirement already satisfied: pathspec==0.5.9 in c:\users\zhiwen\.ebcli-virtual-env\lib\site-packages (from awsebcli) (0.5.9)
Requirement already satisfied: colorama<0.4.4,>=0.2.5 in c:\users\zhiwen\.ebcli-virtual-env\lib\site-packages (from awsebcli) (0.4.3)
Requirement already satisfied: setuptools>=20.0 in c:\users\zhiwen\.ebcli-virtual-env\lib\site-packages (from awsebcli) (57.4.0)
Requirement already satisfied: python-dateutil<3.0.0,>=2.1 in c:\users\zhiwen\.ebcli-virtual-env\lib\site-packages (from awsebcli) (2.8.2)
Requirement already satisfied: six<1.15.0,>=1.11.0 in c:\users\zhiwen\.ebcli-virtual-env\lib\site-packages (from awsebcli) (1.14.0)
Requirement already satisfied: PyYAML<5.5,>=5.3.1 in c:\users\zhiwen\.ebcli-virtual-env\lib\site-packages (from awsebcli) (5.4.1)
Requirement already satisfied: urllib3<1.26,>=1.25.4 in c:\users\zhiwen\.ebcli-virtual-env\lib\site-packages (from awsebcli) (1.25.11)
Requirement already satisfied: termcolor==1.1.0 in c:\users\zhiwen\.ebcli-virtual-env\lib\site-packages (from awsebcli) (1.1.0)
Requirement already satisfied: wcwidth<0.2.0,>=0.1.7 in c:\users\zhiwen\.ebcli-virtual-env\lib\site-packages (from awsebcli) (0.1.9)
Requirement already satisfied: requests<=2.26,>=2.20.1 in c:\users\zhiwen\.ebcli-virtual-env\lib\site-packages (from awsebcli) (2.26.0)
Requirement already satisfied: cement==2.8.2 in c:\users\zhiwen\.ebcli-virtual-env\lib\site-packages (from awsebcli) (2.8.2)
Requirement already satisfied: pywin32>=223 in c:\users\zhiwen\.ebcli-virtual-env\lib\site-packages (from pypiwin32==223->awsebcli) (301)
Requirement already satisfied: jmespath<1.0.0,>=0.7.1 in c:\users\zhiwen\.ebcli-virtual-env\lib\site-packages (from botocore<1.21.0,>=1.19.0->awsebcli) (0.10.0)
Requirement already satisfied: idna<4,>=2.5 in c:\users\zhiwen\.ebcli-virtual-env\lib\site-packages (from requests<=2.26,>=2.20.1->awsebcli) (3.2)
Requirement already satisfied: charset-normalizer~=2.0.0 in c:\users\zhiwen\.ebcli-virtual-env\lib\site-packages (from requests<=2.26,>=2.20.1->awsebcli) (2.0.3)
Requirement already satisfied: certifi>=2017.4.17 in c:\users\zhiwen\.ebcli-virtual-env\lib\site-packages (from requests<=2.26,>=2.20.1->awsebcli) (2021.5.30)
WARNING: You are using pip version 21.1.3; however, version 21.2.1 is available.
You should consider upgrading via the 'C:\Users\Zhiwen\.ebcli-virtual-env\Scripts\python.exe -m pip install --upgrade pip' command.

***********************
5. Creating EB wrappers
***********************

***************
6. Finishing up
***************
Success!

EBCLI has been installed.
```
9. In file explorer, navigate to C:\Users\<type-your-account-name>\.ebcli-virtual-env\executables<br/>
There will be 4 files.<br/>
Hover over the VBScript Script File named path_exporter.vbs and right click > create shortcut.<br/>
Change the shortcut to name "eb.vbs"<br/>
Right click the shortcut > cut.<br/>
Navigate to the location of the requirements.txt in ImagePredictionFoodSG repository and right click > paste.<br/>
You should have a shortcut called eb.vbs in the same directory as requirements.txt now.<br/>
9. Using your command line, setup a new EB application by entering the following command:<br/>
```eb init```<br/>
10. You will be prompted to select a Region you'd like to deploy the application in. Select a region near you. Type the number representing ap-southeast-1 for Asia Pacific (Singapore).<br/>
```
Select a default region
1) us-east-1 : US East (N. Virginia)
2) us-west-1 : US West (N. California)
3) us-west-2 : US West (Oregon)
4) eu-west-1 : EU (Ireland)
5) eu-central-1 : EU (Frankfurt)
6) ap-south-1 : Asia Pacific (Mumbai)
7) ap-southeast-1 : Asia Pacific (Singapore)
8) ap-southeast-2 : Asia Pacific (Sydney)
9) ap-northeast-1 : Asia Pacific (Tokyo)
10) ap-northeast-2 : Asia Pacific (Seoul)
11) sa-east-1 : South America (Sao Paulo)
12) cn-north-1 : China (Beijing)
13) cn-northwest-1 : China (Ningxia)
14) us-east-2 : US East (Ohio)
15) ca-central-1 : Canada (Central)
16) eu-west-2 : EU (London)
17) eu-west-3 : EU (Paris)
18) eu-north-1 : EU (Stockholm)
19) eu-south-1 : EU (Milano)
20) ap-east-1 : Asia Pacific (Hong Kong)
21) me-south-1 : Middle East (Bahrain)
22) af-south-1 : Africa (Cape Town)
(default is 3): 7
```
11. You will be prompted to create a new application if you haven't. Type the number representing create a new application.<br/>
```
Select an application to use
1) testing
2) myflaskapp
3) [ Create new Application ]
(default is 3): 3
```
12. You will be prompted to fill in your application name. Change the name if you want.<br/>
```
Enter Application Name
(default is "AWS_test_deploy"): deploy_test
Application deploy_test has been created.
```
13. Now in your browser, type in the following url and login to AWS.<br/>
```https://console.aws.amazon.com/iam/home?#/security_credentials```<br/>
Under Your Security Credentials tab, select Access keys (access key ID and secret access key) tab, select Create New Access Key.<br/>
Copy the Access key id and Secret access key for later use.<br/>
14. Now navigate back to your command line and paste the access key id and secret access key.<br/>
```
(aws-access-id): AKIAJOUAASEXAMPLE
(aws-secret-key): 5ZRIrtTM4ciIAvd4EXAMPLEDtm+PiPSzpoK
```
15. AWS will automatically detect the python code and prompt you to choose the platform version.
```
It appears you are using Python. Is this correct?
(Y/n): Y
Select a platform branch.
1) Python 3.8 running on 64bit Amazon Linux 2
2) Python 3.7 running on 64bit Amazon Linux 2
3) Python 3.6 running on 64bit Amazon Linux (Deprecated)
(default is 1): 1
```
16. You won't need to SSH into your instances for this tutorial. For the "Do you want to set up SSH for your instances?" prompt, answer No. This concludes the setup of your application.<br/>
```
Cannot setup CodeCommit because there is no Source Control setup, continuing with initialization
Do you want to set up SSH for your instances?
(Y/n): n
```
17. Go to your browser, type in https://ap-southeast-1.console.aws.amazon.com/elasticbeanstalk/home?region=ap-southeast-1#/applications<br/>
Select your new application deploy_test and you will be directed to the environment page for deploy_test.<br/>
18. Select create a new environment.<br/>
19. You will be prompted to select environment tier.<br/>
Select Web server environment<br/>
19. Under Create a web server environment tab, you will have to fill up Application name.<br/>
Under Environment information tab, you will have to fill Environment name and Domain.<br/>
20. Under the Platform, select Python for Platform options.<br/>
Under the Platform branch, ensure that Python 3.8 running on 64bit Amazon Linux 2 is selected.<br/>
Under the Platform version, ensure that 3.3.3 (Recommended) is selected.<br/>
21. Under the Application code tab, you will have to select upload your code.<br/>
Under Source code origin, ensure that Local file is selected.<br/>
Select Choose file and upload the compressed file of ImagePredictionFoodSG repository<br/>
Ensure that the compressed file does not exceed the maximum size 512 MB.<br/>
Ensure that the compressed file contains the following contents before uploading.<br/>
```
ImagePredictionFoodSG
|--.elasticbeanstalk
|--Include
|--Lib
|--Scripts
|--.gitignore.txt
|--application.py
|--eb VB Script File (shortcut)
|--pyvenv.cfg
|--requirements.txt
```
22. Wait for the environment to be created in a few minutes.<br/>
23. Navigate to the dashboard page of your environment or click on your environment on the left side of your page.<br/>
24. Copy the domain name of your environment for later. The domain name can be found in your dashboard below the environment name.<br/>
```For example: myflaskappenv.eba-example.ap-southeast-1.elasticbeanstalk.com```<br/>
25. Type in the browser https://github.com/wangzksit/NutriCare/blob/main/app/src/main/java/com/example/nutricare/ImageRecognitionUtil/ImageRecognitionSingleton.kt and navigate to the page.<br/>
26. Change the line 47 in ImageRecognitionSingleton.<br/>
```val postUrl = "http://myflaskappenv.eba-example.ap-southeast-1.elasticbeanstalk.com" #Change to your own environment domain```
27. You should now be able to send POSTMAN POST requests to the domain name. I sent a picture of a sambal prawn through form data with the key "image".
![image](https://user-images.githubusercontent.com/16185401/127535168-b32fb13e-4807-436c-b3ef-b6bbf3d03eeb.png)
![image](https://user-images.githubusercontent.com/16185401/127536330-58510036-a7f6-4cc0-8663-2f408bc01d13.png)

<br/>
<br/>
For full documentation of how to install AWS EB CLI for steps 6 - 9: https://github.com/aws/aws-elastic-beanstalk-cli-setupk/<br/>
