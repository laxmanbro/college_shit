#include <stdio.h>

void INSERT(int B[],int n);

void main() {
  int n,j;
  printf("Enter the number of numbers wanted to be sort:");
  scanf("%d",&n);
  int B[n];
  printf("Enter all the elements you wanted: ",n);
  for(j=0;j<n;j++)
  {
    scanf("%d",&B[j]);
  }
  INSERT(B,n);
  printf("the sorted  elements are  ");

  for(int j=0;j<n;j++)
  {
    printf("%d ,",B[j]);
  }
  
}


void INSERT(int B[],int n) //function for sorting which inserts certain number between bigger and smaller number
{
  for(int i=0;i<n;i++)
  {
    int value=B[i];
    int pivit=i;
    while(pivit>0&&B[pivit-1]>value)
    {
      B[pivit]=B[pivit-1];
      pivit=pivit-1;
    }
    B[pivit]=value;
  }
}