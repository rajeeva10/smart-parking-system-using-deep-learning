#!/bin/sh

Text_To_Display()
{
echo "###############################################################################"
echo " 										   "
echo "			Choose the option for the necessary Translation"
echo " 										   "
echo "			1. Object-Detection(OD)"
echo " 										   "
echo "			2. Image-to-Speech using Camera (ITSC)"
echo " 									           "
echo "#############################################################################"
}
while :
do
 Text_To_Display
 #echo "Choose option to enter : "
 read INPUT_STRING
 case $INPUT_STRING in 
	1)
		echo "You are executing the Object-Detetion (OD)"
		python C:/Users/lenovo/Desktop/VIRTUAL_EYE/Object_detection.py
		;;
	2)
	 	echo "You are executing the Image-to-Speech using Camera (ITSC)"
		python C:/Users/lenovo/Desktop/VIRTUAL_EYE/test.py
		;;
	q)
	 	echo "Programm is terminated"
		;;
 esac
done 
echo "complete"
