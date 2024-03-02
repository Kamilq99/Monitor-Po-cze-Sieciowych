import psutil
import time

def generate_network_report():
    connections = psutil.net_connections(kind='inet')

    report = []
    for conn in connections:
        connection_info = {
            'pid': conn.pid or 'N/A',
            'laddr': conn.laddr,
            'raddr': conn.raddr,
            'status': conn.status
        }
        report.append(connection_info)

    return report

def main():
    try:
        while True:
            network_report = generate_network_report()

            print("Aktywne połączenia sieciowe:")
            for connection in network_report:
                print(connection)

            time.sleep(5)
    except KeyboardInterrupt:
        print("Przerwano monitorowanie połączeń sieciowych.")

if __name__ == "__main__":
    main()