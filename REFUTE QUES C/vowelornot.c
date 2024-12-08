#include <stdio.h>
#include <ctype.h>
int main () 
{
    char input[2];

    printf("Enter a single character: ");
    scanf("%1s",input);
    if (isalpha(input[0]) && input[1] == '\0'){
        char ch = tolower(input[0]);

        if (ch == 'a' || ch == 'e' || ch == 'i' || ch == 'o' || ch == 'u'){
            printf("%c is a vowel.\n", input[0]);
        }else {
            printf("%c is not a vowel.\n", input[0]);

        }
    } else {
        printf("Invalid input. Please enter a single alphabetric character. \n");

    }        
    return 0;
}