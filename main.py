from multiprocessing import Process
import time

def mencuci():
    print("Mencuci dimulai...")
    time.sleep(5)
    print("Mencuci selesai!")

def mengeringkan():
    print("Mengeringkan dimulai...")
    time.sleep(3)
    print("Mengeringkan selesai!")

def menyetrika():
    print("Menyetrika dimulai...")
    time.sleep(4)
    print("Menyetrika selesai!")

if _name_ == "_main_":
    proses1 = Process(target=mencuci)
    proses2 = Process(target=mengeringkan)
    proses3 = Process(target=menyetrika)

    proses1.start()
    proses2.start()
    proses3.start()

    proses1.join()
    proses2.join()
    proses3.join()

    print("Semua proses selesai!")
