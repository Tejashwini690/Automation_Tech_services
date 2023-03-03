import os
print("\t\t\t\tWelcome to hadoop cluster set up bot")
print("\t\t\t\t------------------------------------")
print(''' \t\t\t\tFor setting hadoop cluster you have to follow certain steps:
          \t\t\tStep:1 Give details about namenode.
          \t\t\tStep:2 Give details about datanode.
          \t\t\tStep:3 give details about client.
''')

print("\t\t\t\tSetting namenode")
print("\t\t\t\t----------------")
print()

Namenode_IP = input("\t\t\t\tGive IP at which you want to configure namenode:")
#install hadoop 
os.system("ssh root@{} yum install wget -y".format(Namenode_IP))
os.system("ssh root@{} wget http://35.244.242.82/yum/java/el7/x86_64/jdk-8u171-linux-x64.rpm".format(Namenode_IP))
os.system("ssh root@{} wget https://archive.apache.org/dist/hadoop/core/hadoop-1.2.1/hadoop-1.2.1-1.x86_64.rpm".format(Namenode_IP))
os.system("ssh root@{} rpm -ivh jdk-8u171-linux-x64.rpm".format(Namenode_IP))
os.system("ssh root@{} rpm -ivh hadoop-1.2.1-1.x86_64.rpm --force".format(Namenode_IP))
#copy namenode.py into instance
os.system("scp namenode.py root@{}:/root/".format(Namenode_IP))
#install python3 on the instance
os.system("ssh root@{} yum install python3 -y".format(Namenode_IP))
#setup namenode core-site.xml and hdfs-site.xml
os.system("ssh root@{} python3 namenode.py".format(Namenode_IP))
#format the namenode
os.system("ssh root@{} hadoop namenode -format".format(Namenode_IP))
#start namenode
os.system("ssh root@{} hadoop-daemon.sh start namenode".format(Namenode_IP))

print("\t\t\t\tSetup namenode Successfully")
print("\t\t\t\t----------------")
print()

print("\t\t\t\tSetting datanodes")
print("\t\t\t\t----------------")
print()

Datanode_IP = []
count_datanode = int(input("\t\t\t\tHow many datanode you want to configure: "))
for i in range(0,count_datanode):
	d_ip = input("\t\t\t\tGive IP at which you want to configure datanode{}:".format(i+1))
	Datanode_IP.append(d_ip)
	#install hadoop 
	os.system("ssh root@{} yum install wget -y".format(Datanode_IP[i]))
	os.system("ssh root@{} wget http://35.244.242.82/yum/java/el7/x86_64/jdk-8u171-linux-x64.rpm".format(Datanode_IP[i]))
	os.system("ssh root@{} wget https://archive.apache.org/dist/hadoop/core/hadoop-1.2.1/hadoop-1.2.1-1.x86_64.rpm".format(Datanode_IP[i]))
	os.system("ssh root@{} rpm -ivh jdk-8u171-linux-x64.rpm".format(Datanode_IP[i]))
	os.system("ssh root@{} rpm -ivh hadoop-1.2.1-1.x86_64.rpm --force".format(Datanode_IP[i]))
	#copy datanode.py into instance
	os.system("scp datanode.py root@{}:/root/".format(Datanode_IP[i]))
	os.system("ssh root@{} yum install python3 -y".format(Datanode_IP[i]))
	#setup datanode core-site.xml and hdfs-site.xml
	os.system("ssh root@{} python3 datanode.py".format(Datanode_IP[i]))
	#start datanode
	os.system("ssh root@{} hadoop-daemon.sh start datanode".format(Datanode_IP[i]))

print("\t\t\t\tSetup datanode Successfully")
print("\t\t\t\t----------------")
print()

print("\t\t\t\tSetting up the client")
print("\t\t\t\t----------------")
print()

Client_IP = []
count_client = int(input("\t\t\t\tHow many client you want to configure: "))
for i in range(0,count_client):
	c_ip = input("\t\t\t\tGive IP at which you want to configure client:")
	Client_IP.append(c_ip)
	#install hadoop 
	os.system("ssh root@{} yum install wget -y".format(Client_IP[i]))
	os.system("ssh root@{} wget http://35.244.242.82/yum/java/el7/x86_64/jdk-8u171-linux-x64.rpm".format(Client_IP[i]))
	os.system("ssh root@{} wget https://archive.apache.org/dist/hadoop/core/hadoop-1.2.1/hadoop-1.2.1-1.x86_64.rpm".format(Client_IP[i]))
	os.system("ssh root@{} rpm -ivh jdk-8u171-linux-x64.rpm".format(Client_IP[i]))
	os.system("ssh root@{} rpm -ivh hadoop-1.2.1-1.x86_64.rpm --force".format(Client_IP[i]))
	#copy client.py into instance
	os.system("scp client.py root@{}:/root/".format(Client_IP[i]))
	os.system("ssh root@{} yum install python3 -y".format(Client_IP[i]))
	#setup datanode core-site.xml and hdfs-site.xml
	os.system("ssh root@{} python3 client.py".format(Client_IP[i]))
	os.system("ssh root@{} hadoop dfsadmin -report".format(Client_IP[i]))

print("\t\t\t\tSetup client Successfully")
print("\t\t\t\t----------------")
print()
	
print("\t\t\t\tCongratulations!!!!")
print("\t\t\t\t-------------------")
print("\t\t\t\tHadoop Cluster Setup Successfully!!!")