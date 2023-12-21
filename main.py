import types
from datetime import date
from random import randint


class Password:
    def __init__(self, min_size=None, n_numb=None, n_alpha=None, n_char=None, not_numb=None, not_alpha=None,
                 not_char=None, alpha_type="all"):
        match type(min_size):
            case types.NoneType:
                if n_alpha is None or n_numb is None or n_char is None:
                    if not n_numb and not n_alpha and not n_char:
                        raise ValueError("You must specify the size of the password !")
                    raise ValueError("You must specify the size of the password if all custom sizes are not specified!")
            case _:
                try:
                    self._len = int(min_size)
                    if self._len < 1:
                        raise ValueError("The default password size must be greater than 1 !")
                except TypeError:
                    raise ValueError("You must enter a whole number!")

        if min_size:
            calc_prct = special_division(self._len)
            s_prct = calc_prct[0]
            t_prct = calc_prct[1]
        if n_numb:
            try:
                n_numb = int(n_numb)
                if n_numb < 0:
                    raise
            except:
                raise ValueError(f"Specified custom sizes on n_numb must be an integer greater than or equal to 0 !")
        if n_alpha:
            try:
                n_alpha = int(n_alpha)
                if n_alpha < 0:
                    raise
            except:
                raise ValueError(f"Specified custom sizes on n_alpha must be an integer greater than or equal to 0 !")
        if n_char:
            try:
                n_char = int(n_char)
                if n_char < 0:
                    raise
            except:
                raise ValueError(f"Specified custom sizes on n_char must be an integer greater than or equal to 0 !")

        match min_size:
            case 1:
                self._numbers_a = n_alpha if n_alpha is not None else 1
                self._numbers_n = n_numb if n_numb is not None else 0
                self._numbers_c = n_char if n_char is not None else 0
            case 2:
                self._numbers_a = n_alpha if n_alpha is not None else 1
                self._numbers_n = n_numb if n_numb is not None else 1
                self._numbers_c = n_char if n_char is not None else 0
            case 3:
                self._numbers_a = n_alpha if n_alpha is not None else 1
                self._numbers_n = n_numb if n_numb is not None else 1
                self._numbers_c = n_char if n_char is not None else 1
            case _:
                self._numbers_a = n_alpha if n_alpha is not None else s_prct
                self._numbers_n = n_numb if n_numb is not None else t_prct
                self._numbers_c = n_char if n_char is not None else t_prct

        self._forbid_alph = not_numb
        self._forbid_numb = not_alpha
        self._forbid_char = not_char
        self._preferred_alpha = alpha_type

    def generate(self):
        raw_password = []
        str_password = ""
        if self._numbers_a > 0:
            raw_password += self.with_alpha()
        if self._numbers_n > 0:
            raw_password += self.with_number()
        if self._numbers_c > 0:
            raw_password += self.with_char()
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

    def with_alpha(self) -> list:
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
        match self._preferred_alpha.lower():
            case "all" | "default":
                return [alpha_maj[randint(0, len(alpha_maj) - 1)] if randint(1, 2) % 2 == 0 else
                        alpha_min[randint(0, len(alpha_min) - 1)] for it in range(self._numbers_a)]
            case "maj" | "upper":
                return [alpha_maj[randint(0, len(alpha_maj) - 1)] for it in range(self._numbers_a)]
            case "min" | "lower":
                return [alpha_min[randint(0, len(alpha_min) - 1)] for it in range(self._numbers_a)]
            case _:
                raise ValueError("The type of the letters must be upper (or maj), lower (or min) or both "
                                 + "(all or default) !")

    def with_char(self) -> list:
        characters = ['!', '?', '@', '#', '$', '%', '^', '&', '*', '(', ')', '{', '}', '[', ']', '_', '-', '+']
        if self._forbid_char is not None:
            for e in self._forbid_char:
                for ind in range(len(characters)):
                    if e == characters[ind]:
                        characters.pop(ind)
                        break
        return [characters[randint(0, len(characters) - 1)] for it in range(self._numbers_c)]


def special_division(n):
    sixty_percent = int(0.6 * n)
    twenty_percent = int(0.2 * n)
    good = False
    while not good:
        if type(sixty_percent) is not int:
            sixty_percent = take_superior(sixty_percent, n)
        elif type(twenty_percent) is not int or twenty_percent <= 0:
            twenty_percent = take_superior(twenty_percent, n)
        elif sixty_percent + twenty_percent * 2 < n:
            sixty_percent += 1
        elif sixty_percent + twenty_percent * 2 > n:
            sixty_percent -= 1
        else:
            good = True
    return sixty_percent, twenty_percent


def take_superior(n, m):
    while n < m:
        m -= 1
    return m + 1


def custom_shuffle(original_list):
    shuffled_list = original_list.copy()

    for i in range(len(shuffled_list) - 1, 0, -1):
        j = randint(0, i)
        shuffled_list[i], shuffled_list[j] = shuffled_list[j], shuffled_list[i]

    return shuffled_list


if __name__ == "__main__":
    try:
        # Generate a password with the default settings. Customize them will be intensified with the cli interface.
        print(Password(input("What size for the password ? ")).generate())
        input()
    except Exception as err:
        print("\033[H\033[J", end="")
        print('-' * (len(str(err)) + 24))
        print(f"An error has occurred: {err}.")
        print("Press any key to exit...")
        input('-' * (len(str(err)) + 24))
        exit(1)
