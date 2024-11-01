import random
import re

TEXT = """
Egg and Spam,
Egg, bacon, and Spam,
Egg, bacon, sausage, and Spam,
Spam, bacon, sausage, and Spam,
Spam, egg, Spam, Spam, bacon, and Spam,
Spam, sausage, Spam, Spam, Spam, bacon, Spam, tomato, and Spam,
Spam, Spam, Spam, egg, and Spam,
Spam, Spam, Spam, Spam, Spam, Spam, baked beans, Spam, Spam, Spam, and Spam--
""".lower()

WORDS = re.split(r"\W+", TEXT)


def get_spam() -> str:
    return random.choice(WORDS)
