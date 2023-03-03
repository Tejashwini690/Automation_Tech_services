import os

print("\t\t\t\tWelcome to automation world")
print("\t\t\t\t---------------------------")
print("\t\t\t\tChoose which automation you want to do:")
print("\t\t\t\t---------------------------------------")
print('''
	   \t\t\tAutomation:1 AWS Service Automation
	   \t\t\tAutomation:2 Logical Volume Managment Automation
	   \t\t\tAutomation:3 Docker Automation 
	   \t\t\tAutomation:4 Hadoop Cluster Setup
	   \t\t\tAutomation:5 Webserver Configure Automation
	''')
automation_number = input("\t\t\t\tEnter automation number:")
automation_number = int(automation_number)

if(automation_number==1):
	os.system("python aws_automation.py")

elif(automation_number==2):
	os.system("python LVM_automation.py")

elif(automation_number==3):
	os.system("python Docker_automation.py")

elif(automation_number==4):
	os.system("python automate_hadoop_cluster.py")

elif(automation_number==5):
	os.system("python webserver_automation.py")

else:
	print("invalid choice")
