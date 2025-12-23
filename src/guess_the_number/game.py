import random
from typing import Callable


def is_valid(text: str, right: int) -> bool:
    """True, если text — целое число в диапазоне 1..right."""
    return text.isdigit() and 1 <= int(text) <= right


def ask_right_border(
    input_func: Callable[[str], str] = input,
    print_func: Callable[..., None] = print,
) -> int:
    """Запрашивает правую границу n (натуральное число >= 1)."""
    while True:
        s = input_func("Введите правую границу диапазона (натуральное число): ").strip()
        if s.isdigit() and int(s) >= 1:
            return int(s)
        print_func("А может быть все-таки введем натуральное число?")


def ask_play_again(
    input_func: Callable[[str], str] = input,
    print_func: Callable[..., None] = print,
) -> bool:
    """Спрашивает, играть ли ещё раз."""
    while True:
        s = input_func("Хотите сыграть еще раз? (да/нет): ").strip().lower()
        if s in ("да", "д", "yes", "y"):
            return True
        if s in ("нет", "н", "no", "n"):
            return False
        print_func('Введите "да" или "нет".')


def play_one_round(
    right: int,
    secret: int,
    input_func: Callable[[str], str] = input,
    print_func: Callable[..., None] = print,
) -> int:
    """
    Один раунд угадывания.
    Возвращает количество попыток (считаются только корректные вводы).
    """
    attempts = 0
    while True:
        user_input = input_func(f"Введите число от 1 до {right}: ").strip()

        if not is_valid(user_input, right):
            print_func(f"А может быть все-таки введем целое число от 1 до {right}?")
            continue

        guess = int(user_input)
        attempts += 1

        if guess < secret:
            print_func("Ваше число меньше загаданного, попробуйте еще разок")
        elif guess > secret:
            print_func("Ваше число больше загаданного, попробуйте еще разок")
        else:
            print_func("Вы угадали, поздравляем!")
            return attempts


def run_game() -> None:
    print("Добро пожаловать в числовую угадайку")

    while True:
        right = ask_right_border()
        secret = random.randint(1, right)

        attempts = play_one_round(right, secret)
        print(f"Количество попыток: {attempts}")

        if not ask_play_again():
            print("Спасибо, что играли в числовую угадайку. Еще увидимся...")
            break


if __name__ == "__main__":
    run_game()
