# ipscaner
IpScaner - это сканеруйт IP на локалном сети 

Как работает программа:
Ввод диапазона IP-адресов: Пользователь вводит диапазон в формате CIDR, например, 192.168.1.0/24.
Сканирование портов: Программа проверяет указанные порты для каждого IP-адреса в сети.
Результаты: Для каждого IP-адреса выводится список открытых портов и соответствующих служб.

Примечания:
Для работы программы могут потребоваться права администратора, если вы сканируете сеть с ограничениями.
Таймаут для проверки портов установлен на 0.5 секунды, чтобы ускорить процесс. Вы можете изменить его при необходимости.
Удачи в использовании! 😊


    "FTP": 21,
    "SSH": 22,
    "PJL": 9100,
    "VNC": 5900,
    "RDP": 3389,
    "RTSP": 554,
    "MySQL": 3306,
    "HTTP": 80,
    "Telnet": 23
