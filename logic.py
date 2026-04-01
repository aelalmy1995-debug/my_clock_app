import time

def get_time() -> dict:
    return {
            "hour": time.strftime("%H"),
            "minutes": time.strftime("%M"),
            "seconds": (time.time() % 60) / 60
            }


def get_date() -> dict:
    return {
            "day": time.strftime("%d"),
            "month": time.strftime("%b"),
            }

