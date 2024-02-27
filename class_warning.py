# -*- config: utf8 -*-

import warnings

list_category = [Warning, UserWarning, DeprecationWarning, SyntaxWarning, RuntimeWarning, FutureWarning,
                 PendingDeprecationWarning, ImportWarning, UnicodeWarning, BytesWarning, ResourceWarning]
list_filter = ['default', 'error', 'ignore', 'always', 'module', 'once']


def division_by_zero(dividend, divider, warning_category):
    try:
        print('Вывод в консоль перед генерацией предупреждения')
        if divider < 0.1:
            warnings.warn('Делитель приближается к нулю', warning_category)
            print('Вывод в консоль после генерации предупреждения')
        else:
            return dividend / divider
    except UserWarning as exc:
        print(f'Предупреждение было было перехвачено как исключение.\n{warning_category().__class__.__name__}: {exc}')


def result(dividend, divider, warning_category, name_filter):
    warnings.simplefilter(name_filter)
    quotient_of_numbers = division_by_zero(dividend, divider, warning_category)
    if quotient_of_numbers is not None:
        print(f'Функция отработала правильно. Она возвращает значение: {int(quotient_of_numbers)}')


result(4, 1, list_category[1], list_filter[3])
