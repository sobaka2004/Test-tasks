import statistics
import argparse
import os

def counter(data: list[int], number: int) -> int:
    count = 0
    for i in data:
        if i != number:
            count += abs(i - number)
            if count > 20:
                return -1
    return count

if __name__=="__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument("file_path", type=str, help="Путь к файлу")
    argument = parser.parse_args()

    try:
        if not os.path.exists(argument.file_path):
            raise FileNotFoundError("Файл не найден")
        elif os.path.getsize(argument.file_path) == 0:
            raise ValueError()
        
        numbers = []
        with open(argument.file_path, "r", encoding="utf-8") as file:
            for line in file:
                clear_line = line.strip()
                if clear_line:
                    numbers.append(int(clear_line))
            
            if numbers:
                median_number = statistics.median_low(numbers)
                answer = counter(numbers, median_number)
                if answer == -1:
                    print("20 ходов недостаточно для приведения всех элементов массива к одному числу")
                else:
                    print(answer)
            else:
                print("В файле только пустые строки")

    except FileNotFoundError as error:
        print(f"{error}")
    except ValueError:
        print("В файле есть буквы или он пуст")
    except Exception as error:
        print(f"Ошибка :( \n {error}")