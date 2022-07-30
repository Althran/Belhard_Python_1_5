"""
ЗАДАНИЕ
--------------------------------------------------------------------------------
Напишите программу, которая принимает текст и выводит два слова:
наиболее часто встречающееся и самое длинное.

можно решить с помощью циклов и переменных, но предпочтительней с
помощью модуля collections, используя collections.Counter
"""
from collections import Counter


def common_and_longest(text: str) -> tuple:
    common = None
    longest = None
    text1 = text.split()
    common = (Counter(text1).most_common(1)[0][0])
    longest = max(text1, key=len)
    return common, longest


if __name__ == '__main__':
    assert common_and_longest(
        "привет пока ялюблюpython привет"
    ) == ('привет', 'ялюблюpython')
    print('Решено!')
