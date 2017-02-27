from threading import Thread, Event
import time


class ProgressThread(Thread):
    def __init__(self, worker):
        super().__init__()
        self.worker = worker

    def run(self):
        while self.worker.get_event().wait():
            print(self.worker.get_progress_message())
            if self.worker.is_exit():
                break
            self.worker.get_event().clear()


class Worker:
    def __init__(self, count=100):
        self.count = count
        self.progress_msg = None
        self.exit = False
        self.event = Event()

    def get_event(self):
        return self.event

    def get_progress_message(self):
        return self.progress_msg

    def is_exit(self):
        return self.exit

    def do_work(self):
        for i in range(self.count):
            print('processing item {}'.format(i))
            if i != 0 and (i+1) % 10 == 0:
                self.progress_msg = '%d items processed...' % (i+1)
                self.event.set()
            time.sleep(0.0001)
        self.exit = True
        self.progress_msg = 'exiting'
        self.event.set()


def main():
    worker = Worker()
    ProgressThread(worker).start()
    worker.do_work()


if __name__ == '__main__':
    main()