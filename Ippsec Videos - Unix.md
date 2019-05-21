# Ippsec Videos (Unix)

## Easy


| No   | Box       | Status  | User                                           | Priv Esc                                                     | Notes                                                        |
| ---- | --------- | ------- | ---------------------------------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| 1    | Irked     | Watched | UnrealIRCd Exploit, hidden files, steg         | SUID bit, creating the file "#!/bin/sh, /bin/bash"           | Steg, IRC, a bit of ghidra                                   |
| 2    | Curling   |         |                                                |                                                              | Done box but not yet watched.                                |
| 3    | Frolic    |         |                                                |                                                              |                                                              |
| 4    | Sunday    | Watched | password guessing                              | sudo file (wget -i), using sleep function as cron reverts file back every 5s. Also can use wget -O to replace the shadow file. (use wget to read) | Bit of shellshocked info.                                    |
| 5    | Valentine |         | sshkey in http enum                            | Resuming tmux                                                | Additional Dirtyc0w demo                                     |
| 6    | Nibbles   | Watched | Password Guessing, Malicious File Upload, RCE  | sudo -l, creating the file. "#!/bin/sh, bash"                | Nibbleblog exploit, port forwarding(SSH Proxy), compiling rationallove exploit "glibc -  'getwcd()'" |
| 7    | Bashed    | Watched | Dir Enum, webshell,  reverse shell, NOPWD sudo | cronjob file                                                 | Cherrytree demo                                              |
| 8    | Sense     |         |                                                |                                                              |                                                              |
| 9    | Shocker   |         |                                                |                                                              |                                                              |
| 10   | Mirai     |         |                                                |                                                              |                                                              |
| 11   | Blocky    |         |                                                |                                                              |                                                              |
| 12   | Bank      |         |                                                |                                                              |                                                              |
| 13   | Beep      |         |                                                |                                                              |                                                              |



## Medium

| No   | Box            | Status | User | Priv Esc | Notes |
| ---- | -------------- | ------ | ---- | -------- | ----- |
| 1    | Redcross       |        |      |          |       |
| 2    | Vault          |        |      |          |       |
| 3    | Carrier        |        |      |          |       |
| 4    | Waldo          |        |      |          |       |
| 5    | Hawk           |        |      |          |       |
| 6    | Tartarsauce    |        |      |          |       |
| 7    | DevIios        |        |      |          |       |
| 8    | Olympus        |        |      |          |       |
| 9    | Canape         |        |      |          |       |
| 10   | Poison         |        |      |          |       |
| 11   | Stratusphere   |        |      |          |       |
| 12   | Celestial      |        |      |          |       |
| 13 | Aragog         |        |      |          |       |
| 14 | Flux Capacitor |        |      |          |       |
| 15 | Inception      |        |      |          |       |
| 16 | Enterprise     |        |      |          |       |
| 17 | Node           |        |      |          |       |
| 18 | SolidState |        |      |          |       |
| 19 | Nineveh |        |      |          |       |
| 20 | Europa | Watched | user enum via SSL cert, enumerate host and directories. SQLi on admin login, php injection | cronjob runs a world writable .sh file. | Also a small demo on Sparta |
| 21 | Apocalyst |        |      |          |       |
| 22 | Sneaky |        |      |          |       |
| 23 | Lazy |        | 2nd order SQL, insufficient cookie entropy - padbuster padding attack | Making a fake "cat" and adding to $PATH |  |
| 24 | Haircut |        |      |          | Watch next |
| 25 | CronOS |        |      |          |       |
| 26 | Tenten |        |      |          |       |
| 27 | October |        |      |          |       |
| 28 | Popcorn |        |      |          |       |
|      |              |        |      |          |       |



## Hard

| No   | Box           | Status | User | Priv Esc | Notes |
| ---- | ------------- | ------ | ---- | -------- | ----- |
| 1    | Zipper        |        |      |          |       |
| 2    | Dab           |        |      |          |       |
| 3    | Oz            |        |      |          |       |
| 4    | Falafel       |        |      |          |       |
| 5    | CrimeStoppers |        |      |          |       |
| 6    | Kotarak       |        |      |          |       |
| 7    | Shrek         |        |      |          |       |
| 8    | Calamity      |        |      |          |       |
| 9    | Holiday       |        |      |          |       |
| 10   | Charon        |        |      |          |       |
| 11   | Joker         |        |      |          |       |



## Insane

| No   | Box           | Status | User | Priv Esc | Notes |
| ---- | ------------- | ------ | ---- | -------- | ----- |
| 1    | Reddish       |        |      |          |       |
| 2    | Mischief      |        |      |          |       |
| 3    | Nightmare     |        |      |          |       |
| 4    | Nightmare(v2) |        |      |          |       |
| 5    | Fulcrum       |        |      |          |       |
| 6    | Ariekei       |        |      |          |       |
| 7    | Jail          |        |      |          |       |
| 8    | Brainfuck     |        |      |          |       |

