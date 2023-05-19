#!/bin/sh

gen="ln -s gen /usr/bin" 
fcrypt="ln -s fcrypt /usr/bin/"
dcrypt="ln -s dcrypt /usr/bin"
des="fcrypt"
des2="dcrypt"
x="finshed"
for install in "$gen"; do
	
	if ! which "$install" &> /dev/null; then

		sudo sh -c "$install" && cd $des && sudo sh -c "$fcrypt" && cd .. && sudo sh -c "$dcrypt"
		echo "$x"
		exit
		


	else
		sudo sh -c "rm /usr/bin/gen"
		sudo sh -c "$install" && cd $des && sudo sh -c "$fcrypt" && cd .. && cd $des2 && sudo sh -c "$dcrypt"
		echo "$x"
		exit


	fi 

done


