#include <iostream>

using namespace std; 

int main() {
    int i = 0; 
    
    LOOP: 
        i++;
        if (i < 10) {
            cout << i << endl;
            goto LOOP;
        }
        else {
            cout << i;
        }
}