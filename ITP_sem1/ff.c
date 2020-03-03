#include<stdio.h>
int fact(int n);
void main(){
	int i,j,n
	scanf("%d",&n);
	
	printf("%d",j);

	
	}

int c(int a,int b){
	return fact(a)/(fact(a-b)*fact(b));
}


int fact(int n){
	if(n>1)
		return n * fact(n-1);
	else
		return 1;
}