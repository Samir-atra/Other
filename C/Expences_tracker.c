#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<time.h>
#include<unistd.h>

int budget;
int withdraw;
int amount_left;
char withdrawal_purpose[10];
char sources[10];
char date[10];
char timee[8];
int result;
const char *filename = "/home/samer/Desktop/month.csv";
time_t t;

int main(void)
{
    FILE * fi;
    time(&t);


    if (access (filename, F_OK) == -1)
    {
        printf("The budget for the month: ");
        scanf("%i", &budget);

        withdraw = 0;
        amount_left = budget;

        printf("The sources of the budget: ");
        scanf("%s", sources);

        //printf("%s", ctime(&t));
        strftime(date, 20, "%Y-%m-%d", localtime(&t));
        strftime(timee, 20, "%H:%M:%S", localtime(&t));
        //date = ctime(&t);

        fi = fopen("month.csv", "a+");
        fprintf(fi, "Budget, Withdraw, Amount_left, Withdrawal_purpose, Date, Time\n");
        fprintf(fi, "%i, %i, %i, sources of the budget: %s, %s, %s\n", budget, withdraw, amount_left, sources, date, timee);
        fclose(fi);
    }
    else
    {

        fi = fopen("month.csv", "r");
        int num_tokens = 0;
        char myString[100];
        char *token;
        char *beedoo = NULL;
        char token_list[100][100]; 

        while(!feof(fi))
        {
            fgets(myString, 100, fi);
        }

        token = strtok_r(myString, ",", &beedoo);

        while(token != NULL)
        {
            strcpy(token_list[num_tokens], token); 
            num_tokens++;
            token = strtok_r(NULL, " ", &beedoo);
        }
        
        fclose(fi);
        token_list[2][strlen(token_list[2])-1] = '\0';
        int tokenn;

        sscanf(token_list[2], "%i", &tokenn);
        budget = tokenn;

        printf("The amount to be withrrawn: ");
        scanf("%i", &withdraw);

        amount_left = budget - withdraw;

        printf("The withdrawal purpose: ");
        scanf("%s", withdrawal_purpose);

        strftime(date, 20, "%Y-%m-%d", localtime(&t));
        strftime(timee, 20, "%H:%M:%S", localtime(&t));

        fi = fopen("month.csv", "a+");
        fprintf(fi, "%i, %i, %i, %s, %s, %s\n", budget, withdraw, amount_left, withdrawal_purpose, date, timee);
        fclose(fi);
    }

}
