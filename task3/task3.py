import argparse
import json
import os

def fill_values(data: list | dict | str | int, values_source: dict) -> None:
    if isinstance(data, list):
        for element in data:
            fill_values(element, values_source)
            
    elif isinstance(data, dict):
        if "id" in data and data["id"] in values_source:
            data["value"] = values_source[data["id"]]
            
        if "values" in data:
            fill_values(data["values"], values_source)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("values_file_path", type=str, help="Путь к файлу values.json")
    parser.add_argument("tests_file_path", type=str, help="Путь к файлу tests.json")
    parser.add_argument("report_file_path", type=str, help="Путь к файлу report.json")
    
    argument = parser.parse_args()

    try:
        if not os.path.exists(argument.values_file_path):
            raise FileNotFoundError("Файл со значениями не найден")
        if not os.path.exists(argument.tests_file_path):
            raise FileNotFoundError("Файл с тестами не найден")

        with open(argument.values_file_path, "r", encoding="utf-8") as file:
            input_values = json.load(file)
        with open(argument.tests_file_path, "r", encoding="utf-8") as file:
            input_tests = json.load(file)

        if not input_values or "values" not in input_values:
            raise ValueError("Файл values.json пуст или в нем отсутсвует ключ values")

        value_by_id = {}
        for element in input_values["values"]:
            value_by_id[element["id"]] = element["value"]

        if "tests" not in input_tests:
            raise ValueError("В файле tests.json отсутсвует ключ tests")
            
        fill_values(input_tests["tests"], value_by_id)

        with open(argument.report_file_path, "w", encoding="utf-8") as file:
            json.dump(input_tests, file, indent=4, ensure_ascii=False)
            
        print(f"Отчет записан в файл по пути: {argument.report_file_path}")

    except FileNotFoundError as error:
        print(f"{error}")
    except ValueError as error:
        print(f"{error}")
    except json.JSONDecodeError:
        print("Один из файлов содержит некорректный json")
    except Exception as error:
        print(f"Ошибка :( \n {error}")