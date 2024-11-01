This is an example repository accompanying a [post on my blog][1].


It is a python projects with three entry-points:

- `spam/quickscripts/simple_spam.py`
- `spam/quickscripts/some_spam.py`
- `spam/longscripts/continuous_spam.py`

The last two scripts use [`clargs`][2], the first is a simple example without external libraries.

All three depend on `spam/lib/libspam.py`.


The way to run the examples, is to first install the project in your `venv`, and then run:

- `python -m spam.quickscripts.simple_spam`
- `python -m spam.quickscripts.some_spam 10`
- `python -m spam.longscripts.continuous_spam 100`


[1]: https://blog.claude.nl/posts/how-to-structure-a-python-project-with-multiple-entry-points/
[2]: https://pypi.org/project/clargs/
