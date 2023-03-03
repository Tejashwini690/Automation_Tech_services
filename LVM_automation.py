import os

def lvm_partition():
	IP = input("\t\t\t\tEnter IP at which you want to create partition:")
	print("\t\t\t\t----------------------------------------------------")
	print("\t\t\t\tFrom this choose disk for create physical volume")
	print("\t\t\t\t------------------------------------------------")
	os.system("ssh root@{} fdisk -l".format(IP))
	print("\t\t\t\t------------------------------------------------")
	count_pv = input("\t\t\t\tHow many disk you want to choose for create physical volume: ")
	count_pv = int(count_pv)
	pv=[]
	for i in range(0,count_pv):
		pvname = input("\t\t\t\tEnter disk{} name:".format(i+1))
		pv.append(pvname)

		print("\t\t\t\tcreating pythsical volumes..")
		print("\t\t\t\t----------------------------")
		os.system("ssh root@{} pvcreate {}".format(IP,pv[i]))
	
		print("\t\t\t\tdisplaying physical volumes..") 
		print("\t\t\t\t----------------------------")
		os.system("ssh root@{} pvdisplay {}".format(IP,pv[i]))
	

	vg_name = input("\t\t\t\tWhat volume group name you want to give:")
	vg_disk = ""
	for i in pv:
		vg_disk = vg_disk + " " + i

	print("\t\t\t\tcreating volume group..")
	os.system("ssh root@{} vgcreate {} {}".format(IP,vg_name,vg_disk))

	print("\t\t\t\tdisplaying volume froup..")
	print("\t\t\t\t-------------------------")
	os.system("ssh root@{} vgdisplay {}".format(IP,vg_name))

	print("\t\t\t\tdisplaying physical volumes..")
	print("\t\t\t\t---------------------------")
	for i in pv:
		os.system("ssh root@{} pvdisplay {}".format(IP,i))

	partition_size = input("\t\t\t\tEnter the partition size you want to create:") 
	lv_name = input("\t\t\t\twhat name you want to give to logical volume :")

	print("\t\t\t\tcreating logical volume..")
	os.system("ssh root@{} lvcreate --size {} --name {} {}".format(IP,partition_size,lv_name,vg_name))

	print("\t\t\t\tdisplaying logical volume..")
	print("\t\t\t\t---------------------------")
	os.system("ssh root@{} lvdisplay /dev/{}/{}".format(IP,vg_name,lv_name))

	print("\t\t\t\tformat the partition..")
	os.system("ssh root@{} mkfs.ext4 /dev/{}/{}".format(IP,vg_name,lv_name))

	print("\t\t\t\tmounting partition into folder..")
	mount_folder = input("\t\t\t\tEnter mount folder name:")

	print("\t\t\t\tmaking folder..")
	os.system("ssh root@{} mkdir {}".format(IP,mount_folder))

	print("\t\t\t\tmount the partition..")
	os.system("ssh root@{} mount /dev/{}/{} {}".format(IP,vg_name,lv_name,mount_folder))

	print("\t\t\t\tshowing status of mounting..")
	os.system("ssh root@{} df -h".format(IP))

	print("\t\t\t\t----------------------")
	print("\t\t\t\tCongratulations!!!!!!!")
	print("\t\t\t\tLogical volume created")

def extend_partition():
	IP = input("\t\t\t\tEnter IP at which you want to extend partition:")

	lv_extend_name = input("\t\t\t\tEnter logical volume name which you want to extend the size:")

	extend_size = input("\t\t\t\tHow many size you want to extend:")

	print("\t\t\t\textending the size of logical volume..")
	os.system("ssh root@{} lvextend --size +{} {}".format(IP,extend_size,lv_extend_name))

	print("\t\t\t\tsee the status but not extended in mounted folder because new part not formatted yet..")
	print("\t\t\t\t------------------------")
	os.system("ssh root@{} df -h".format(IP))

	print("\t\t\t\tfor format new extended space..")
	os.system("ssh root@{} resize2fs {}".format(IP,lv_extend_name))
	
	print("\t\t\t\tnow mounted folder size also increased..")
	print("\t\t\t\t------------------------")
	os.system("ssh root@{} df -h".format(IP))
	
	print("\t\t\t\t----------------------")
	print("\t\t\t\tCongratulations!!!!!!!")
	print("\t\t\t\tLogical volume extended")
	print("\t\t\t\t----------------------")
	print()

def lvm_main():
	while(True):
		print('''\t\t\t\tChoose one of the option.
	     \t\t\tOption1: Create logical volume.
	     \t\t\tOption2: Extend partition size.
	     \t\t\tOption3: Exit.
	    ''')
		option = input("\t\t\t\tEnter the option which you want to choose:")
		option = int(option)

		if(option==1):
			lvm_partition()

		elif(option==2):
			extend_partition()

		elif(option==3):
			break
		else:
			print("\n\t\t\t\tinvalid option!!!")


'''def reduce_partition():
	lv_reduce_name = input("\t\t\tEnter logical volume name which you want to reduce the size:")
	reduce_size = input("\t\t\tHow many size you want to reduce")
	mounted_folder = input("\t\t\tEnter folder where partition is mounted:")
	os.system("ssh root@{} umount {}/".format(IP,mounted_folder))
'''

print("\t\t\t\tWelcome To Logical Volume Managment Automation bot")
print("\t\t\t\t--------------------------------------------------")
lvm_main()