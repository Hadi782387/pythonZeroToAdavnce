import time
import datetime
import pygame

def set_alarm(alarm_time):
    sound_file = "Medium Bell Ringing Far.mp3"
    alarm_time_obj = datetime.datetime.strptime(alarm_time, "%H:%M:%S").time()

    while True:
        current_time_obj = datetime.datetime.now().time()
        print(current_time_obj.strftime("%H:%M:%S"))

        if current_time_obj >= alarm_time_obj:
            print("Wake up!")

            pygame.mixer.init()
            pygame.mixer.music.load(sound_file)
            pygame.mixer.music.play()

            while pygame.mixer.music.get_busy():
                time.sleep(1)
            break

        time.sleep(1)

if __name__ == "__main__":
    alarm_time = input("Enter time to set alarm (HH:MM:SS): ")
    set_alarm(alarm_time)