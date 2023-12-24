# Internal modules
import builtins
import sys
import os

# Project modules
import core

# Externals modules
import keyboard as kb
import msvcrt

pressed_key: str = None
pressed_key_code: int = None
numbers_code = {
    79: '1',
    80: '2',
    81: '3',
    75: '4',
    76: '5',
    77: '6',
    71: '7',
    72: '8',
    73: '9',
    82: '0'
}


def initial_screen():
    selected_list = "*  "
    pressing = False
    while True:
        clear_stdin()
        print("\033[H\033[J", end="")
        print(f"╔{'═' * 22}╗")
        print(f"║ [{selected_list[0]}] Default Settings ║")
        print(f"║ [{selected_list[1]}] Custom Settings  ║")
        print(f"║ [{selected_list[2]}] Exit{' ' * 13}║")
        print(f"╚{'═' * 22}╝")
        key = kb.read_event()
        if not pressing:
            if key.scan_code == 72 and not key.is_keypad:  # UP ARROW
                pressing = True
                selected_list = change_str(selected_list, 0, '') if selected_list[0] != '*' else "  *  "
            elif key.scan_code == 80 and not key.is_keypad:  # DOWN ARROW
                pressing = True
                selected_list = ' ' + selected_list if selected_list[2] != '*' else "*  "
            elif key.scan_code == 28:  # ENTER
                if selected_list[0] == '*':
                    return ds_screen()
                elif selected_list[1] == '*':
                    return cs_screen()
                else:
                    return
        else:
            pressing = False
            clear_stdin()


def ds_screen(n='0'):
    clear_stdin()
    pressing = False
    while True:
        print("\033[H\033[J", end="")
        print(f"╔{'═' * (24 + ((len(n) + 2) if len(n) > 6 else 9))}╗")
        print(f"║ Press esc to return to the menu{' ' * ((len(n) - 6) if len(n) > 6 else 1)}║")
        print(f"╠{'═' * 23}╦{'═' * ((len(n) + 2) if len(n) > 6 else 9)}╣")
        print(f"║ Size of the password: ║ {n.center(len(n) if len(n) > 6 else 7)} ║")
        print(f"╚{'═' * 23}╩{'═' * ((len(n) + 2) if len(n) > 6 else 9)}╝")
        key = kb.read_event()
        kb.hook(what_is_this_key)
        if not pressing:
            if pressed_key in core.numbers_str:  # NUMBERS
                pressing = True
                n = n + pressed_key if int(n) > 0 else pressed_key
            elif key.scan_code == 75:  # LEFT ARROW
                pressing = True
                n = str(int(n) - 1) if int(n) > 0 else n
            elif key.scan_code == 77:  # RIGHT ARROW
                pressing = True
                n = str(int(n) + 1)
            elif key.scan_code == 14:  # BACKSPACE
                pressing = True
                n = change_str(n, len(n) - 1, '') if len(n) > 1 else '0'
            elif key.scan_code == 28 and int(n) > 0:  # ENTER
                return result_screen(size=int(n), callback="ds_screen")
            elif key.scan_code == 1:  # ESC
                clear_stdin()
                return initial_screen()
        else:
            pressing = False
            clear_stdin()


def cs_screen(alpha_ind=None, nb_alpha='0', nb_numb='0', nb_char='0', ban_alph=[], ban_numb=[], ban_char=[]):
    clear_stdin()
    pressing = False
    match type(alpha_ind):
        case builtins.int:
            pass
        case builtins.str:
            match alpha_ind:
                case "uppercase":
                    alpha_ind = 1
                case "lowercase":
                    alpha_ind = 2
                case _:
                    alpha_ind = 0
        case _:
            alpha_ind = 0

    alpha_types = ["<- All ->", "<- Uppercase ->", "<- Lowercase ->"]
    selected_list = "*     "
    while True:
        bigger = len(alpha_types[alpha_ind]) if len(alpha_types[alpha_ind]) >= len(nb_alpha) and len(
            alpha_types[alpha_ind]) >= len(nb_numb) and len(alpha_types[alpha_ind]) >= len(nb_char) else len(
            nb_alpha) if len(nb_alpha) >= len(nb_numb) and len(nb_alpha) >= len(nb_char) else len(nb_numb) if len(
            nb_numb) >= len(nb_char) else len(nb_char)
        print("\033[H\033[J", end="")
        print(f"╔{'═' * (30 + bigger)}╗")
        print(f"║ Press esc to return to the menu {' ' * (bigger - 3)}║")
        print(f"╠{'═' * 27}╦{'═' * (bigger + 2)}╣")
        print(f"║ [{selected_list[0]}] Number of letters:    ║ {nb_alpha.center(bigger)} ║")
        print(f"╠{'═' * 27}╬{'═' * (bigger + 2)}╣")
        print(f"║ [{selected_list[1]}] Number of numbers:    ║ {nb_numb.center(bigger)} ║")
        print(f"╠{'═' * 27}╬{'═' * (bigger + 2)}╣")
        print(f"║ [{selected_list[2]}] Number of characters: ║ {nb_char.center(bigger)} ║")
        print(f"╠{'═' * 27}╬{'═' * (bigger + 2)}╣")
        print(f"║ [{selected_list[3]}] Type of letters:      ║ {alpha_types[alpha_ind].center(bigger)} ║")
        print(f"╠{'═' * 27}╩{'═' * (bigger + 2)}╣")
        print(f"║ [{selected_list[4]}] Advanced settings {' ' * (bigger + 7)}║")
        print(f"╠{'═' * (bigger + 30)}╣")
        print(f"║ [{selected_list[5]}] Generate password {' ' * (bigger + 7)}║")
        print(f"╚{'═' * (bigger + 30)}╝")
        key = kb.read_event()
        kb.hook(what_is_this_key)
        if not pressing:
            if pressed_key_code == 72 and not key.is_keypad:  # UP ARROW
                pressing = True
                selected_list = change_str(selected_list, 0, '') if selected_list[0] != '*' else "     *     "
            elif pressed_key_code == 80 and not key.is_keypad:  # DOWN ARROW
                pressing = True
                selected_list = ' ' + selected_list if selected_list[5] != '*' else "*     "
            elif pressed_key in core.numbers_str:  # NUMBERS
                pressing = True
                if selected_list[0] == '*':
                    nb_alpha = nb_alpha + pressed_key if int(nb_alpha) > 0 else pressed_key
                elif selected_list[1] == '*':
                    nb_numb = nb_numb + pressed_key if int(nb_numb) > 0 else pressed_key
                elif selected_list[2] == '*':
                    nb_char = nb_char + pressed_key if int(nb_char) > 0 else pressed_key
            elif key.scan_code == 14:  # BACKSPACE
                pressing = True
                if selected_list[0] == '*':
                    nb_alpha = change_str(nb_alpha, len(nb_alpha) - 1, '') if len(nb_alpha) > 1 else '0'
                elif selected_list[1] == '*':
                    nb_numb = change_str(nb_numb, len(nb_numb) - 1, '') if len(nb_numb) > 1 else '0'
                elif selected_list[2] == '*':
                    nb_char = change_str(nb_char, len(nb_char) - 1, '') if len(nb_char) > 1 else '0'
            elif key.scan_code == 75:  # LEFT ARROW
                pressing = True
                if selected_list[0] == '*':
                    nb_alpha = str(int(nb_alpha) - 1) if int(nb_alpha) > 0 else nb_alpha
                elif selected_list[1] == '*':
                    nb_numb = str(int(nb_numb) - 1) if int(nb_numb) > 0 else nb_numb
                elif selected_list[2] == '*':
                    nb_char = str(int(nb_char) - 1) if int(nb_char) > 0 else nb_char
                elif selected_list[3] == '*':
                    alpha_ind = alpha_ind - 1 if alpha_ind > 0 else 2
            elif key.scan_code == 77:  # RIGHT ARROW
                pressing = True
                if selected_list[0] == '*':
                    nb_alpha = str(int(nb_alpha) + 1)
                elif selected_list[1] == '*':
                    nb_numb = str(int(nb_numb) + 1)
                elif selected_list[2] == '*':
                    nb_char = str(int(nb_char) + 1)
                elif selected_list[3] == '*':
                    alpha_ind = alpha_ind + 1 if alpha_ind < 2 else 0
            elif key.scan_code == 1:  # ESC
                clear_stdin()
                return initial_screen()
            elif key.scan_code == 28:  # ENTER
                if selected_list[4] == '*':
                    pressing = True
                    compressed_data = advanced_screen(ban_alpha=ban_alph, ban_numbers=ban_numb, ban_characters=ban_char)
                    ban_alph = compressed_data[0].copy()
                    ban_numb = compressed_data[1].copy()
                    ban_char = compressed_data[2].copy()
                if selected_list[5] == '*':
                    return result_screen(nb_alpha=nb_alpha, nb_numb=nb_numb, nb_char=nb_char,
                                         alpha_type=alpha_types[alpha_ind][3:-3].lower(), banned_alpha=ban_alph,
                                         banned_numb=ban_numb, banned_characters=ban_char, callback="cs_screen")
        else:
            pressing = False
            clear_stdin()


def advanced_screen(ban_alpha: list, ban_numbers: list, ban_characters: list) -> list[list]:
    clear_stdin()
    pressing = False
    selected_list = "*   "
    ban_numbers = [str(n) for n in ban_numbers] if len(ban_numbers) > 0 else []
    while True:
        str_letters = make_str_from_list(ban_alpha, ", ") if len(ban_alpha) > 0 else "None"
        str_numbers = make_str_from_list(ban_numbers, ", ") if len(ban_numbers) > 0 else "None"
        str_characters = make_str_from_list(ban_characters, ", ") if len(ban_characters) > 0 else "None"
        bigger = len(str_letters) if len(str_letters) >= len(str_numbers) and len(str_letters) >= len(
            str_characters) else len(str_numbers) if len(str_numbers) >= len(str_characters) else len(str_characters)
        print("\033[H\033[J", end="")
        print(f"╔{'═' * 27}╦{'═' * (bigger + 2)}╗")
        print(f"║ [{selected_list[0]}] Banned letters:       ║ {str_letters.center(bigger)} ║")
        print(f"╠{'═' * 27}╬{'═' * (bigger + 2)}╣")
        print(f"║ [{selected_list[1]}] Banned numbers:       ║ {str_numbers.center(bigger)} ║")
        print(f"╠{'═' * 27}╬{'═' * (bigger + 2)}╣")
        print(f"║ [{selected_list[2]}] Banned characters:    ║ {str_characters.center(bigger)} ║")
        print(f"╠{'═' * 27}╩{'═' * (bigger + 2)}╣")
        print(f"║ [{selected_list[3]}] Go back {' ' * (bigger + 17)}║")
        print(f"╚{'═' * (bigger + 30)}╝")
        key = kb.read_event()
        kb.hook(what_is_this_key)
        
        if not pressing:
            if pressed_key_code == 72 and not key.is_keypad:  # UP ARROW
                pressing = True
                selected_list = change_str(selected_list, 0, '') if selected_list[0] != '*' else "   *   "
            elif pressed_key_code == 80 and not key.is_keypad:  # DOWN ARROW
                pressing = True
                selected_list = ' ' + selected_list if selected_list[3] != '*' else "*   "
            elif pressed_key_code == 28:  # ENTER
                pressing = True
                if selected_list[3] == '*':
                    clear_stdin()
                    ban_numbers = [int(n) for n in ban_numbers]
                    return [ban_alpha, ban_numbers, ban_characters]
            elif pressed_key_code == 14:  # BACKSPACE
                pressing = True
                if selected_list[0] == '*':
                    if len(ban_alpha) > 0:
                        ban_alpha.pop(len(ban_alpha) - 1)
                    else:
                        ban_alpha = []
                elif selected_list[1] == '*':
                    if len(ban_numbers) > 0:
                        ban_numbers.pop(len(ban_numbers) - 1)
                    else:
                        ban_numbers = []
                elif selected_list[2] == '*':
                    if len(ban_characters) > 0:
                        ban_characters.pop(len(ban_characters) - 1)
                    else:
                        ban_characters = []

            if selected_list[0] == '*':
                if pressed_key in core.alpha_maj or pressed_key in core.alpha_min:
                    pressing = True
                    if pressed_key not in ban_alpha:
                        ban_alpha.append(pressed_key)
            elif selected_list[1] == '*':
                if pressed_key in core.numbers_str:
                    pressing = True
                    if pressed_key not in ban_numbers:
                        ban_numbers.append(pressed_key)
            elif selected_list[2] == '*':
                if pressed_key in core.characters:
                    pressing = True
                    if pressed_key not in ban_characters:
                        ban_characters.append(pressed_key)
        else:
            pressing = False
            clear_stdin()


def result_screen(callback, size=None, nb_alpha=None, nb_numb=None, nb_char=None, alpha_type="all", banned_alpha=[],
                  banned_numb=[], banned_characters=[]):
    clear_stdin()
    pressing = False
    passwd = core.Password(min_size=size, n_numb=nb_numb, n_alpha=nb_alpha, n_char=nb_char, not_numb=banned_numb,
                           not_alpha=banned_alpha, not_char=banned_characters, alpha_type=alpha_type).generate()
    while True:
        print("\033[H\033[J", end="")
        print(f"╔{'═' * (26 + (7 if len(passwd) < 8 else len(passwd) - 1))}╗")
        print(f"║ Press esc to return to the menu{' ' * (1 if len(passwd) < 8 else len(passwd) - 7)}║")
        print(f"╠{'═' * (26 + (7 if len(passwd) < 8 else len(passwd) - 1))}╣")
        print(f"║ Here is your password: {passwd}{' ' * (9 - len(passwd) if len(passwd) < 8 else 1)}║")
        print(f"║ Press c to copy to clipboard{' ' * (4 if len(passwd) < 8 else len(passwd) - 4)}║")
        print(f"║ Press r to regenerate password{' ' * (2 if len(passwd) < 8 else len(passwd) - 6)}║")
        print(f"║ Press e to edit generation{' ' * (6 if len(passwd) < 8 else len(passwd) - 2)}║")
        print(f"╚{'═' * (26 + (7 if len(passwd) < 8 else len(passwd) - 1))}╝")
        key = kb.read_event()
        if not pressing:
            if key.scan_code == 1:  # ESC
                clear_stdin()
                return initial_screen()
            if key.scan_code == 46:  # C
                pressing = True
                print(copy_to_clipboard(passwd))
            if key.scan_code == 19:  # R
                pressing = True
                clear_stdin()
                passwd = core.Password(min_size=size, n_numb=nb_numb, n_alpha=nb_alpha, n_char=nb_char,
                                       not_numb=banned_numb, not_alpha=banned_alpha, not_char=banned_characters,
                                       alpha_type=alpha_type).generate()
            if key.scan_code == 18:
                match callback:
                    case "ds_screen":
                        return ds_screen(n=str(size))
                    case "cs_screen":
                        return cs_screen(alpha_ind=alpha_type, nb_alpha=nb_alpha, nb_numb=nb_numb, nb_char=nb_char,
                                         ban_alph=banned_alpha, ban_numb=banned_numb, ban_char=banned_characters)
        else:
            pressing = False
            clear_stdin()


def change_str(chain: str, index: int, new_str: str):
    new_chain = ''
    for i in range(len(chain)):
        new_chain += chain[i] if i != index else new_str
    return new_chain


def clear_stdin():
    while msvcrt.kbhit():
        msvcrt.getch()
    sys.stdin.flush()


def make_str_from_list(another_list: list, separator: str):
    string = ''
    for e in another_list:
        string += str(e) + separator
    return string.rstrip(separator)


def what_is_this_key(e):
    global pressed_key, pressed_key_code
    pressed_key, pressed_key_code = f"{e.name}", e.scan_code


def copy_to_clipboard(text: str):
    try:
        # Linux
        if "linux" in sys.platform:
            os.system(f"echo '{text}' | xclip -selection clipboard")

        # Windows
        elif "win" in sys.platform:
            os.system(f"echo {text.strip()} | clip")
            return os.system("msg %USERNAME% Successfully copied to clipboard !")

        # macOS
        elif "darwin" in sys.platform:
            os.system(f"echo '{text}' | pbcopy")

        else:
            return "Unsupported operating system"
    except Exception as e:
        raise f"An error occurred while trying to copy to the clipboard: {e}"


if __name__ == "__main__":
    try:
        initial_screen()
    except Exception as err:
        print("\033[H\033[J", end="")
        print('-' * 50)
        print(f"An error has occurred: {err}.")
        print("Press any key to exit...")
        input('-' * 50)
        exit(1)
