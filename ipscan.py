import socket
from ipaddress import ip_network

# Список портов для сканирования
PORTS = {
    "FTP": 21,
    "SSH": 22,
    "PJL": 9100,
    "VNC": 5900,
    "RDP": 3389,
    "RTSP": 554,
    "MySQL": 3306,
    "HTTP": 80,
    "Telnet": 23
}

def scan_ports(ip):
    """Сканирует указанные порты на данном IP-адресе."""
    open_ports = []
    for service, port in PORTS.items():
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(0.5)  # Устанавливаем таймаут
                result = s.connect_ex((ip, port))
                if result == 0:  # Если порт открыт
                    open_ports.append((service, port))
        except Exception as e:
            print(f"Ошибка при сканировании {ip}:{port} - {e}")
    return open_ports

def main():
    # Ввод диапазона IP-адресов
    network = input("Введите диапазон IP-адресов (например, 192.168.1.0/24): ")
    try:
        # Генерация списка IP-адресов из сети
        ip_list = [str(ip) for ip in ip_network(network, strict=False)]
    except ValueError:
        print("Неверный формат сети. Попробуйте снова.")
        return

    print(f"Сканирование сети {network}...")
    for ip in ip_list:
        open_ports = scan_ports(ip)
        if open_ports:
            print(f"Открытые порты на {ip}:")
            for service, port in open_ports:
                print(f"  - {service} (порт {port})")
        else:
            print(f"На {ip} открытых портов не найдено.")

if __name__ == "__main__":
    main()
