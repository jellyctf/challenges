#include <stdio.h>
#include <string.h>

int get_key() {
    return 7;
}

int main(int argc, char **argv) {
    if (argc < 2) {
        printf("%s%s%s", "usage: ", argv[0], " flag\n");
        return 2;
    }

    char *flag = "c^eer<M?tZX<*Ia,kX?*MX_)kX:Xik*g<,..v";
    int i;
    int flaglen = strlen(flag);
    char output[flaglen];
    int key = get_key();

    if (strcmp(argv[1], "hint") == 0) {
        puts("use secure secret value of the princess' age\n");
        return key;
    }

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
