#include <stdio.h>
#include <string.h>
#include "myscanner.h"

extern int yylex();
extern int yylineno;
extern char* yytext;
char keywords[32][10] = {"auto","break","case","char","const","continue","default",
                            "do","double","else","enum","extern","float","for","goto",
                            "if","int","long","register","return","short","signed",
                            "sizeof","static","struct","switch","typedef","union",
                            "unsigned","void","volatile","while"};
int check_keyword(char *s)
{
	int i;
	for(i=0;i<32;i++)
	{
		if(strcmp(keywords[i],s)==0)
		{
			return 1;
		}
	}
	return 0;
}
int main()
{
	int n,count=1;
	n=yylex();
	printf("%d\n",n );
	while(n)
	{
		if (n==IF)
		{
				printf("Found IF BLOCK %s from line number %d\n",yytext,count);

		}
		else if(n==ELSE){
				printf("Found ELSE BLOCK %s from line number %d\n",yytext,count);
		}

			else if(n==IDENTIFIER)
		{
			if(check_keyword(yytext))
			{
				printf("Found KEYWORD %s at line number %d\n",yytext,count);
			}
			else
			{
				printf("Found IDENTIFIER %s at line number %d\n",yytext,count);
			}

		}
		else if(n==NUMBER)
		{
			printf("Found NUMBER %s at line number %d\n",yytext,count);
		}
		else if(n==NEWLINE){
			count++;
		}
		else if(n==FOR){
			printf("Found FOR %s at line number %d\n",yytext,count);
		}
		else if(n==WHILE){
			printf("Found WHILE %s at line number %d\n",yytext,count);
		}
		n=yylex();
	}
	return 0;
}

/*
smt ("if".*[\n\t].*[\{][.*{smt1}][\}])|("if".*[\n].*[\{]([.*{smt1}])[\}]"else".*[\{]([.*{smt1}])[\}])
smt1 (("if".*[\n].*[\{]({smt1})[\}])|("if".*[\n].*[\{]({smt1})[\}]"else".*[\{]({smt1})[\}])|{fun})*

*/