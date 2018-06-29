a=`v4l2-ctl --list-devices |tr -s '\n\t' '_'`
OIFS="$IFS"
IFS='_'
read -a new_string <<< "${a}"
IFS="$OIFS"

for ((i=0; i<${#new_string[@]}; i++)); do
    echo ${new_string[$i]} | grep 'RGB' >> /dev/null;
    if [[ $? == 0 ]]; then
       echo ${new_string[$i+1]}
     fi
done
