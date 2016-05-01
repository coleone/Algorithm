#include <stdio.h>
#include <string.h>
#include <stdlib.h>

char* stringRev(char* str){
	if(!str) return;

	int length=strlen(str);
	char* str_2 = (char*)malloc((size_t)length);
	strcpy(str_2, str);

	char* start = str_2;
	char* end = str_2 + strlen(str_2) - 1;
	char temp;
	
	while( end > start){
		temp = *start;
		*start++ = *end;
		*end-- = temp;
	}
	
	str = str_2;

	return str;
}

int main()
{	int i = 0;
	char* str = "123";
	
	for(i = 0; i < strlen(str); i++){
		printf("%c %c \n", *(str+i), str[i]);
	}
	
	str = stringRev(str);
	
	for(i = 0; i < strlen(str); i++){
		printf("%c %c \n", *(str+i), str[i]);
	}
	return 0;
}

