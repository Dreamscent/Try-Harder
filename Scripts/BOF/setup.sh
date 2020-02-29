#!/bin/bash

if [ $# -eq 2 ];
  then
	sed -i 's/targetip/'$1'/g' *.py
	sed -i 's/targetport/'$2'/g' *.py
	echo "Scripts configured to connect to vulnerable server:" $1 "on port" $2

  else
	echo "Usage: ./setup.sh <targetip> <targetport>" 
fi
