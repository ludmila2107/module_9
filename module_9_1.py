def apply_all_func(int_list, *functions):
    results = {}

    for func in functions:  # Перебираем переданные функции
        results[func.__name__] = func(int_list)  # Вызываем функцию и сохраняем результат в словаре

    return results  # Возвращаем словарь с результатами




print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))