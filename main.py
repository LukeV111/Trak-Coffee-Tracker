import machine
import time
import socket

def http_get(url):
    _, _, host, path = url.split('/', 3)
    addr = socket.getaddrinfo(host, 80)[0][-1]
    s = socket.socket()
    s.connect(addr)
    s.send(bytes('GET /%s HTTP/1.0\r\nHost: %s\r\n\r\n' % (path, host), 'utf8'))
    while True:
        data = s.recv(100)
        if data:
            print(str(data, 'utf8'), end='')
        else:
            break
    s.close()

while 1:
    trig=machine.Pin(5,machine.Pin.OUT)
    trig.low()
    time.sleep_ms(2)
    trig.high()
    time.sleep_ms(10)
    trig.low()
    echo=machine.Pin(4,machine.Pin.IN)
    while echo.value() == 0:
        pass
    t1 = time.ticks_us()
    while echo.value() == 1:
        pass
    t2 = time.ticks_us()
    cm = (t2 - t1) / 58.0
    print(cm)
    time.sleep(1)


    if cm >= 15:
        print('object_present is now False') 
        time.sleep(1)
        flag_reset = 0
        
    elif cm <= 15 and flag_reset == 0:
        print('object_present is now True')
        http_get('https://supply.puristcoffee.com/index.php?coffeeshop=4&machinenumber=6')
        time.sleep(1)
        flag_reset = 1
        
#    if cm >= 15:
#        print('1')
#        time.sleep(1)
#    elif cm <= 15:
#        print('2')
#        time.sleep(1)
