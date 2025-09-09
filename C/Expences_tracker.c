#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>
#include <unistd.h>

// Global variables
int budget;
int withdraw;
int amount_left;
char withdrawal_purpose[50];
char sources[50];
char date[20];
char timee[20];
const char *filename = "month.csv"; // CSV file to store expenses
time_t t;

int main(void) {
    FILE *fi; // File pointer
    time(&t); // Get current time

    // Check if the CSV file exists
    if (access(filename, F_OK) == -1) {
        // --- First-time setup: Create the file and record the initial budget ---

        printf("The budget for the month: ");
        scanf("%i", &budget);

        withdraw = 0;
        amount_left = budget;

        printf("The sources of the budget: ");
        scanf("%s", sources);

        // Get and format the current date and time
        strftime(date, 20, "%Y-%m-%d", localtime(&t));
        strftime(timee, 20, "%H:%M:%S", localtime(&t));

        // Open the CSV file in append mode
        fi = fopen(filename, "a+");
        if (fi == NULL) {
            perror("Error opening file");
            return 1;
        }

        // Write the header row and the initial budget entry
        fprintf(fi, "Budget,Withdraw,Amount_Left,Purpose,Date,Time\n");
        fprintf(fi, "%i,%i,%i,Initial Budget: %s,%s,%s\n", budget, withdraw, amount_left, sources, date, timee);
        fclose(fi);

        printf("Initial budget of %d recorded in %s\n", budget, filename);

    } else {
        // --- Subsequent runs: Read the last entry and record a new withdrawal ---

        // Open the file for reading to get the last known amount
        fi = fopen(filename, "r");
        if (fi == NULL) {
            perror("Error opening file");
            return 1;
        }

        char myString[100];
        char last_line[100] = "";

        // Read the file line by line to get the last line
        while (fgets(myString, sizeof(myString), fi) != NULL) {
            strcpy(last_line, myString);
        }
        fclose(fi);

        // Parse the last line to get the remaining budget
        char *token = strtok(last_line, ",");
        // We need the third token which is the amount_left
        for (int i = 0; i < 2 && token != NULL; i++) {
            token = strtok(NULL, ",");
        }

        if (token != NULL) {
            sscanf(token, "%i", &budget);
        } else {
            printf("Could not parse the last budget amount. Starting fresh.\n");
            budget = 0; // Default value if parsing fails
        }

        printf("Current amount left: %d\n", budget);
        printf("The amount to be withdrawn: ");
        scanf("%i", &withdraw);

        amount_left = budget - withdraw;

        printf("The withdrawal purpose: ");
        scanf("%s", withdrawal_purpose);

        // Get and format the current date and time
        strftime(date, 20, "%Y-%m-%d", localtime(&t));
        strftime(timee, 20, "%H:%M:%S", localtime(&t));

        // Open the file in append mode to add the new transaction
        fi = fopen(filename, "a+");
        if (fi == NULL) {
            perror("Error opening file");
            return 1;
        }
        fprintf(fi, "%i,%i,%i,%s,%s,%s\n", budget, withdraw, amount_left, withdrawal_purpose, date, timee);
        fclose(fi);

        printf("Withdrawal of %d recorded. Amount left: %d\n", withdraw, amount_left);
    }

    return 0;
}
