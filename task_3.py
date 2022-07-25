# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

def coding(string):
    count = 1
    code_str = ''
    for i in range(len(string)-1):
        if string[i] == string[i+1]:
            count += 1
        else:
            code_str = code_str + str(count) + string[i]
            count = 1
    if count > 1 or (string[-2] != string[-1]):
        code_str = code_str + str(count) + string[-1]
    return code_str

def decoding(code_str):
    number = ''
    decode_str = ''
    for i in range(len(code_str)):
        if code_str[i].isdigit():
            number += code_str[i]
        else:
            decode_str = decode_str + code_str[i] * int(number)
            number = ''
    return decode_str

    
text = input('Введите текст для сжатия: ')
print('Текст после сжатия: ', coding(text))
print('Текст после восстановления: ', decoding(coding(text)))
