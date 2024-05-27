#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int runChallenge(int passcodeLength)
{
    int EXTRA_ALLOWANCE = passcodeLength;
    int bitmask = (1 << passcodeLength) - 1;
    int maxTimeout = bitmask;
    int passCode = random() & bitmask;

    printf("WARNING: System will timeout after %d entries\n", maxTimeout + EXTRA_ALLOWANCE);
    printf("Enter %d-digit binary passcode  \n", passcodeLength);

    int timeout = 0;
    int userInput = 0;

    char received;

    while (timeout < maxTimeout + EXTRA_ALLOWANCE)
    {
        scanf(" %c", &received);

        // optimisation with bit shift
        userInput = bitmask & (userInput << 1 | (received != '0'));
        if (userInput == passCode)
        {
            return 1;
        }

        if (timeout % passcodeLength == 4)
        {
            printf("Passcode incorrect. Try again!\n");
        }

        timeout++;
    }

    printf("Timeout exceeded\n");

    return 0;
}

int main(int argc, char **argv) {
    srand(time(NULL));

    int PASSCODE_LENGTH = 5;
    int NUM_PHASES = 10;

    int phase_number;
    int result = 0;

    for (phase_number = 1; phase_number <= NUM_PHASES; phase_number++)
    {
        printf("\n\nStarting phase_number %d...\n", phase_number);
        result = runChallenge(PASSCODE_LENGTH);

        // flush stdin
        int c;
        while((c = getchar()) != '\n' && c != EOF);

        printf("Phase number %d - validation result: %d\n", phase_number, result);

        if (result == 0)
        {
            break;
        }
    }

    if (phase_number == NUM_PHASES + 1)
    {
        FILE *f = fopen("flag.txt", "r");
        if(f == NULL){

            printf("Flag not found: please run this on the server\n");
            exit(0);
        }
        char buf[64];
        fgets(buf, 63, f);
        printf("Validation successful. Unlocking vault: %s\n", buf);
    }

    return 0;
}