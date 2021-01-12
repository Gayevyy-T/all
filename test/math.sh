#!/usr/bin/env bash


if [[ $1 =~ ^[A-Z] ]]
then
	echo "how proper"
else
	echo "NOT"
fi




#if [[ $(expr $1 % 2) -eq 0 ]]
#then
#	echo "even"
#else
#	echo "odd"
#fi
