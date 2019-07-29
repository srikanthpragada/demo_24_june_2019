from threading import Thread
import threading

class PrimeThread(Thread):
    def __init__(self, num):
        super().__init__()
        self.num = num

    def run(self):
        print("Checking : ", self.num)
        for n in range(2, self.num // 2 + 1):
            if self.num % n == 0:
                print(f"{self.num} is not a prime number!")
                break
        else:
            print(f"{self.num} is a prime number!")


nums = [393939393, 2334343434349, 29292939327, 38433828283, 62551414124111]
# Open file
for n in nums:
    t = PrimeThread(n)
    t.start()

# wait for termination of all threads
for t in threading.enumerate():
    if t != threading.current_thread():
        t.join()


print("\nThe End\n")
# close file