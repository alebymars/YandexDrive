import sys

import allure
import pytest

sys.path.append("./src")

from MainRtriangle import Rtriangle


def get_rtriangle() -> Rtriangle:
    return Rtriangle(0, 0, 0, 3, 4, 0)


@allure.title("Прямоугольный треугольник")
@allure.description(
    "Тест проверяет, возвращает ли get_rtriangle() прямоугольный треугольник."
)
@allure.tag("Func")
@allure.label("owner", "Alexandr Voronkov")
def test_get_rtriangle():

    x1 = get_rtriangle().x1
    y1 = get_rtriangle().y1
    x2 = get_rtriangle().x2
    y2 = get_rtriangle().y2
    x3 = get_rtriangle().x3
    y3 = get_rtriangle().y3

    with allure.step(f"Вычисляем значение для стороны A"):
        a = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
    with allure.step(f"Вычисляем значение для стороны B"):
        b = ((x3 - x2) ** 2 + (y3 - y2) ** 2) ** 0.5
    with allure.step(f"Вычисляем значение для стороны C"):
        c = ((x1 - x3) ** 2 + (y1 - y3) ** 2) ** 0.5

    sides = [a, b, c]
    sides.sort()

    expected_result = sides[2] ** 2 == (sides[0] ** 2 + sides[1] ** 2)

    try:
        assert expected_result, "Треугольник является прямоугольным"
        allure.attach(f"Треугольник является прямоугольным", "Результаты:")
    except AssertionError as e:
        assert expected_result, "Треугольник не является прямоугольным"
        allure.attach(
            f"{e}?",
            "Результаты:",
        )
