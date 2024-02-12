all: rev1 binary1 binary2
rev1:
	gcc -Og -g -gdwarf-4 -fno-stack-protector -no-pie -z execstack -o bin/rev1 rev1.c

binary1:
	gcc -o bin/binary1 binary1.c

binary2:
	gcc -o bin/binary2 binary2.c