# src/guess_the_number/game.py
from __future__ import annotations

import random
from typing import Callable, Optional


def is_valid(s: str, right: int = 100) -> bool:
    """Return True if s is an integer string in [1, right]."""
    if not s.isdigit():
        return False
    n = int(s)
    return 1 <= n <= right


def ask_right_border(
    input_func: Optional[Callable[[str], str]] = None,
    output_func: Optional[Callable[..., None]] = None,
) -> int:
    """Ask user for the right border n (natural number)."""
    import builtins

    if input_func is None:
        input_func = builtins.input
    if output_func is None:
        output_func = print

    while True:
        s = input_func("Введите правую границу диапазона (натуральное число): ").strip()
        if s.isdigit() and int(s) >= 1:
            return int(s)
        output_func("А может быть все-таки введем натуральное число?")


def ask_play_again(
    input_func: Optional[Callable[[str], str]] = None,
    output_func: Optional[Callable[..., None]] = None,
) -> bool:
    """Ask user if they want to play again."""
    import builtins

    if input_func is None:
        input_func = builtins.input
    if output_func is None:
        output_func = print

    while True:
        s = input_func("Хотите сыграть еще раз? (да/нет): ").strip().lower()
        if s in ("да", "д", "y", "yes"):
            return True
        if s in ("нет", "н", "n", "no"):
            return False
        output_func("Пожалуйста, ответьте 'да' или 'нет'.")


def play_one_round(
    right: int,
    secret: int,
    input_func: Optional[Callable[[str], str]] = None,
    output_func: Optional[Callable[..., None]] = None,
) -> int:
    """Play a single round. Returns attempts count."""
    import builtins

    if input_func is None:
        input_func = builtins.input
    if output_func is None:
        output_func = print

    attempts = 0
    while True:
        user_input = input_func(f"Введите число от 1 до {right}: ").strip()
        if not is_valid(user_input, right):
            output_func("А может быть все-таки введем целое число от 1 до 100?")
            continue

        guess = int(user_input)
        attempts += 1

        if guess < secret:
            output_func("Ваше число меньше загаданного, попробуйте еще разок")
        elif guess > secret:
            output_func("Ваше число больше загаданного, попробуйте еще разок")
        else:
            output_func("Вы угадали, поздравляем!")
            return attempts


def run_game(
    input_func: Optional[Callable[[str], str]] = None,
    output_func: Optional[Callable[..., None]] = None,
) -> None:
    """Main entrypoint for the game (can be tested with injected I/O)."""
    import builtins

    if input_func is None:
        input_func = builtins.input
    if output_func is None:
        output_func = print

    output_func("Добро пожаловать в числовую угадайку")

    while True:
        right = ask_right_border(input_func=input_func, output_func=output_func)
        secret = random.randint(1, right)
        attempts = play_one_round(right, secret, input_func=input_func, output_func=output_func)
        output_func(f"Количество попыток: {attempts}")

        if not ask_play_again(input_func=input_func, output_func=output_func):
            output_func("Спасибо, что играли в числовую угадайку. Еще увидимся...")
            break
