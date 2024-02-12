rev1:
	gcc -Og -g -gdwarf-4 -fno-stack-protector -no-pie -z execstack -o bin/rev1 rev1.c