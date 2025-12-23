import builtins
import guess_the_number.game as g


def test_is_valid():
    assert g.is_valid("1", 100) is True
    assert g.is_valid("100", 100) is True
    assert g.is_valid("0", 100) is False
    assert g.is_valid("101", 100) is False
    assert g.is_valid("-5", 100) is False
    assert g.is_valid("1.2", 100) is False
    assert g.is_valid("abc", 100) is False


def test_play_one_round_attempts(monkeypatch, capsys):
    # secret=7, right=10
    # вводы: некорректный, затем 3 (valid), 9 (valid), 7 (valid)
    inputs = iter(["-1", "3", "9", "7"])
    monkeypatch.setattr(builtins, "input", lambda prompt="": next(inputs))

    attempts = g.play_one_round(10, 7)
    out = capsys.readouterr().out

    assert attempts == 3
    assert "целое число от 1 до 10" in out
    assert "меньше загаданного" in out
    assert "больше загаданного" in out
    assert "Вы угадали, поздравляем!" in out


def test_ask_right_border(monkeypatch, capsys):
    inputs = iter(["0", "abc", "15"])
    monkeypatch.setattr(builtins, "input", lambda prompt="": next(inputs))
    n = g.ask_right_border()
    out = capsys.readouterr().out

    assert n == 15
    assert "натуральное число" in out


def test_ask_play_again(monkeypatch, capsys):
    inputs = iter(["maybe", "да"])
    monkeypatch.setattr(builtins, "input", lambda prompt="": next(inputs))
    assert g.ask_play_again() is True
    out = capsys.readouterr().out
    assert 'Введите "да" или "нет".' in out

    inputs = iter(["нет"])
    monkeypatch.setattr(builtins, "input", lambda prompt="": next(inputs))
    assert g.ask_play_again() is False
