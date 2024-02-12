all: rev1 pwn1 pwn2
rev1:
	gcc -Og -g -gdwarf-4 -fno-stack-protector -no-pie -z execstack -o bin/rev1 rev1.c

pwn1:
	gcc -o bin/pwn1 pwn1.c

pwn2:
	gcc -o bin/pwn2 pwn2.c