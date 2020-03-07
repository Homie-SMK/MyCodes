/*
  Thanos sort is a supervillain sorting algorithm, 
  which works as follows: if the array is not sorted, 
  snap your fingers* to remove the first or the second half of the items, and repeat the process.

  Given an input array, what is the size of the longest sorted array you can obtain from it using Thanos sort?

  *Infinity Gauntlet required.

  <Input>
  The first line of input contains a single number n (1≤n≤16) — the size of the array. n is guaranteed to be a power of 2.

  The second line of input contains n space-separated integers ai (1≤ai≤100) — the elements of the array.

  <Output>
  Return the maximal length of a sorted array you can obtain using Thanos sort. 
  The elements of the array have to be sorted in non-decreasing order.
*/

#include <stdio.h>
#include <math.h>
#define SIZE 20

int thanos(int arr[], int l, int r)
{
    if(l == r)  return 1;
    int half = r - l + 1 >> 1;
    int m = l + half;
    int answer1 = thanos(arr, l, m - 1);
    int answer2 = thanos(arr, m, r);
    if(arr[m] >= arr[m-1] && answer1 == answer2 && answer1 == half) return answer1 + answer2;
    else return max(answer1, answer2);
}


int main(void)
{
    int size, i;
    int arr[SIZE];

    while(scanf("%d", &size))
    {
        for(i = 0 ; i < size ; i++)
        {
            scanf("%d", &arr[i]);
        }
        printf("%d\n", thanos(arr, 1, size));
    }
    return 0;
}
