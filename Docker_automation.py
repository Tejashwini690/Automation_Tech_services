#importing OS module
import os
import paramiko as ps
import sys
import getpass as gp
#Creating MENU
global ip,un,pw
ip=input("\n\t\t\t\tEnter the IP at which You want to Configure Docker : ")
un=input("\t\t\t\tEnter the UserName : ")
pw=gp.getpass("\t\t\t\tEnter the Password : ")
def docker_menu():
    print("\n\t\t\t\t    WELCOME TO THE DOCKER AUTOMATION MENU!!!\n")
    print("\t\t\t\t\tPlease Select From the Below Options\n")
    print("\t\t\t\t1.Install Docker(If not pre-installed)")
    print("\t\t\t\t2.Start Docker Service")
    print("\t\t\t\t3.View The All the Containers")
    print("\t\t\t\t4.Pull OS Image from Docker Hub")
    print("\t\t\t\t5.Launch A Docker Container")
    print("\t\t\t\t6.Run A command in Running Docker Container")
    print("\t\t\t\t7.Start the Existing Container")
    print("\t\t\t\t8.Check the Logs of docker container")
    print("\t\t\t\t9.Remove Docker Container")
    print("\t\t\t\t10.Stop Docker Service")
    print("\t\t\t\t11.Uninstall Docker(If installed)")
    print("\t\t\t\t12.Exit Automation Menu.")
    print("\t\t\t\t13.Exit to the Main Menu")
    IN=input("\n\t\t\t\tPlease Input the Option Number : ")
    if IN == "1":
        doc_inst()
    elif IN == "2":
        doc_launch()
    elif IN == "3":
        doc_ps()
    elif IN == "4":
        doc_pull()
    elif IN == "5":
        doc_run()
    elif IN == "6":
        doc_exec()
    elif IN == "7":
        doc_start()
    elif IN == "8":
        doc_logs()
    elif IN == "9":
        doc_rem()
    elif IN == "10":
        doc_stop()
    elif IN == "11":
        doc_unin()
    elif IN == "12":
        quit()
    elif IN == "13":    
        os.system("python automation.py")
    else :
        print("Please select Valid valid Number from given option\n")
        docker_menu()


def doc_inst():
    print("\n\t\t\t\tPlease wait while we install Docker for You!!!\n")
    sshclient=ps.SSHClient()
    sshclient.set_missing_host_key_policy(ps.AutoAddPolicy())
    sshclient.connect(hostname=ip,username=un,password=pw)
    stdin, stdout, stderr=sshclient.exec_command("cd /etc/yum.repos.d\ncat > docker.repo\n")
    stdin.write('''[Docker]
baseurl=https://download.docker.com/linux/centos/7/x86_64/stable/
gpgcheck=0''')
    stdin.flush()
    stdin, stdout, stderr=sshclient.exec_command("yum install -y docker-ce --nobest")
    err=stderr.readlines()
    print("\t\t\t\t".join(err))
    out=stdout.readlines()
    print("".join(out))
    print("\nDocker is Successfully Installed!!!\n")
    yn=input("\n\t\t\t\tDo you want to return to Docker Automation Menu?(y/n) :  ")
    if yn=="y":
        docker_menu()
    else:
        yon=input("\n\t\t\t\tDo you want to exit the Docker Automation?(y/n) :  ")
        if yon=="y":
            quit()
        else:
            docker_menu()

def doc_launch():
    sshclient=ps.SSHClient()
    sshclient.set_missing_host_key_policy(ps.AutoAddPolicy())
    sshclient.connect(hostname=ip,username=un,password=pw)
    stdin, stdout, stderr=sshclient.exec_command("systemctl enable docker")
    stdin, stdout, stderr=sshclient.exec_command("systemctl start docker")
    err=stderr.readlines()
    print("\t\t\t\t".join(err))
    out=stdout.readlines()
    print("".join(out)) 
    print("\n\t\t\t\tDocker service has been started!!!\n")
    yn=input("\n\t\t\t\tDo you want to return to Docker Automation Menu?(y/n) :  ")
    if yn=="y":
        docker_menu()
    else:
        yon=input("\n\t\t\t\tDo you want to exit the Docker Automation?(y/n) :  ")
        if yon=="y":
            quit()
        else:
            docker_menu()

def doc_ps():
    sshclient=ps.SSHClient()
    sshclient.set_missing_host_key_policy(ps.AutoAddPolicy())
    sshclient.connect(hostname=ip,username=un,password=pw)
    print("\t\t\t\tThese are the existing docker containers :\n")
    stdin, stdout, stderr=sshclient.exec_command("docker ps -a")
    err=stderr.readlines()
    print("\t\t\t\t".join(err))
    out=stdout.readlines()
    print("\t\t\t\t".join(out))
    yn=input("\n\t\t\t\tDo you want to return to Docker Automation Menu?(y/n) :  ")
    if yn=="y":
        docker_menu()
    else:
        yon=input("\n\t\t\t\tDo you want to exit the Docker Automation?(y/n) :  ")
        if yon=="y":
            quit()
        else:
            docker_menu()

def doc_pull():
    sshclient=ps.SSHClient()
    sshclient.set_missing_host_key_policy(ps.AutoAddPolicy())
    sshclient.connect(hostname=ip,username=un,password=pw)
    os=input("\t\t\t\tEnter the OS Image You want Pull : ")
    vr=input("\t\t\t\tEnter the version of OS : ")
    stdin, stdout, stderr=sshclient.exec_command(f"docker pull {os}:{vr}")
    err=stderr.readlines()
    print("\t\t\t\t".join(err))
    out=stdout.readlines()
    print("".join(out))
    yn=input("\n\t\t\t\tDo you want to return to Docker Automation Menu?(y/n) :  ")
    if yn=="y":
        docker_menu()
    else:
        yon=input("\n\t\t\t\tDo you want to exit the Docker Automation?(y/n) :  ")
        if yon=="y":
            quit()
        else:
            docker_menu()

def doc_run():
    sshclient=ps.SSHClient()
    sshclient.set_missing_host_key_policy(ps.AutoAddPolicy())
    sshclient.connect(hostname=ip,username=un,password=pw)
    os=input("\t\t\t\tEnter the OS you want to Launch : ")
    nm=input("\t\t\t\tEnter the Name You want to give to Your Container : ")
    stdin, stdout, stderr=sshclient.exec_command(f"docker run -dit --name {nm} {os}\n")
    err=stderr.readlines()
    print("\t\t\t\t".join(err))
    out=stdout.readlines()
    print("".join(out))
    print("\n\t\t\t\tYour Container has been Launched!!!")
    yn=input("\n\t\t\t\tDo you want to return to Docker Automation Menu?(y/n) :  ")
    if yn=="y":
        docker_menu()
    else:
        yon=input("\n\t\t\t\tDo you want to exit the Docker Automation?(y/n) :  ")
        if yon=="y":
            quit()
        else:
            docker_menu()

def doc_rem():
    sshclient=ps.SSHClient()
    sshclient.set_missing_host_key_policy(ps.AutoAddPolicy())
    sshclient.connect(hostname=ip,username=un,password=pw)
    rm=input("\n\t\t\t\tEner the container-id/container-name which you want to remove : ")
    stdin, stdout, stderr=sshclient.exec_command(f"docker rm -f {rm}")
    err=stderr.readlines()
    print("\t\t\t\t".join(err))
    out=stdout.readlines()
    print("".join(out)) 
    yn=input("\n\t\t\t\tDo you want to return to Docker Automation Menu?(y/n) :  ")
    if yn=="y":
        docker_menu()
    else:
        yon=input("\n\t\t\t\tDo you want to exit the Docker Automation?(y/n) :  ")
        if yon=="y":
            quit()
        else:
            docker_menu()

def doc_exec():
    sshclient=ps.SSHClient()
    sshclient.set_missing_host_key_policy(ps.AutoAddPolicy())
    sshclient.connect(hostname=ip,username=un,password=pw)
    atc=input("\t\t\t\tEnter the container-id/container-name in which you want to run command : ")
    cmd=input("\t\t\t\tEnter the Commnad you want to run : ")
    stdin, stdout, stderr=sshclient.exec_command(f"docker exec {atc} {cmd}")
    err=stderr.readlines()
    print("\t\t\t\t".join(err))
    out=stdout.readlines()
    print("".join(out))
    yn=input("\n\t\t\t\tDo you want to return to Docker Automation Menu?(y/n) :  ")
    if yn=="y":
        docker_menu()
    else:
        yon=input("\n\t\t\t\tDo you want to exit the Docker Automation?(y/n) :  ")
        if yon=="y":
            quit()
        else:
            docker_menu()

def doc_logs():
    sshclient=ps.SSHClient()
    sshclient.set_missing_host_key_policy(ps.AutoAddPolicy())
    sshclient.connect(hostname=ip,username=un,password=pw)
    lg=input("\t\t\t\tEnter the container-id/container-name to get its logs : ")
    stdin, stdout, stderr=sshclient.exec_command(f"docker logs {lg}")
    err=stderr.readlines()
    print("\t\t\t\t".join(err))
    out=stdout.readlines()
    print("".join(out))   
    yn=input("\n\t\t\t\tDo you want to Return to Docker Automation Menu?(y/n) : ")
    if yn=="y":
        docker_menu()
    else:
        yon=input("\n\t\t\t\tDo you want to exit the Docker Automation?(y/n) :  ")
        if yon=="y":
            quit()
        else:
            docker_menu()

def doc_stop():
    sshclient=ps.SSHClient()
    sshclient.set_missing_host_key_policy(ps.AutoAddPolicy())
    sshclient.connect(hostname=ip,username=un,password=pw)
    stdin, stdout, stderr=sshclient.exec_command("systemctl stop docker")
    err=stderr.readlines()
    print("\t\t\t\t".join(err))
    out=stdout.readlines()
    print("".join(out)) 
    print("\n\t\t\t\tDocker service has been stoped!!!\n")
    yn=input("\n\t\t\t\tDo you want to return to Docker Automation Menu?(y/n) :  ")
    if yn=="y":
        docker_menu()
    else:
        yon=input("\n\t\t\t\tDo you want to exit the Docker Automation?(y/n) :  ")
        if yon=="y":
            exit()
        else:
            docker_menu()

def doc_unin():
    print("\n\t\t\t\tPlease wait while we Uninstall Docker for You!!!\n")
    sshclient=ps.SSHClient()
    sshclient.set_missing_host_key_policy(ps.AutoAddPolicy())
    sshclient.connect(hostname=ip,username=un,password=pw)
    stdin, stdout, stderr=sshclient.exec_command("yum remove -y docker-ce")
    err=stderr.readlines()
    print("\t\t\t\t".join(err))
    out=stdout.readlines()
    print("".join(out))
    print("\n\t\t\t\tDocker Has Been Successfully Removed!!!\n")
    yn=input("\t\t\t\tDo you want to return to Docker Automation Menu?(y/n) :  ")
    if yn=="y":
        docker_menu()
    else:
        yon=input("\n\t\t\t\tDo you want to exit the Docker Automation?(y/n) :  ")
        if yon=="y":
            quit()
        else:
            docker_menu()

def doc_start():
    sshclient=ps.SSHClient()
    sshclient.set_missing_host_key_policy(ps.AutoAddPolicy())
    sshclient.connect(hostname=ip,username=un,password=pw)
    inp=input("\t\t\t\tEnter the Container-id\Container-name to be Started : ")
    stdin, stdout, stderr=sshclient.exec_command(f"docker start {inp}")
    err=stderr.readlines()
    print("\t\t\t\t".join(err))
    out=stdout.readlines()
    print("".join(out))
    print("\n\t\t\t\tContainer Has Been Successfully Started!!!\n")
    yn=input("\t\t\t\tDo you want to return to Docker Automation Menu?(y/n) :  ")
    if yn=="y":
        docker_menu()
    else:
        yon=input("\n\t\t\t\tDo you want to exit the Docker Automation?(y/n) :  ")
        if yon=="y":
            quit()
        else:
            docker_menu()

docker_menu()