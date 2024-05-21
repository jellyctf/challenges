#include <stdio.h>
#include <stdlib.h>

int main(int argc, char **argv) {
    int coin_balance = 100;
    int non_jelly_remainder_stock = 100;
    int con = 0;

    while (con == 0){
        printf("\nWelcome to the Phase Connect coffee shop v1.0\n");
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
            printf("\nCurrently on sale\n");
            printf("1. Kaneko Lumi Inspired - $35 each (%d in stock)\n", non_jelly_remainder_stock);
            printf("2. Jelly Hoshiumi Inspired (Limited Edition) - $1,000,000 each (1 in stock)\n");
            printf("Please make a selection: ");
	
            int choice;
	    fflush(stdin);
            scanf("%d", &choice);

            if (choice == 1)
            {
                printf("\nEnter desired quantity: ");

                int quantity = 0;
                fflush(stdin);
                scanf("%d", &quantity);
                printf("\n");

                if (quantity > non_jelly_remainder_stock)
                {
                    printf("Currently out of stock... please order a smaller quantity.");
                }
                else
                {
                    int total_cost = 35 * quantity;
                    printf("Current balance: %d\n", coin_balance);
                    printf("Total cost: %d\n", total_cost);

                    if (coin_balance < total_cost)
                    {
                        printf("Insufficient funds to purchase! Please try again!\n\n");
                    }
                    else
                    {
                        coin_balance = coin_balance - total_cost;
                        non_jelly_remainder_stock = non_jelly_remainder_stock - quantity;
                        printf("%d coffees purchased! Your coffee is being packaged and will be delivered in 2028!\n\n", quantity);
                        printf("Current balance: %d\n", coin_balance);
                    }
                }
            }
            else if (choice == 2)
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
