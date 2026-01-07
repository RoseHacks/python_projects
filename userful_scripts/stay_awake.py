import ctypes
import time

# This Python script uses the Windows API via the ctypes library to prevent the system from entering sleep

ES_CONTINUOUS = 0x80000000
ES_SYSTEM_REQUIRED = 0x00000001
ES_DISPLAY_REQUIRED = 0x00000002

# It epeatedly sets the thread execution state flags above ^, which signals to the system that user activity is ongoing.

def keep_awake():
    ctypes.windll.kernel32.SetThreadExecutionState(
        ES_CONTINUOUS | ES_SYSTEM_REQUIRED | ES_DISPLAY_REQUIRED
    )

def allow_sleep():
    ctypes.windll.kernel32.SetThreadExecutionState(ES_CONTINUOUS)

# API call every 10 seconds to maintain this state.

try:
    print("BRB...")
    while True:
        keep_awake()
        time.sleep(10)
except KeyboardInterrupt:
    print("Restore sleep ability")
    allow_sleep()

