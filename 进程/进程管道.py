import multiprocessing


def send_data(conn, data):
    conn.send(data)


def receive_data(conn):
    print(conn.recv())


def main():
    conn_send, conn_recv = multiprocessing.Pipe()
    process_send = multiprocessing.Process(target=send_data, args=(conn_send, 123))
    process_receive = multiprocessing.Process(target=receive_data, args=(conn_recv,))
    process_send.start()
    process_receive.start()


if __name__ == '__main__':
    main()

