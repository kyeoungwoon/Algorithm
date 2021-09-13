#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main(){
    int num;
    cin >> num;

    vector<int> temp;

    for(int i=0; i<num; i++){
        int tp;
        cin >> tp;
        temp.push_back(tp);
    }
    sort(temp.begin(), temp.end());
    for(int i=0; i<num; i++){
        // cout << temp[i] << endl; 
        cout << temp[i] << '\n'; // endl은 output buffer을 비우기 떄문에 느림
    }
    
    return 0;
}
