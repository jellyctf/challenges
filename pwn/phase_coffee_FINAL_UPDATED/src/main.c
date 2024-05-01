#include <stdio.h>
#include <stdlib.h>

int main(int argc, char **argv) {
    int BUF_SIZE = 64;
    char address[BUF_SIZE];
    int coin_balance = 1000;
    int con = 0;

    while (con == 0){
        int menu;

        printf("\nWelcome to the Phase Connect coffee shop v2.0\n");
        printf("We sell coffee! \n");
        printf("Please buy our coffee... \n");
        printf("or else... \n");

        printf("1. Check Account Balance\n");
        printf("2. Purchase Coffee\n");
        printf("3. Exit\n");

        printf("Enter a menu selection \n");
        fflush(stdin);

        scanf("%d", &menu);

        if(menu == 1)
        {
            printf("\n\nCurrent account balance: %d \n\n", coin_balance);
        }
        else if (menu == 2)
        {
            printf("\n\nCurrently on sale\n");
            printf("1. Tenma Maemi Inspired - $35 each\n");
            printf("2. Amanogawa Shiina Inspired - $35 each\n");
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

                    if (total_cost < 0)
                    {
                        printf("Requested quantity too large!\n");
                    }
                    else
                    {
                        printf("Current balance: %d\n", coin_balance);
                        printf("Total cost: %d\n", total_cost);

                        if (coin_balance < total_cost)
                        {

                            printf("Insufficient funds to purchase! Please try again!\n\n");
                        }
                        else
                        {
                            int remaining_coin_balance = coin_balance - total_cost;

                            printf("Your order is being processed. Please enter your shipping address: ");
                            scanf("\n");
                            fgets(address, 1000, stdin);

                            printf("%d coffees purchased! Your coffee is being packaged and will be delivered in 2028!\n", quantity);
                            printf("Coffee will be delivered to %s\n", address);
                            printf("Current balance: %d\n", remaining_coin_balance);

                            coin_balance = remaining_coin_balance;
                        }
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
                        FILE *f = fopen("flag.txt", "r");
                        if(f == NULL){

                            printf("Flag not found: please run this on the server\n");
                            exit(0);
                        }
                        char buf[64];
                        fgets(buf, 63, f);
                        printf("YOUR FLAG IS: %s\n", buf);
                        break;
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