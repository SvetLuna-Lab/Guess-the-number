# src/guess_the_number/game.py
from __future__ import annotations

import builtins
import random
from typing import Callable, Optional

InputFunc = Callable[[str], str]
OutputFunc = Callable[..., None]


def is_valid(s: str, right: int = 100) -> bool:
    return s.isdigit() and 1 <= int(s) <= right


def ask_right_border(input_func: Optional[InputFunc] = None,
                     output_func: Optional[OutputFunc] = None) -> int:
    input_func = builtins.input if input_func is None else input_func
    output_func = print if output_func is None else output_func

    while True:
        s = input_func("Введите правую границу диапазона (натуральное число): ").strip()
        if s.isdigit() and int(s) >= 1:
            return int(s)
        output_func("А может быть все-таки введем натуральное число (>= 1)?")


def ask_play_again(input_func: Optional[InputFunc] = None,
                   output_func: Optional[OutputFunc] = None) -> bool:
    input_func = builtins.input if input_func is None else input_func
    output_func = print if output_func is None else output_func

    while True:
        s = input_func("Хотите сыграть еще раз? (да/нет): ").strip().lower()
        if s in ("да", "д", "yes", "y"):
            return True
        if s in ("нет", "н", "no", "n"):
            return False
        output_func("Введите 'да' или 'нет'.")


def play_one_round(right: int,
                   secret: Optional[int] = None,
                   input_func: Optional[InputFunc] = None,
                   output_func: Optional[OutputFunc] = None) -> int:
    input_func = builtins.input if input_func is None else input_func
    output_func = print if output_func is None else output_func

    secret = random.randint(1, right) if secret is None else secret
    attempts = 0

    while True:
        user_input = input_func(f"Введите число от 1 до {right}: ").strip()
        if not is_valid(user_input, right):
            output_func(f"А может быть все-таки введем целое число от 1 до {right}?")
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
