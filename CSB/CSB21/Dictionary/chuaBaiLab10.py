number_list = ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X',
'XI', 'XII', 'XIII', 'XIV', 'XV', 'XVI', 'XVII', 'XVIII', 'XIX', 'XX']
# number_list -> dictionary
dic = {}
for i in range(len(number_list)):
    key = number_list[i]  # key: La Mã
    value = i + 1         # value: Ả Rập
    dic[key] = value
dic
