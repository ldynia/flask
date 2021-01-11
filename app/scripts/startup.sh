#!/bin/ash

echo "Install requirements.txt"
pip install -r /app/requirements.txt --no-cache-dir

# is $@ empty 
if [ -z "$@" ]
then
    echo "Run App"
    flask run --host=$HOST --port=$PORT
else
    echo "Executeing \$@ command: $@"
    exec $@
fi