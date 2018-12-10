# Nmap


Common Nmap Scan Types

	-sT TCP Connect Scan
	-sS TCP Syn Scan (aka Stealh Scan)
	-sX Xmas scan
	-sV Version Scan, get information on services version
	-sN ???
	
Extra Nmap Options

	-p <port(s)> Define Port number(s). Scans 1-1000 only if not specified
	-p- Scan app ports
	-A Aggresive Scan (Gets a lot of stuff)
	-O Gets/Guesses Operating System
	
more nmap

	-sL : list targets to scan
	-pn : disable port scan


nmap interactive(for privesc)

	nmap --interactive
	!bash -p
	

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
