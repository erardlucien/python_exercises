# functionwithargwithdefaultval:
# arg := argument
# val := value
# a function with arguments with default value.
def ask_ok(prompt, retries=4, reminder='Please try again!'):
    while True:
        ok = input(prompt)
        if ok in ('y', 'ye', 'yes'):
            return True
        if ok in ('n', 'no', 'nop', 'nope'):
            return False
        retries = retries - 1
        if retries < 0:
            raise ValueError('Invalid user reponse!')
        print(reminder)
# Important warning: the default value is evaluated only once.
# This makes a difference when the default is mutable object
# such as list, dictionary, or instance of most classes.


def f(a, L=[]):
    L.append(a)
    return L


def f1(a, L=None):
    if L is None:
        L = []
    L.append(a)
    return L
