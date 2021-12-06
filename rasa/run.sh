pid=$(lsof -n -i :5055 | grep LISTEN | awk '{print $2}')

if [ -z "$pid" ]
then
    kill -9 $pid
    echo "Kill proc"
fi
unset pid

rasa x --enable-api