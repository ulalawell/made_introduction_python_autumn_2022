import time


def mean(k):
    def _mean(func):
        statistics = []

        def wrapper(*args, **kwargs):
            start_ts = time.time()
            result = func(args[0])
            end_ts = time.time()
            statistics.append(end_ts - start_ts)

            if k > len(statistics):
                print("Mean time for {} calls is {} sec.".format(
                    k, sum(statistics) / len(statistics)))
            else:
                print("Mean time for {} calls is {} sec.".format(
                    k, sum(statistics[-k:]) / k))

            return result

        return wrapper

    return _mean


@mean(10)
def foo(arg1):
    pass


@mean(2)
def boo(arg1):
    delay_sec = 0.5
    time.sleep(delay_sec)
    pass


if __name__ == '__main__':
    for _ in range(15):
        print(foo("Walter"))

    for _ in range(20):
        print(boo("Scott"))

    print('ok')
