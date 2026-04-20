import threading

def run_threads(passwords, worker, threads=5):
    def task(pwd):
        worker(pwd)

    thread_list = []

    for pwd in passwords:
        t = threading.Thread(target=task, args=(pwd,))
        t.start()
        thread_list.append(t)

        if len(thread_list) >= threads:
            for th in thread_list:
                th.join()
            thread_list = []

    for th in thread_list:
        th.join()
