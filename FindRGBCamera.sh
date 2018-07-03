a=`v4l2-ctl --list-devices |tr -s '\n\t' '_'`
OIFS="$IFS"
IFS='_'
read -a new_string <<< "${a}"
IFS="$OIFS"

for ((i=0; i<${#new_string[@]}; i++)); do
    echo ${new_string[$i]} | grep 'RGB' >> /dev/null;
    if [[ $? == 0 ]]; then
       camera=${new_string[$i+1]}
       echo ${camera}
     fi
done

function record()
{
    video_name=`date +"%Y_%m_%d_%H:%M:%S"`
    echo ${video_name}
    if [ $(ls -l | grep "/*.mp4" | wc -l) -gt 59 ]
     then
         echo "file > 59"
         rm -r $(ls -rt | grep "/*.mp4" | head -n1)
     fi

    do=`ffmpeg -t 300 -s 640x480 -i ${camera} -vf hflip -b:v 700K ${video_name}.mp4`
}


while true; do
    record
done
