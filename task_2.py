# Создайте программу для игры в "Крестики-нолики".

def move(array, msg1, msg2, msg3):
       
       x = int(input(msg1))
       while not 0 <= x <= 2:
               x = int(input(msg1))
       y = int(input(msg2))       
       while not 0 <= y <= 2:
              y = int(input(msg2))
       if array[y][x] == '*':
              array[y][x] = msg3
              for i in arr:
                     print(*i)
       else:
              print('Ход невозможен, позиция занята. Повторите попытку!')
              move(array, msg1, msg2, msg3)


arr = [['*', '*', '*'],
       ['*', '*', '*'],
       ['*', '*', '*']]
count = 0
while count <= 9:
       msgX_x = 'Игрок крестиками введите № столбца: '
       msgX_y = 'Игрок крестиками введите № строки: '
       msgX = 'X'
       move(arr, msgX_x, msgX_y, msgX)
       count += 1
       if ((arr[0][0] == 'X' and arr[0][1] == 'X' and arr[0][2] == 'X') or 
           (arr[1][0] == 'X' and arr[1][1] == 'X' and arr[1][2] == 'X') or 
           (arr[2][0] == 'X' and arr[2][1] == 'X' and arr[2][2] == 'X') or
           (arr[0][0] == 'X' and arr[1][0] == 'X' and arr[2][0] == 'X') or 
           (arr[0][1] == 'X' and arr[1][1] == 'X' and arr[2][1] == 'X') or 
           (arr[0][2] == 'X' and arr[1][2] == 'X' and arr[2][2] == 'X') or
           (arr[0][0] == 'X' and arr[1][1] == 'X' and arr[2][2] == 'X') or 
           (arr[2][0] == 'X' and arr[1][1] == 'X' and arr[0][2] == 'X')):
              print('Победили крестики')
              break 
       if count == 9:
              print('Ничья')
              break
       msgO_x = 'Игрок ноликами введите № столбца: '
       msgO_y = 'Игрок ноликами введите № строки: '
       msgO = 'O'
       move(arr, msgO_x, msgO_y, msgO)
       count += 1
       if ((arr[0][0] == 'O' and arr[0][1] == 'O' and arr[0][2] == 'O') or 
           (arr[1][0] == 'O' and arr[1][1] == 'O' and arr[1][2] == 'O') or 
           (arr[2][0] == 'O' and arr[2][1] == 'O' and arr[2][2] == 'O') or
           (arr[0][0] == 'O' and arr[1][0] == 'O' and arr[2][0] == 'O') or 
           (arr[0][1] == 'O' and arr[1][1] == 'O' and arr[2][1] == 'O') or 
           (arr[0][2] == 'O' and arr[1][2] == 'O' and arr[2][2] == 'O') or
           (arr[0][0] == 'O' and arr[1][1] == 'O' and arr[2][2] == 'O') or 
           (arr[2][0] == 'O' and arr[1][1] == 'O' and arr[0][2] == 'O')):
              print('Победили нолики')
              break 
