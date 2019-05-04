# Nmap

The "default"

```bash
nmap -sC -sV -oA -p- <ip>
-sC All common scripts
-sV version scan
-oA output all formats
-p- scan all ports
```


Common Nmap Scan Types

```bash
-sT TCP Connect Scan
-sS TCP Syn Scan (aka Stealh Scan)
-sX Xmas scan
-sU Scan UDP
-sn enumerate hosts(no port scan) (tbc)
```

Extra Nmap Options

```bash
-p <port(s)> Define Port number(s). Scans 1-1000 only if not specified
-p- Scan all ports
-sV Version Scan, get information on services version
-O Gets/Guesses Operating System
-A Aggresive Scan, Gets both OS and Service Versions
```

more nmap

```bash
-sL list targets to scan
-pn disable port scan
```


nmap interactive(for privesc)

	nmap --interactive
	!bash -p


cool nmap scripts
	
	--script=http-enum
	--script=http-default-accounts
	--script=http-phpmyadmin-dir-traversal

Heartbleed Detection

	nmap -sV -p 443 --script=ssl-heartbleed 192.168.1.0/24

passing parameters into nmap script example

	nmap -p 3306 <ip> --script mysql-dump-hashes --script-args='username=root,password=secret'
	nmap -p 3306 100.65.136.252 --script=mysql-query --script-args='query="show tables FROM corporate_database",username=root,password=abc123'
	
	**dont forget username and pass

List of nmap scripts	
https://nmap.org/nsedoc/
