def personal_sum(numbers):
    result = 0
    incorrect_data = 0

    for number in numbers:
        try:
            result += number
        except TypeError:
            incorrect_data += 1

    return result, incorrect_data


def calculate_average(numbers):
    try:
        total_sum, incorrect_data_count = personal_sum(numbers)
        count = len(numbers) - incorrect_data_count  # Учитываем некорректные данные

        if count == 0:  # Если после исключения некорректных данных нет чисел
            raise ZeroDivisionError("Нет корректных данных для вычисления среднего.")

        average = total_sum / count
        return average
    except ZeroDivisionError:
        return 0
    except TypeError:
        print("В numbers записан некорректный тип данных.")
        return None

print(f'Результат 1: {calculate_average("1, 2, 3")}') # Строка перебирается, но каждый символ - строковый тип
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}') # Учитываются только 1 и 3
print(f'Результат 3: {calculate_average(567)}') # Передана не коллекция
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}') # Всё должно работать


# def f1(number):
#      return 10 / number
#
# # def f2():
# #      print('That a good day')
# #      result_f1 = f1(0)
# #      return result_f1
#
#
# # def f2():
# #     print('That a good day')
# #     summ = 0
# #     for i in range(-2, 2):
# #         summ += f1(i)
# #     return  summ
#
# def f2():
#     summ = 0
#     for i in range(-2, 2, 1):
#         try:
#             summ += f1(i)
#             print(summ)
#         except ZeroDivisionError as exc:
#             print(f'inside f1 something is wrong: {exc}, but a programm is alive, we are done')
#     return summ / 0
#
#
# try:
#      total = f2()
#      print(f'your result: {total}')
#      # total = f2()
#      # # print(total)
#
# except ZeroDivisionError as exc:
#     print(f'something is wrong - {exc}, but we are strong')