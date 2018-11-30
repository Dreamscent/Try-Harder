Find all files with SUID bit

find / -perm -u=s -type f 2>/dev/null
or
find / -perm -4000 -type f 2>/dev/null

    /denotes  start from the top (root) of the file system and find every directory
    -permdenotes search for the permissions that follow
    -u=sdenotes look for files that are owned by the root user
    -typestates the type of file we are looking for
    f denotes a regular file not the directories or special files
    2 denotes to the second file descriptor of the process, i.e. stderr (standard error)
    > means redirection
    /dev/null is a special filesystem object that throws away everything written into it.
