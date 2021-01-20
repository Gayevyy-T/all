extremes(){
args=$#
l=( )
big=0
smal=$1
        for number in $@
        do
                l=(${l[*]} $number)
                #l+=($number)
        done

        for x in $(eval echo {0..$(($args-1))})
        do
                if [[ ${l[$x]} -ge $big ]]
                then
                        big=${l[$x]}

                elif [[ ${l[$x]} -le $smal ]]
                then
                        smal=${l[$x]}
                fi
        done
}

extremes $@
echo $smal
echo $big
