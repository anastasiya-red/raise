class InvalidDataException(Exception):
    def __init__(self, message):
        self.message = message

class ProcessingException(Exception):
    def __init__(self, message):
        self.message = message


def example(a, b):
    if type(a) is str:
        raise InvalidDataException('на месте "а" должно быть число')
    if type(b) is str:
        raise ProcessingException('на месте "b" должно быть число')
    return (a + 2 * b)

def work(a, b):
    try:
        print(example(a,b))
    except (InvalidDataException, ProcessingException) as err:
        print(f'{err.message}')
        raise

try:
    work(5, '5')
except Exception:
    print('всё ещё есть проблема')
else: print('пример решён')


print()
try:
    work(5, 5)
except Exception:
    print('всё ещё есть проблема')
else: print('пример решён')