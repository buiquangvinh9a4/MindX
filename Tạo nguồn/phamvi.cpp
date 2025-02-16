#include <iostream>
using namespace std;

class HinhChuNhat {
public:
    double chieuDai, chieuRong;
    void nhap(double x = 0, double y = 0) { 
        chieuDai = x;
        chieuRong = y;
    }  
    void thongTin() {          
        cout << "Chiều dài: " << chieuDai << ", ";
        cout << "Chiều rộng: " << chieuRong << endl;
    }

};


int main() {
    HinhChuNhat hinh1, hinh2;
    hinh1.nhap(10, 5.5);
    cout << hinh1.chieuDai << endl;
}



