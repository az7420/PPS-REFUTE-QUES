#include <stdio.h>
#include <string.h>

// Function to check if a string is palindromic
int isPalindrome(char str[]) {
    int start = 0;
    int end = strlen(str) - 1;

    while (start < end) {
        if (str[start] != str[end]) {
            return 0; // Not a palindrome
        }
        start++;
        end--;
    }
    return 1; // Palindrome
}

int main() {
    char str[100];
    
    // Input the string
    printf("Enter a string: ");
    scanf("%s", str);

    // Check if the string is a palindrome
    if (isPalindrome(str)) {
        printf("The string \"%s\" is palindromic.\n", str);
    } else {
        printf("The string \"%s\" is not palindromic.\n", str);
    }

    return 0;
}
