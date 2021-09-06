#include <stdio.h>

// int main(){
//     while(1){
//         int a, b;
//         scanf("%d %d", &a, &b); printf("%d\n", a+b);
//     }
//     return 0;
// }


int main(){
    int a, b;
    while (scanf("%d %d", &a, &b) != EOF){
        printf("%d\n", a+b);
    }
    return 0;
}