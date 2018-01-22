%{
	#include "myscanner.h"

%}

letter_ [a-zA-Z_]
digit [0-9]
id {letter_}({letter_}|{digit})*

digits {digit}+
fract ([\.]{digit}*)?
exp ([eE][\+\-]?{digits})?
num {digits}{fract}{exp}

any [.*]
fun {any}

smt ("if".*[\{][.*{smt}*][\}])


if ("if"[ ]*[\(].*)
for ("for"[ ]*[\(].*)
while ("while"[ ]*[\(].*)
else ("else"[ ]*[\{]?)



%%
{if} return IF;
("else"[ ]*[\{]?) return ELSE;
{for} return FOR;
{while} return WHILE;



{id} return IDENTIFIER;
{num} return NUMBER;
[\n] return NEWLINE;
 [^a-zA-Z_] return OTHER;

%%
int yywrap(void)
{
	return 1;
}


