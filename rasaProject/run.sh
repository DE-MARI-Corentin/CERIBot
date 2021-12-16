source /usr/local/stow/rasax/bin/activate

pid=$(lsof -n -i :5055 | grep LISTEN | awk '{print $2}')

if [ -z "$pid" ]
then
    kill -9 $pid
    echo "Kill proc $pid"
fi
unset pid

#rm models/*

#rasa train
rasa run actions &
rasa x --enable-api
