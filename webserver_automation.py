import os
print("\t\t\t\tWelcome to webserver configuration bot")
print("\t\t\t\t--------------------------------------")
IP = input("\t\t\t\tEnter IP at which you want to configure the web server: ")
#install httpd
os.system("ssh root@{} yum install httpd -y".format(IP))
#start service of httpd
os.system("ssh root@{} systemctl start httpd".format(IP))
#permanent enable the service of httpd
os.system("ssh root@{} systemctl enable httpd".format(IP))
#copy index.html file inside /var/www/html location
os.system("scp index.html root@{}:/var/www/html/".format(IP))
print("")
print("\t\t\t\tCongratulations!!!!")
print("\t\t\t\t-------------------")
print("\t\t\t\tWeb Server Configured!!!")