#include <stdio.h>

void Inserting(int Arr[],int n);

void main() {
  int n,j;
  printf("Enter the number of elements you want to sort:");
  scanf("%d",&n);
  int Arr[n];
  printf("Enter all the elements: ",n);
  for(j=0;j<n;j++)
  {
    scanf("%d",&Arr[j]);
  }
  Inserting(Arr,n);
  printf("the elements are  ");

  for(int j=0;j<n;j++)
  {
    printf("%d ,",Arr[j]);
  }
  
}


void Inserting(int Arr[],int n) //function for sorting which inserts certain number between bigger and smaller number
{
  for(int i=0;i<n;i++)
  {
    int value=Arr[i];
    int index=i;
    while(index>0&&Arr[index-1]>value)
    {
      Arr[index]=Arr[index-1];
      index=index-1;
    }
    Arr[index]=value;
  }
}