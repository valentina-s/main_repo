if __name__ == "__main__":
    
    import os
    import time
    import sys
    sys.stdout.flush()


    for i in range(10):
        time.sleep(1)
        print(i)
        sys.stdout.flush()
    f  = open(os.path.join('data','flag.txt'),'w')
    f.write('400')
        
    
    #raise ValueError('Error!')       