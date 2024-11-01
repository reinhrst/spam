from .. import lib
import clargs


def some_spam_run(
        how_many: int,
        /,
        *,
        shout: clargs.Flag = False,
):
    """
    Serves as much from the spam kitchen as you want

    @param how_many: Specify how many dishes you want
    @param shout: If given, the chef is happy to shout at you
    """
    for i in range(how_many):
        if shout:
            print(lib.get_spam().upper())
        else:
            print(lib.get_spam())


if __name__ == "__main__":
    clargs.create_parser_and_run(some_spam_run)
