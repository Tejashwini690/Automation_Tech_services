import os

def aws_instance():
	print('\t\t\tCreating a Key Pair...')

	key_name = input('\t\t\tEnter your key pair name that you want to give = ') 
	os.system("aws ec2 create-key-pair --key-name={}".format(key_name))

	print('\n\t\t\t**Please copy this KeyPairID for future use**')
	

	print('\n\t\t\tCreating a Sec Group...')
	sec_name = input('\t\t\tEnter your security group name that you want to give = ') 
	os.system('aws ec2 create-security-group --description {} --group-name {}'.format(key_name, sec_name))
	print('\n\t\t\t**Please copy this GroupID  for future use**\n')
	

	auth = input('\n\t\t\tTo provide autorized security enter your GroupID here : ')
	os.system('aws ec2 authorize-security-group-ingress --group-id {} --protocol tcp --port 22 --cidr 0.0.0.0/0'.format(auth))

	print('\n\t\t\tCreaing an Instance On AWS Cloud...')
	img_id = input('\t\t\tPlease provide us image ID which OS you want to launch : ')
	instance_type = input('\t\t\tPlease provide which type of OS you want to launch :')
	os.system('aws ec2 run-instances --image-id {} --instance-type {} --security-group-ids {} --key-name {}'.format(img_id, instance_type, auth, key_name))
	print('\n\t\t\tYour Instance is created you can verify it from console.aws.amazon.com/ec2/')

def start_instance():
    start_id = input('Enter Instance ID that you want to start : ')
    os.system('aws ec2 start-instances --instance-ids {}'.format(start_id))
    print('Your Instance start successfully.')

def stop_instance():
    stop_id = input('Enter Instance ID that you want to stop : ')
    os.system('aws ec2 stop-instances --instance-ids {}'.format(stop_id))
    print('Your Instance stop successfully.')
    
def cloudfront_service():
	print("\t\t\t\tFor giving origin in cloud front we have to use S3 bucket ....")
	choice_bucket = input("\t\t\t\tDo you want to create bucket or want to use existing bucket..(type-create bucket/existing bucket)?")
	if(("create bucket" in choice_bucket)):
		bucket_name = input("\t\t\t\tEnter bucket name which you want to use for cloud front service:")
		region_name = input("\t\t\t\tEnter region name :")
		os.system("aws s3 mb s3://{} --region {}".format(bucket_name,region_name))
		print("\t\t\t\tbucket created....")
		print()
		print("\t\t\t\tUpload obect inside bucket...")
		object_name = input("\t\t\t\tEnter object which you want to upload:")
		print("Which type of permission you want to give to object..")
		print("\t\t\t\t(private)(public-read)(public-read-write)(authenticated-read)(aws-exec-read)(bucket-owner-read)(bucket-owner-full-control)(log-delivery-write)")
		object_permission = input("\t\t\t\tEnter permission for object:")
		os.system("aws s3 cp {} s3://{} --acl {}".format(object_name,bucket_name,object_permission))
		print()
		print("\t\t\t\tObject is uploaded successfully...")
		print("\t\t\t\tCreating cloud front distribution...")
		os.system("aws cloudfront create-distribution --origin-domain-name {}.s3.amazonaws.com --default-root-object {}".format(bucket_name,object_name))
	if(("existing bucket" in choice_bucket)):
		bucket_name=input("\t\t\t\tEnter S3 bucket name:")
		object_name=input("\t\t\t\tEnter object name:")
		os.system("aws cloudfront create-distribution --origin-domain-name {}.s3.amazonaws.com --default-root-object {}".format(bucket_name,object_name))
        
def s3_service():
	bucket_name = input("\t\t\t\tEnter bucket name:")
	region_name = input("\t\t\t\tEnter region name :")
	os.system("aws s3 mb s3://{} --region {}".format(bucket_name,region_name))
	print("\t\t\t\tbucket created....")
	print()
	choice_upload = input("\t\t\t\tDo you want to upload obect inside bucket(Yes/No)...")
	if(("Yes" in choice_upload) or ("YES" in choice_upload) or ("yes" in choice_upload)):
		object_name = input("\t\t\t\tEnter object-path which you want to upload:")
		print("Which type of permission you want to give to object..")
		print("\t\t\t\t(private)(public-read)(public-read-write)(authenticated-read)(aws-exec-read)(bucket-owner-read)(bucket-owner-full-control)(log-delivery-write)")
		object_permission = input("\t\t\t\tEnter permission for object:")
		os.system("aws s3 cp {} s3://{} --acl {}".format(object_name,bucket_name,object_permission))
		print()
		print("\t\t\t\tObject is uploaded successfully...")
	else:
		print("okay")
#creating volume 

def EBS_volume():
    def create_volume():
        print("To create volume ----------")
        volume_type=input("enter volume type :")
        volume_size=input("enter volume size :")
        avail_zone=input("enter EBS availability zone : ")
        print("\t\t\t\t--------------creating volume-------------------\n")
        os.system("aws ec2 create-volume --volume-type {}  --size {} --availability-zone {}".format(volume_type,volume_size,avail_zone)) 

    #Attach volume
    def Attach_volume():
        print("To Attach volume ----------")
        instance_id=input("enter instance id to attach volume:")
        vol_id= input("enter volume id to attach :")
        device=input("enter device to attach as :") #ex:/dev/xvdf 
        print("\t\t\t\t--------------Attaching volume-------------------\n")
        os.system("aws ec2  attach-volume  --instance-id {}  --volume-id {} --device {} ".format(instance_id,vol_id,device))

    #detach volume
    def detach_volume():
        print("To detach volume ----------")
        instance_id=input("enter instance id to detach volume:")
        vol_id= input("enter volume id to detach  :")
        device=input("enter device to detach as :") #ex:/dev/xvdf 
        print("\t\t\t\t--------------detaching  volume-------------------\n")
        os.system("aws ec2  detach-volume --instance-id  {}  --volume-id {}    --device {}".format(instance_id,vol_id,device))

    #modify volume
    def modify_volume():
        print("To modify  volume ----------")
        volume_id=input("enter volume id to modify :")
        size=input("enter volume size to modify :")
        print("\t\t\t\t--------------Modifying  volume-------------------\n")
        os.system("aws ec2 modify-volume --volume-id {} --size {} ".format(volume_id,size))
        
    #Automation code
    print("\t\t\t\t------------------EBS Automation--------------------\n")

    while(1):
        print("\t\t\t\t 1.Create volume \n \t\t\t\t 2.Attach volume \n \t\t\t\t 3.Modify volume \n \t\t\t\t 4.Detach volume \n \t\t\t\t 5.exit \n")
        choice=int(input("choose your Requirement :"))
        if(choice==1):
            create_volume()
        if(choice==2):
            Attach_volume()
        if(choice==3):
            modify_volume()
        if(choice==4):
            detach_volume()
        if(choice==5):
            break
            
def IAM_user():
    #creating User
    def create_user():
        print("\t\t\t\t-------------To create user--------------\n")
        name=input("enter user_name to create IAM User :")
        os.system("aws iam create-user --user-name {} ".format(name))

    #creating group
    def create_group():
        print("\t\t\t\t-------------To create group--------------\n")
        group_name=input("enter group name to create IAM group :")
        os.system("aws iam create-group  --group-name {} ".format(group_name))
        
        
    #get specific group details
    def get_group():
        group_name=input("enter group name to get details :")
        os.system("aws iam get-group --group-name {}".format(group_name))


    #add user to group
    def  user_add_group():
        print("\t\t\t\t-------------To add user in group--------------\n")
        user_name=input("enter the user name to add in group :")
        group_name=input("enter the group name :")
        os.system(" aws iam add-user-to-group --user-name {} --group-name  {} ".format(user_name,group_name))
        
    #To add group-policy
    def group_policy():
        print("\t\t\t\t-------------To add group policy--------------\n")
        group_name=input("enter group name to add policy :")
        policy=input("enter policy name to add : ")
        os.system("aws iam attach-group-policy --policy-arn arn:aws:iam::aws:policy/{}  --group-name {}".format(policy,group_name))

    #to check the details of group
    def group_details():
        print("\t\t\t\t-------------To check group--------------\n")
        group_name=input("enter the group name for details : ")
        os.system("aws iam get-group --group-name {} ".format(group_name))


    #create access key of user
    def create_access_key():
        print("\t\t\t\t-------------To create access key--------------\n")
        user=input("enter  user_name to create access key :")
        os.system("aws iam create-access-key --user-name {} ".format(user))

    #list-users
    def list_users():
        os.system("aws iam list-users")
        
    #list-groups
    def list_groups():
        os.system("aws iam list-groups")

    #delete user
    def delete_user():
        print("\t\t\t\t-------------To delete user--------------\n")
        user_name=input("enter user name to delete :")
        os.system("aws iam delete-user --user-name {} ".format(user_name))
        
    #delete group
    def delete_group():
        group_name=input("enter group name to delete :")
        os.system("aws iam delete-group --group-name {}".format(group_name))
        
    #remove user from group
    def del_group_user():
        print("\t\t\t\t-------------To remove user from group-------------\n")
        user_name=input("enter user to delete from group :")
        group_name=input("enter group to delete that user")
        os.system("aws iam remove-user-from-group --user-name {} --group-name {} ".format(user_name,group_name))

    #delete access key of user
    def delete_access_key():
        print("\t\t\t\t-------------To delete user-access key--------------\n")
        user=input("enter  user_name to delete access key :")
        access_key=input("enter access-key-id  to delete : ")
        os.system("aws iam delete-access-key --user-name {} --access-key-id {}  ".format(user,access_key))


    #Automation code 

    while(1):
        print("\t\t\t\t ------------------IAM-----------------\n")
        print("\t\t\t\t 1.create-user \n \t\t\t\t 2.create-group \n \t\t\t\t 3.get-group details \n \t\t\t\t 4.add-user-to-group \n \t\t\t\t 5.add-group-policy \n \t\t\t\t 6.group-details \n \t\t\t\t 7.create access key \n \t\t\t\t 8.list-users \n \t\t\t\t 9.list-grops \n  \t\t\t\t 10.delete-user \n \t\t\t\t 11.delete group \n \t\t\t\t 12.remove-user from group \n \t\t\t\t 13.delete user access key\n \t\t\t\t 14.exit \n")	
        choice=int(input("enter your requirement : "))
        if(choice==1):
            create_user()
        if(choice==2):
            create_group()
        if(choice==3):
            get_group()
        if(choice==4):
             user_add_group()
        if(choice==5):
            group_policy()
        if(choice==6):
            group_details()
        if(choice==7):
            create_access_key()
        if(choice==8):
            list_users()
        if(choice==9): 
            list_groups()
        if(choice==10):
            delete_user()
        if(choice==11):
            delete_group()
        if(choice==12):
            del_group_user()
        if(choice==13):
            delete_access_key()
        if(choice==14):
            break

print("\t\t\t\tFirst ,Configure AWS to enter into AWS\n")
os.system("aws configure")
while(1):
	print('''\t\t\tChoose your requirement.
			 \t\t\t\t1: Create Aws instance.
			 \t\t\t\t2: Start AWS Instance.
			 \t\t\t\t3: Stop AWS Instance.
			 \t\t\t\t4: Create a S3 bucket.
			 \t\t\t\t5: Create a cloudFront service.
			 \t\t\t\t6: EBS Volume
			 \t\t\t\t7: IAM User
			 \t\t\t\t8: exit
		''')
	option = input("\t\t\t: select from menu :")
	option = int(option)

	if(option==1):
		aws_instance()
	elif(option == 2):
		start_instance()
	elif(option == 3):
		stop_instance()
	elif(option==4):
		s3_service()
	elif(option==5):
		cloudfront_service()
	elif(option==6):
		EBS_volume()
	elif(option==7):
		IAM_user()  
	elif(option==8):
		exit() 	
	else:
		print("\n\t\t\tinvalid option!!!")
print("\t\t\t\t________________________________________________________________________________________________________________________\n")

