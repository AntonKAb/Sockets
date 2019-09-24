import socket
import threading
import datetime
from multiprocessing import Process,  freeze_support


class TimeNow:
    def time(self, sock):
        requests_list = ['HOUR', 'SECONDS', 'MINUTES']
        time_now = str(datetime.datetime.now())
        up = sock.upper()
        if up in requests_list:
            if up == 'HOUR':
                return time_now[11:13]
            if up == 'MINUTES':
                return time_now[14:16]
            if up == 'SECONDS':
                return time_now[17:19]
            if up is 'STOP':
                quit()
        else:
            return 'ERROR'

    def server_connection(self):
        with socket.socket() as sock:
            sock.bind(('127.0.0.1', 10001))
            sock.listen(socket.SOMAXCONN)
            count_workers = 5
            for _ in range(count_workers):
                w_list = [Process(target=self.time, args=sock)]
            while True:
                connection.settimeout(5)
                connection, addr = sock.accept()
                for i in w_list:
                    i.start()
                for i in w_list:
                    i.join()
                pt = threading.Thread(target=self.server_connection)
                pt.start()
                with connection:
                    try:
                        while True:
                            data = connection.recv(1024)
                            if not data:
                                break
                            print(data.decode('utf-8'))
                    except socket.timeout:
                        print('Connection has been closed by timeout')
                        break

