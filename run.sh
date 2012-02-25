#!/bin/sh

JAVACLASS="Problem$1"

if [ ! -f $JAVACLASS.class ]
then
	javac $1.java
elif [ $1.java -nt $JAVACLASS.class ]
then
	javac $1.java
fi

if [ ! -f $1.out ]
then
	gcc $1.c -o $1.out
elif [ $1.c -nt $1.out ]
then
	gcc $1.c -o $1.out
fi

echo "\nJava:"
time java $JAVACLASS
echo "\nPython:"
time python $1.py
echo "\nC:"
time ./$1.out

