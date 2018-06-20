import machine
import time


def do_connect():
    import network
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print('connecting to network...')
        sta_if.active(True)
        sta_if.connect('WifiName', 'WifiPassword')
        while not sta_if.isconnected():
            pass
    print('network config:', sta_if.ifconfig())
    time.sleep(7200)
    machine.reset()
