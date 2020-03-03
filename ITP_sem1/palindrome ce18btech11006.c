#include <stdio.h>
#include<string.h>
void main(){

	int n,i,count=0;
	char str[30];
	printf("enter the word you want to find palindrome or not \n");
	gets(str);//getting string from keyboard 
	n=strlen(str);//finding the length of the string 
	for(i=0;i<n;i++){//finding palindrome by counting the string characters
		if(str[i]==str[n-i-1])
			count++;
	}
	if(count==n){
		printf("yes it is a palindrome\n");
	}
	else
		printf("no its not a palindrome\n");



}