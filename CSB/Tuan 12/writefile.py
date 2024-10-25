with open('write.txt', 'w') as file:
    sochan = ''     # xâu chứa các số chẵn
    sole = ''       # xâu chứa các số lẻ
    for i in range(101):
        if i % 2 == 0:     
            sochan = sochan + str(i) + ' ' # nếu là số chẵn, cộng dồn vào xâu
        else:
            sole = sole + str(i) + ' '  # ngược lại
    
    file.write(f'{sochan}\n')
    file.write(sole)