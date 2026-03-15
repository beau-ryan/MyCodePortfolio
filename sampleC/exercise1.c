/* Re-studying the basics in computer programming
For my OS development project 
problem is we don't have a reliable OS without some overhead controller 
e.g. Microsoft, Apple, Linux all being changed and heavily regulated 
and losing trusting users, and maintainers 
Also Due to the rise of this non-sense, predictive AI 
The fear around it so i will practice, practice and practice more 
while rebuilding my full stack digital ecosystem & Operational Systems 

*/

#include <stdio.h>


int main() {
    int myNum = 50;
    char name[] = "John";
    printf("Hello %s\n", name);  // This is a comment
    printf("\nHello World!\n");
    printf("\nHow are you?\n");
    
    printf("\nI am learning C.\nAnd it's alright!");
    
    printf("\nPractice, Practice, Practice/n%d", myNum);
    return 0;
}

// Create variables
int myNum = 15;            // Integer (whole number)
float myFloatNum = 5.99;   // Floating point number
char myLetter = 'D';       // Character

/* Print variables
    printf("%d\n", myNum);
    printf("%f\n", myFloatNum);
    printf("%c\n", myLetter);
    
    int x = 5, y = 6, z = 50;
    printf("%d", x + y + z);
*/

/* This is a comment

\n - it createes a new line
\t - Inserts a horizontal tab	
\\ - Inserts a backslash character (\)	
\\" - Inserts a double quote character
Line 1: #include <stdio.h> tells C to include a header file.
use // for short comments and 
int - stores whole numbers (integers), such as 123 or -123
float - stores numbers with decimals, such as 19.99 or -19.99
char - stores a single character, such as 'a' or 'B'. Characters are surrounded by single quotes
for longer comments.


*/

/*  % declare type 
Print variables
    printf("%d\n", myNum);
    printf("%f\n", myFloatNum);
    printf("%c\n", myLetter);
    printf("%s\n", myString);

    int %d/%i
    char %c
    string %s
    float %f
    double %lf
*/


/*  Data types in C 

    int - 2/4 bytes - storing number values  
    e.g. 1 excludes non-decimal values
    float - 4 bytes This type stores the decimal values Sufficient for storing upto 6/7 decimal digits
    e.g. 2.99
    double - 8 bytes fractions, Sufficient fo storing upto 15 decimal digits
    e.g. 3.99
    char - 1 byte Stores singles characters/letter/number, or ASCII vaules 
    e.g. 'D'

    something you learn new one can write very large or very small floating point numbers 
    e.g this do with using the letter ('e'/'E') e.gg 36e4 meaning 36 x 10^4 =360000
*/
