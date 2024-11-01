from ..lib import get_spam
import time
import random
import clargs


def continuous_spam_run(
        spam_speed: int,
):
    """
    Keeps serving from the kitchen

    @param spam_speed: on average we will serve you this many items per minute
    """
    avg_sleep_sec = 60 / spam_speed

    while True:
        sleep_sec = random.random() * avg_sleep_sec * 2
        time.sleep(sleep_sec)
        print(get_spam())


if __name__ == "__main__":
    clargs.create_parser_and_run(continuous_spam_run)
