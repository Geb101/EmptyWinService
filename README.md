Пустая сужба "Windows"

Из основных функций этой службы это:

1. Логировать события службы в "Просмотр Событий"

     ![image](https://github.com/user-attachments/assets/96bc760f-bceb-4b71-9b12-936eff974169)
   
2. Устанавливать, запусукать, останавливать и удалять через терминал

Установка службы:
  1. Вам нужен Python3:
     
     ```winget install -e --id Python.Python.3.9```
     
  3. Устанвока библеотек для работы со службой:
     
     ```pip install pywin32```
     
  5. Для установки службы:
     
     ```python WinService.py install```
     
  7. Для запуска:
     
     ```python WinService.py start```
    
  9. Для остановки:
      
      ```python WinService.py stop```
     
  11. Что бы удалить службу:
      
      ```python WinService.py remove```
