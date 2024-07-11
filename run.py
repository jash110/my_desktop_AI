import multiprocessing

# To run Athena
def startAthena():
    # Code for process 1
    print("Process 1 (Athena) is running.")
    from main import start
    start()

# To run hotword
def listenHotword():
    # Code for process 2
    print("Process 2 (Hotword) is running.")
    from engine.features import hotword
    hotword()

# Start both processes
if __name__ == '__main__':
    p1 = multiprocessing.Process(target=startAthena)
    p2 = multiprocessing.Process(target=listenHotword)
    
    try:
        p1.start()
        p2.start()
        p1.join()
    except KeyboardInterrupt:
        print("Interrupted by user")
    finally:
        if p1.is_alive():
            p1.terminate()
            p1.join()
        if p2.is_alive():
            p2.terminate()
            p2.join()
            

    print("System stopped")
