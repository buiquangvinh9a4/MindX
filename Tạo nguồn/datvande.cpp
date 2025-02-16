#include <iostream>
using namespace std;

class Cat {
private:    
    string ten;
    string mauSac;
public:      
    void keu() {        // phương thức keu() hiển thị "Meow meow"
        cout << "Meow meow" << endl;
    }
    void chay
};

int main() {
    Cat meo1, meo2;  // khởi tạo 2 đối tượng thuộc lớp Cat
    cout << "Mèo 1 kêu: ";
    meo1.keu();      // gọi phương thức keu() cho meo1
    cout << "Mèo 2 kêu: ";
    meo2.keu();      // gọi phương thức keu() cho meo2
    return 0;
}


