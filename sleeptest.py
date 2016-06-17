import time

try:
    while True:
        print('I sleep now')
        time.sleep(10)
        print('Sleep over now')
        time.sleep(3)
        print('time to sleep again')
        time.sleep(5)
except KeyboardInterrupt:
    print 'interrupted!'
