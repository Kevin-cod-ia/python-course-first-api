import time

def duration_time(function):
    def wraper():
        init = time.time()
        function()
        final = time.time()

        print(f'O tempo total da aplicação {function.__name__} foi de {str(init-final)}')

    return wraper




@duration_time
def main():
    for i in range(100000000):
        ...



main()