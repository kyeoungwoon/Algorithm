#include <stdio.h>

void SelectionSort(int* arr, int len){
    for(int i=0; i<len; i++){
        for(int j=i+1; j<len; j++){
            if(arr[i]>arr[j]){
                int temp;
                temp=arr[i];
                arr[i]=arr[j];
                arr[j]=temp;
            }
        }
    }
}

int main(){
    int tcase;
    scanf("%d", &tcase);
    int arr[tcase];
    for(int i=0; i<tcase; i++){
        scanf("%d ", &arr[i]);
    }
    SelectionSort(arr, tcase);
    printf("%d %d", arr[0], arr[1]);
}
