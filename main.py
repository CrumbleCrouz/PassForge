import os
from random import randint


class Password:
    def __init__(self, min_size=None, n_numb=None, n_alph=None, not_numb=None, not_alpha=None):
        if min_size:
            self._len = min_size
        else:
            raise ValueError("You must specify the size of the password !")
        self._numbers_a = n_alph if n_alph is not None else special_division(min_size)
        self._numbers_n = n_numb if n_numb is not None else min_size - self._numbers_a
        self._forbid_alph = not_numb
        self._forbid_numb = not_alpha

    def generate(self):
        raw_password = []
        str_password = ""
        if self._numbers_a > 0:
            raw_password += self.with_alpha()
        if self._numbers_n > 0:
            raw_password += self.with_number()

        for e in custom_shuffle(raw_password):
            str_password += str(e)
        return str_password

    def with_number(self) -> list:
        numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        if self._forbid_numb is not None:
            for e in self._forbid_numb:
                for ind in range(len(numbers)):
                    if e == numbers[ind]:
                        numbers.pop(ind)
                        break
        return [numbers[randint(0, len(numbers) - 1)] for it in range(self._numbers_n)]

    def with_alpha(self, char_type: str = "all") -> list:
        alpha_maj = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
                     'U', 'V', 'W', 'X', 'Y', 'Z']
        alpha_min = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                     'u', 'v', 'w', 'x', 'y', 'z']
        if self._forbid_alph is not None:
            for e in self._forbid_alph:
                for ind in range(len(alpha_min)):
                    if e == alpha_min[ind]:
                        alpha_min.pop(ind)
                        break
                for ind in range(len(alpha_maj)):
                    if e == alpha_maj[ind]:
                        alpha_maj.pop(ind)
                        break
        match char_type.lower():
            case "all":
                return [alpha_maj[randint(0, len(alpha_maj) - 1)] if randint(1, 2) % 2 == 0 else
                        alpha_min[randint(0, len(alpha_min) - 1)] for it in range(self._numbers_a)]
            case "maj":
                return [alpha_maj[randint(0, len(alpha_maj) - 1)] for it in range(self._numbers_a)]
            case "min":
                return [alpha_min[randint(0, len(alpha_min) - 1)] for it in range(self._numbers_a)]


def special_division(n):
    p = 0.75
    while True:
        try:
            int(n * p)
            return int(n * p)
        except TypeError:
            p -= 0.01
            continue


def custom_shuffle(original_list):
    shuffled_list = original_list.copy()

    for i in range(len(shuffled_list) - 1, 0, -1):
        j = randint(0, i)
        shuffled_list[i], shuffled_list[j] = shuffled_list[j], shuffled_list[i]

    return shuffled_list
