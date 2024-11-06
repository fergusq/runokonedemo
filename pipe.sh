#!/bin/bash

if [ ! -p /tmp/tulostin ]
then
	mkfifo /tmp/tulostin
fi

chmod a+rw /tmp/tulostin

#
while true
do
	cat /tmp/tulostin | iconv -t cp437 >/dev/usb/lp0
done
