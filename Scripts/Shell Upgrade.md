Spawn bash on reverse shell

	python -c 'import.pty;pty.spawn("/bin/bash")'

Background the reverse shell

	ctrl + Z

Back in Kali

Get terminal info, take note of TERM type and size of TTY(rows;columns)

	echo $TERM
	stty -a

Change stty settings to raw and echo input

	stty raw -echo

Foreground the reverse shell(Will reopen the nc)

	fg

Reinitialize the terminal

	reset

Match current window

	export SHELL=bash
	export TERM=x256-color (might be diff)
	stty rows 38 columns 116 (might be diff)



