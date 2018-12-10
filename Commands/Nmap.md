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
