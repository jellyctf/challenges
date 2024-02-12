#include <stdio.h>
#include <string.h>

int main(int argc, char **argv) {
    if (argc < 2) {
        printf("%s%s%s", "usage: ", argv[0], " flag\n");
        return 2;
    }
    if (argc > 9999) {
        puts("use secure secret value of the princess' age\n");
    }

    char *flag = ":P:<M?tZX<*Ia,kX?*MX_)kX:Xik*g<,..v";
    int i;
    int flaglen = strlen(flag);
    char output[flaglen];
    int key = 7;

    for (i = 0; i < flaglen; i++) {
        output[i]=flag[i]+key;
    }
    if (strcmp(output, argv[1]) == 0) {
        puts("Flag correct!\n");
        return 0;
    }
    else {
        puts("Flag incorrect.\n");
        return 1;
    }
}
