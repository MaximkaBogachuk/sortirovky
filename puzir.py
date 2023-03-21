def puzir(N,array):    
    from datetime import datetime
    import time
    start_time = datetime.now()

 
    for i in range(N-1):
        for j in range(N-i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
    
    #print(a)
    time.sleep(0.000000000000001)

    print(datetime.now() - start_time)
    vremya=(datetime.now() - start_time)
    return (array,str(vremya))

