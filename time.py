from datetime import datetime
from time import sleep

if __name__ == '__main__':
    t = input()  # 6 | 16:12:09
    if ":" in t:
        t = t.split(':')
        t = datetime(hour=int(t[0]), minute=int(t[1]), second=int(t[2]), year=datetime.now().year,
                     month=datetime.now().month, day=datetime.now().day)
        # if datetime.now() > t:
        #     t = datetime(hour=int(t[0]), minute=int(t[1]), second=int(t[2]), year=datetime.now().year,
        #                  month=datetime.now().month, day=datetime.now().day)
        while datetime.now() < t:
            print(f"{datetime.now().hour}:{datetime.now().minute}:{datetime.now().second}")
            sleep(1)
        else:
            print("finished!!!")
    else:
        t = int(t)
        for i in range(t):
            print(f"{datetime.now().hour}:{datetime.now().minute}:{datetime.now().second}")
            sleep(1)
        else:
            print("finished!!!")
