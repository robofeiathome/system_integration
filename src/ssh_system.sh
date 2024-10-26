#!/bin/bash

IP='10.42.0.193'
PASSWORD='123456'
PING="ping $IP"
while ! $PING | grep -q 'bytes from' ; do 
	echo "SSH not available, trying again."
	sleep 1
	$PING
done

echo "SSH available. Starting connection."

sshpass -p $PASSWORD ssh robofei@$IP
