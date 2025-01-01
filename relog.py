import time

while True:

    tiempo = time.strftime('%H:%M:%S')
    print(f'\rHora actual: {time}', end='')

    time.sleep(1)