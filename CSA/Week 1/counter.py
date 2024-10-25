class Counter:
    count = 0 # thuộc tính
    def __init__(self): # hàm khởi tạo count = 0
        count = 0
    
    def tick(self):     # phương thức tick()
        self.count += 1
    
    def reset(self):    # phương thức reset()
        self.count = 0
        
    def show(self):     # phương thức hiển thị show()
        print(f'Count = {self.count}')
    
def main():
    c1 = Counter()
    c1.show()
    c1.tick()
    c1.show()
    for i in range(5):
        c1.tick()
    c1.show()
    c1.reset()
    c1.show()
    
if __name__ == '__main__':
    main()
    
    