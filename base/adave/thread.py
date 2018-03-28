import threading


class DemoThread(threading.Thread):
    def __init__(self, array1):
        threading.Thread.__init__(self)
        self.arr = array1

    def run(self):
        for i in self.arr:
            print("i", i)


array = ["11", "232", "3232344", "888"]
thread = DemoThread(array)
thread.start()
