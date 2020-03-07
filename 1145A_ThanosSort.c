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