#include <stdio.h>
void merge(int A[],int start,int m,int end);
void mergesort(int A[],int start,int end);
void main() {
 int n,j;
  
  printf("Enter the number of elements to be sorted:");
  scanf("%d",&n);
  int A[n];
  
  printf("Enter the  elements: ",n);
  for(j=0;j<n;j++)
  {
    scanf("%d",&A[j]);
  }
  mergesort(A,0,n-1);
  for(int j=0;j<n;j++)
  {
    printf("%d ,",A[j]);
  }
  
}

void merge(int A[],int start,int m,int end)//This function merges sorted array
{
  int i,j,k;
  int left=m-start+1;
  int right=end-m;
  int L[left];
  int R[right];
  for(i=0;i<left;i++)
  {
    L[i]=A[start+i];
  }
  for(j=0;j<right;j++)
  {
    R[j]=A[m+1+j];
  }
   i=0;
   j=0;
   k=start;
  while(i<left&&j<right)
  {
    if(L[i]<=R[j])
    {
      A[k]=L[i];
      i=i+1;
    }
    else
    {
      A[k]=R[j];
      j=j+1;
    }
      k=k+1;
  }
  while(i<left)
  {
    A[k]=L[i];
    i=i+1;
    k=k+1;
  }
   while(j<right)
  {
    A[k]=R[j];
    j=j+1;
    k=k+1;
  }
}
void mergesort(int A[],int start,int end)//Recursive function which divides sorting into smaller problem
{
  if(start<end)
  {
    int m=(start+end)/2;
    mergesort(A,start,m);
    mergesort(A,m+1,end);
    merge(A,start,m,end);
  }
  
}

