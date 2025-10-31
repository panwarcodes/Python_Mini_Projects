# Alarm_Clock by @panwarcodes/github
import time
import winsound

# Making alarm ringtone
def alarm():
    for i in range(1, 10):
        winsound.Beep(i * 100, 200)

# Alarm setting logic
set_time = int(input("After how many minutes do I call alarm: "))
print(f"Alarm set for {set_time} minute(s). Waiting...")
time.sleep(60 * set_time)


# Call alarm
alarm()