# Internal modules
import sys
import os

# Project modules
import core

# Externals modules
import keyboard as kb
import msvcrt

digits_key_hashmap = {
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
                if selected_list[0] != '*':
                    selected_list = change_str(selected_list, 0, '')
            elif key.scan_code == 80 and not key.is_keypad:  # DOWN ARROW
                pressing = True
                if selected_list[2] != '*':
                    selected_list = ' ' + selected_list
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


def ds_screen():
    clear_stdin()
    n = '0'
    pressing = False
    while True:
        print("\033[H\033[J", end="")
        print(f"╔{'═' * 23}╦{'═' * (len(n) + 2)}╗")
        print(f"║ Size of the password: ║ {n} ║")
        print(f"╚{'═' * 23}╩{'═' * (len(n) + 2)}╝")
        key = kb.read_event()
        if not pressing:
            if key.scan_code in digits_key_hashmap and key.is_keypad:  # KEYPAD NUMBERS
                pressing = True
                n = n + digits_key_hashmap[key.scan_code] if int(n) > 0 else digits_key_hashmap[key.scan_code]
            elif key.scan_code == 14:  # BACKSPACE
                pressing = True
                n = change_str(n, len(n) - 1, '') if len(n) > 1 else '0'
            elif key.scan_code == 28 and int(n) > 0:  # ENTER
                return result_screen(size=int(n))
            elif key.scan_code == 1:  # ESC
                clear_stdin()
                return initial_screen()
        else:
            pressing = False
            clear_stdin()


def cs_screen():
    clear_stdin()
    pressing = False
    alpha_types = ["<- All ->", "<- Uppercase ->", "<- Lowercase ->"]
    alpha_ind = 0
    nb_alpha = '0'
    nb_numb = '0'
    nb_char = '0'
    selected_list = "*    "

    while True:
        bigger = len(alpha_types[alpha_ind]) if len(alpha_types[alpha_ind]) >= len(nb_alpha) and len(
            alpha_types[alpha_ind]) >= len(nb_numb) and len(alpha_types[alpha_ind]) >= len(nb_char) else len(
            nb_alpha) if len(nb_alpha) >= len(nb_numb) and len(nb_alpha) >= len(nb_char) else len(nb_numb) if len(
            nb_numb) >= len(nb_char) else len(nb_char)
        print("\033[H\033[J", end="")
        print(f"╔{'═' * 27}╦{'═' * (bigger + 2)}╗")
        print(f"║ [{selected_list[0]}] Number of letters:    ║ {nb_alpha.center(bigger)} ║")
        print(f"╠{'═' * 27}╬{'═' * (bigger + 2)}╣")
        print(f"║ [{selected_list[1]}] Number of numbers:    ║ {nb_numb.center(bigger)} ║")
        print(f"╠{'═' * 27}╬{'═' * (bigger + 2)}╣")
        print(f"║ [{selected_list[2]}] Number of characters: ║ {nb_char.center(bigger)} ║")
        print(f"╠{'═' * 27}╬{'═' * (bigger + 2)}╣")
        print(f"║ [{selected_list[3]}] Type of letters:      ║ {alpha_types[alpha_ind].center(bigger)} ║")
        print(f"╠{'═' * 27}╩{'═' * (bigger + 2)}╣")
        print(f"║ [{selected_list[4]}] Generate password {' ' * (bigger + 7)}║")
        print(f"╚{'═' * (bigger + 30)}╝")
        key = kb.read_event()

        if not pressing:
            if key.scan_code == 72 and not key.is_keypad:  # UP ARROW
                pressing = True
                if selected_list[0] != '*':
                    selected_list = change_str(selected_list, 0, '')
            elif key.scan_code == 80 and not key.is_keypad:  # DOWN ARROW
                pressing = True
                if selected_list[4] != '*':
                    selected_list = ' ' + selected_list
            elif key.scan_code in digits_key_hashmap and key.is_keypad:  # KEYPAD NUMBERS
                pressing = True
                if selected_list[0] == '*':
                    nb_alpha = nb_alpha + digits_key_hashmap[key.scan_code] if int(nb_alpha) > 0 else \
                    digits_key_hashmap[key.scan_code]
                elif selected_list[1] == '*':
                    nb_numb = nb_numb + digits_key_hashmap[key.scan_code] if int(nb_numb) > 0 else digits_key_hashmap[
                        key.scan_code]
                elif selected_list[2] == '*':
                    nb_char = nb_char + digits_key_hashmap[key.scan_code] if int(nb_char) > 0 else digits_key_hashmap[
                        key.scan_code]
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
                if selected_list[3] == '*':
                    alpha_ind = alpha_ind - 1 if alpha_ind > 0 else 2
            elif key.scan_code == 77:  # RIGHT ARROW
                pressing = True
                print(selected_list)
                if selected_list[3] == '*':
                    print('reached')
                    alpha_ind = alpha_ind + 1 if alpha_ind < 2 else 0
            elif key.scan_code == 1:  # ESC
                clear_stdin()
                return initial_screen()
            elif key.scan_code == 28:
                if selected_list[4] == '*':
                    return result_screen(nb_alpha=nb_alpha, nb_numb=nb_numb, nb_char=nb_char,
                                         alpha_type=alpha_types[alpha_ind][3:-3].lower())
        else:
            pressing = False
            clear_stdin()


def result_screen(size: int = None, nb_alpha=None, nb_numb=None, nb_char=None, alpha_type="all"):
    clear_stdin()
    pressing = False
    passwd = core.Password(min_size=size, n_numb=nb_numb, n_alpha=nb_alpha, n_char=nb_char, not_numb=None,
                           not_alpha=None, not_char=None, alpha_type=alpha_type).generate()
    while True:
        print("\033[H\033[J", end="")
        print(f"╔{'═' * (25 + (7 if len(passwd) < 8 else len(passwd)))}╗")
        print(f"║ Here is your password: {passwd}{' ' * (8 - len(passwd) if len(passwd) < 8 else 1)}║")
        print(f"║ Press c to copy to clipboard{' ' * (3 if len(passwd) < 8 else len(passwd) - 4)}║")
        print(f"║ Press r to regenerate password{' ' * (1 if len(passwd) < 8 else len(passwd) - 6)}║")
        print(f"╚{'═' * (25 + (7 if len(passwd) < 8 else len(passwd)))}╝")
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
                passwd = core.Password(min_size=size, n_numb=nb_numb, n_alpha=nb_alpha, n_char=nb_char, not_numb=None,
                                       not_alpha=None, not_char=None, alpha_type=alpha_type).generate()
        else:
            pressing = False
            clear_stdin()


def change_str(chain: str, index: int, newstr: str):
    newchain = ''
    for i in range(len(chain)):
        newchain += chain[i] if i != index else newstr
    return newchain


def clear_stdin():
    while msvcrt.kbhit():
        msvcrt.getch()
    sys.stdin.flush()


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
        print('-' * (len(str(err)) + 24))
        print(f"An error has occurred: {err}.")
        print("Press any key to exit...")
        input('-' * (len(str(err)) + 24))
        exit(1)
