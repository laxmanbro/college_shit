#include<stdio.h>
void swap(int *a,int *b);
void quicksort(int A[],int start,int end);
int partition(int A[],int start,int end);

void main(){
	int n,i;
	printf("enter the number of elements you want to sort :");
	scanf("%d",&n);
	int A[n];
	printf("enter your elements one by one : \n");
	for(i=0;i<n;i++){
		scanf("%d",&A[i]);
	}
	

quicksort(A,0,n-1);
int j;
printf("the sorted array is ");
for(j=0;j<n;j++)
 printf("%d,",A[j] );
 
}
int partition(int A[],int start,int end){
	int pivot,pindex,i;
	pivot=A[end];
	pindex=start;
	for(i=start;i<=(end-1);i++){
		if(A[i]<=pivot){
			swap(&A[i],&A[pindex]);
			pindex=pindex+1;
		}
	}
	swap(&A[pindex],&A[end]);
	return pindex;
}
void quicksort(int A[],int start,int end){

	int pindex;
	if(start<end)
		{
	pindex=partition(A,start,end);
	quicksort(A,start,pindex-1);
	quicksort(A,pindex+1,end);}
}
void swap(int *a,int *b){
	int temp;
	temp=*a;
	*a=*b;
	*b=temp;
}
