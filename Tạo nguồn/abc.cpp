#include <iostream>
using namespace std;

class HinhChuNhat {
private:    
    double chieuDai, chieuRong;
public:     
    // truyền giá trị cho phương thức nhap() 
    void nhap(double x = 0, double y = 0) { 
        chieuDai = x;
        chieuRong = y;
    }  
    // phương thức hiển thị thông tin của hình chữ nhật
    void thongTin() {          
        cout << "Chiều dài: " << chieuDai << ", ";
        cout << "Chiều rộng: " << chieuRong << endl;
    }

};


int main() {
    HinhChuNhat hinh1, hinh2;
    hinh1.nhap();
    hinh2.nhap(10.5, 5);
    cout << "Hình 1: ";
    hinh1.thongTin();
    cout << "Hình 2: ";
    hinh2.thongTin();

    return 0;
}



