from threading import Thread, Event
import time


class PollingThread(Thread):
    def __init__(self, event):
        super().__init__()
        self.event = event

    def run(self):
        while not self.event.is_set():
            print('polling the service')
            time.sleep(1)
        print('exit polling')


def main():
    event = Event()
    poll = PollingThread(event)
    poll.start()
    time.sleep(5)
    event.set()
    poll.join()


if __name__ == '__main__':
    main()