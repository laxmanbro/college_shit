#include <stdio.h>
void MERGE(int Arr[],int start,int m,int end);
void MERGEsort(int Arr[],int start,int end);
void main() {
 int p,j;
  
  printf("Enter the number of elements to be sorted:");
  scanf("%d",&p);
  int Arr[p];
  
  printf("Enter the  elements: ",p);
  for(j=0;j<p;j++)
  {
    scanf("%d",&Arr[j]);
  }
  MERGEsort(Arr,0,p-1);
  for(int j=0;j<p;j++)
  {
    printf("%d ,",Arr[j]);
  }
  
}

void MERGE(int Arr[],int start,int m,int end)//This function merges sorted array
{
  int i,j,k;
  int left=m-start+1;
  int right=end-m;
  int L[left];
  int R[right];
  for(i=0;i<left;i++)
  {
    L[i]=Arr[start+i];
  }
  for(j=0;j<right;j++)
  {
    R[j]=Arr[m+1+j];
  }
   i=0;
   j=0;
   k=start;
  while(i<left&&j<right)
  {
    if(L[i]<=R[j])
    {
      Arr[k]=L[i];
      i=i+1;
    }
    else
    {
      Arr[k]=R[j];
      j=j+1;
    }
      k=k+1;
  }
  while(i<left)
  {
    Arr[k]=L[i];
    i=i+1;
    k=k+1;
  }
   while(j<right)
  {
    Arr[k]=R[j];
    j=j+1;
    k=k+1;
  }
}
void MERGEsort(int Arr[],int start,int end)//Recursive function which divides sorting into smaller problem
{
  if(start<end)
  {
    int m=(start+end)/2;
    MERGEsort(Arr,start,m);
    MERGEsort(Arr,m+1,end);
    MERGE(Arr,start,m,end);
  }
  
}

