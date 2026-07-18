import argparse

def path(n: int, m: int) -> str:
    path = []
    index = 0

    while True:
        path.append(str(index + 1))
        # Индекс сдвигается на шаг m, ва при выходе из границы возвращается в начало
        index = (index + m - 1) % n
        if index == 0:
            break
    return "".join(path)

def join_paths(n1: int, m1: int, n2: int, m2: int) -> str:
    result = []
    result.append(path(n1, m1))
    result.append(path(n2, m2))
    return "".join(result)

if __name__=="__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument("n1", type=int, help="Размер первого массива")
    parser.add_argument("m1", type=int, help="Интервал для первого массива")
    parser.add_argument("n2", type=int, help="Размер второго массива")
    parser.add_argument("m2", type=int, help="Интервал для второго массива")

    args = parser.parse_args()

    if args.n1 <= 0 or args.m1 <= 0 or args.n2 <= 0 or args.m2 <= 0:
            print("Все аргументы должны быть больше нуля")
    else:
        final_result = join_paths(args.n1, args.m1, args.n2, args.m2)
        print(final_result)