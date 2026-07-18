import argparse
import math
import os


def get_point_position(x: float, y: float, x0: float, y0: float, a: float, b: float) -> int:
    '''
    Определяет положение точки относительно эллипса через каноническое уравнение
    Если точка на границе эллипса, выводит 0, если внутри - 1, если снаружи - 2
    '''
    value = ((x - x0)**2) / (a**2) + ((y - y0)**2) / (b**2)
    if math.isclose(value, 1.0, rel_tol=1e-9):
        return 0
    elif value < 1.0:
        return 1
    else:
        return 2

if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("ellipse_file", type=str, help="Файл с координатами и радиусом эллипса")
    parser.add_argument("points_file", type=str, help="Файл с координатами точек")
    
    argument = parser.parse_args()

    try:
        if not os.path.exists(argument.ellipse_file):
            raise FileNotFoundError("Файл с координатами центра и радиусами эллипса не найден")
        if not os.path.exists(argument.points_file):
            raise FileNotFoundError("Файл с координатами точек не найден")

        with open(argument.ellipse_file, 'r', encoding='utf-8') as file:
            x0, y0 = map(float, file.readline().strip().split())
            a, b = map(float, file.readline().strip().split())

        with open(argument.points_file, 'r', encoding='utf-8') as file:
            for line in file:
                if not line.strip():
                    continue
                x, y = map(float, line.strip().split())
                position = get_point_position(x, y, x0, y0, a, b)
                print(position)

    except FileNotFoundError as error:
        print(f"{error}")
    except ValueError:
        print("В файлах находятся не только числа")
    except ZeroDivisionError:
        print("Радиус эллипса не может быть равен нулю")
    except Exception as error:
        print(f"Ошибка :( \n {error}")