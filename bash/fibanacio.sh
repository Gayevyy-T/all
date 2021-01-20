#!/usr/bin/env bash

function fib {
	l=( )
	for x in $(eval echo {0..$(($1-1))})
	do
		if [[ $x -eq 0 ]]
		then
			echo $x
			l=(${l[*]} $x)
		elif [[ $x -eq 1 ]]
		then
			echo $x
			l+=($x)
		else
			a=$(expr $x - 1)     
			b=$(expr $x - 2)

			let c=${l[$a]}+${l[$b]}
			l+=($c)
			echo ${l[$x]}
		fi
	done
}
fib $1


















