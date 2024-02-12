#include <stdio.h>

int main(int argc, char **argv) {
    int coin_balance = 100;
    int con = 0;

    while (con == 0){
        printf("\nWelcome to the Phase Connect coffee shop\n");
        printf("We sell coffee! \n");
        printf("Please buy our coffee... \n");
        printf("or else... \n");

        printf("1. Check Account Balance\n");
        printf("2. Purchase Coffee\n");
        printf("3. Exit\n");

        printf("Enter a menu selection \n");
        fflush(stdin);

        int menu;
        scanf("%d", &menu);

        if(menu == 1)
        {
            printf("\n\nCurrent account balance: %d \n\n", coin_balance);
        }
        else if (menu == 2)
        {
            printf("\n\nCurrently on sale\n");
            printf("1. Kaneko Lumi Inspired - $35 each\n");
            printf("2. Rie Himemiya Inspired - $35 each\n");
            printf("3. Jelly Hoshiumi Inspired (Limited Edition) - $1,000,000 each\n");
            printf("Please make a selection: ");

            int choice;
            fflush(stdin);
            scanf("%d", &choice);

            if (choice == 1 | choice == 2)
            {
                printf("\nEnter desired quantity: ");

                int quantity = 0;
                fflush(stdin);
                scanf("%d", &quantity);
                printf("\n");

                if (quantity > 0)
                {
                    int total_cost = 35 * quantity;
                    printf("Total cost: %d\n", total_cost);

                    coin_balance = coin_balance - total_cost;

                    if (coin_balance < 0)
                    {
                        printf("Insufficient funds to purchase! Please try again!\n\n");
                    }
                    else
                    {
                        printf("%d coffees purchased! Your coffee is being packaged and will be delivered in 2028!\n\n", quantity);
                        printf("Current balance: %d\n", coin_balance);
                    }
                }
                else
                {
                    printf("Invalid coffee quantity\n");
                }
            }
            else if (choice == 3)
            {
                printf("You have chosen the deluxe, premium, limited edition seiso idol princess Jelly Hoshiumi inspired coffee.\n");
                printf("This coffee costs $1,000,000. Press 1 to confirm purchase: ");

                int bid = 0;
                fflush(stdin);
                scanf("%d", &bid);

                if (bid == 1)
                {
                    if (coin_balance >= 1000000)
                    {
                        char *FLAG = "jellyCTF{PH4SE_C0NN3CT_IS_A_COFF33_C0MP4NY_9518}\n";
                        printf("%s", FLAG);
                    }
                    else
                    {
                        printf("Insufficient funds to purchase! Please try again!\n\n");
                    }
                }
            }
        }
        else
        {
            con = 1;
        }
    }
    return 0;
}