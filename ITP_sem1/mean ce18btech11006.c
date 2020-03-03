#include <stdio.h>
void main(){
	int n,i;
	double mean=0;
	printf("enter the number of numbers you want to find the mean");
	scanf("%d",&n);//scannning the number of elements you want
	int arr[n];
	for(i=0;i<n;i++){    //finding the mean using for loop
		scanf("%d",&arr[i]);
		mean=mean+arr[i];}
	mean=mean/n;
		printf("the mean of the numbers is %lf " ,mean);
}