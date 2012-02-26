#!/bin/sh

JAVACLASS="Problem$1"

if [ -f $1.java ] && [ ! -f $JAVACLASS.class ]; then
	javac $1.java
elif [ $1.java -nt $JAVACLASS.class ]; then
	javac $1.java
fi

if [ -f $1.c ] && [ ! -f $1.out ]; then
	gcc $1.c -o $1.out
elif [ $1.c -nt $1.out ]; then
	gcc $1.c -o $1.out
fi

if [ -f $1.java ]; then
	echo "\nJava:"
	time java $JAVACLASS
fi

echo "\nPython:"
time python $1.py

if [ -f $1.c ]; then
	echo "\nC:"
	time ./$1.out
fi

