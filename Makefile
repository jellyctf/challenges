all: rev1 pwn1 pwn2 pwn3
rev1:
	gcc -Og -g -gdwarf-4 -fno-stack-protector -no-pie -z execstack -o bin/rev1 rev1.c

pwn1:
	gcc -o bin/pwn1 pwn1.c

pwn2:
	gcc -o bin/pwn2 pwn2.c

pwn3:
	gcc -O0 -Wno-deprecated-declarations -std=c99 -fno-stack-protector -o bin/pwn3 pwn3.c