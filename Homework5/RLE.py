# Задача №3
# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

def coding(arr):
    arr_text = list(arr)
    count = 1
    txt_coding = ''
    for i in range(len(arr_text)-1):
        if arr_text[i] == arr_text[i + 1]:
            count += 1
        else:
            txt_coding = txt_coding + str(count) + arr_text[i]
            count =1 
    if count > 1 or (arr_text[len(arr_text)-2] != arr_text[-1]): 
        txt_coding = txt_coding + str(count) + arr_text[-1]

    return txt_coding

def decode(line):
    txt_decoding = ''
    num = ''
    for i in range(len(line)):
        if line[i].isalpha() == False:
            num += line[i]
            
        else:
            txt_decoding = txt_decoding + line[i]*int(num)
            num = ''
    return txt_decoding


line = 'aaaafgaadweeeewwwweWWW'

cod_txt = coding(line)
print((cod_txt))

decod_txt = decode(cod_txt)
print((decod_txt))

