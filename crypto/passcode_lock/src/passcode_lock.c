// de Bruijn brute force challenge
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int runChallenge(int passcodeLength)
{
    int EXTRA_ALLOWANCE = passcodeLength;
    int bitmask = (1 << passcodeLength) - 1;
    int maxTimeout = bitmask;
    int passCode = random() & bitmask;

    printf("Debug random passcode value: %u\n", passCode);
    printf("WARNING: System will timeout after %d entries\n", maxTimeout + EXTRA_ALLOWANCE);
    printf("Enter %d-digit binary passcode  \n", passcodeLength);

    int timeout = 0;
    int userInput = 0;

    char received;

    while (timeout < maxTimeout + EXTRA_ALLOWANCE)
    {
        scanf(" %c", &received);
        printf("Received: %c\n", received);
        printf("Received equality: %d\n", received != '0');
        printf("Debug %u\n", userInput);

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

    int phase;
    int result1 = 0;

    for (phase = 1; phase <= NUM_PHASES; phase++)
    {
        printf("\n\nStarting Phase %d...\n", phase);
        result1 = runChallenge(PASSCODE_LENGTH);

        // flush stdin
        int c;
        while((c = getchar()) != '\n' && c != EOF);

        printf("Phase %d validation result: %d\n", phase, result1);

        if (result1 == 0)
        {
            break;
        }
    }

    if (phase == NUM_PHASES + 1)
    {
        printf("Win! Flag is: ____\n");
    }

    return 0;
}