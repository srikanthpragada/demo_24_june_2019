from threading import Thread
import threading


class PrimeThread(Thread):
    def __init__(self, num, file):
        super().__init__()
        self.num = num
        self.file = file

    def run(self):
        print("Checking : ", self.num)
        for n in range(2, self.num // 2 + 1):
            if self.num % n == 0:
                self.file.write(f"{self.num} is not a prime number!\n")
                break
        else:
            self.file.write(f"{self.num} is a prime number!\n")


nums = [393939393, 2334334348, 29292939327, 38433828283, 62551414124111]

# Open file
f = open("primes.txt", "wt")
for n in nums:
    t = PrimeThread(n, f)
    t.start()

# wait for termination of all threads
for t in threading.enumerate():
    if t != threading.current_thread():
        t.join()

print("\nThe End\n")
# close file
f.close()
