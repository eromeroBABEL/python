import sys,paramiko

host_address="192.168.1.59"

if len(sys.argv)==2:
	password="oracle"
	command=sys.argv[1]
	try:
		client=paramiko.SSHClient()
		client.load_system_host_keys()
		client.connect(host_address,22,"root",password)
		client.set_missing_host_key_policy(paramiko.WarningPolicy)
		stdin,stdout,stderr= client.exec_command(command)
		print stdout.read()
	finally:
		client.close()
