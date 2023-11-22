import math


def calculate_lower_bound(V, T, P):
    """
    Вычисляет нижнюю границу числа всевозможных паролей (S*).
    """
    S_star = math.ceil(V * T / P)
    return S_star


def find_alphabet_and_length(V, T, P, A_min=2, A_max=100, L_max=100):
    """
    Находит минимальные мощность алфавита паролей (A) и длину паролей (L),
    обеспечивающие вероятность подбора пароля злоумышленником не более P,
    при скорости подбора паролей V, максимальном сроке действия пароля T.
    """
    S_star = calculate_lower_bound(V, T, P)

    for A in range(A_min, A_max + 1):
        for L in range(1, L_max + 1):
            S = A ** L
            if S >= S_star:
                return A, L

    return None, None


# Заданные параметры
V = 10  # скорость перебора паролей (паролей в минуту)
T = 3 * 7 * 24 * 60  # максимальный срок действия пароля (в минутах)
P = 1e-4  # вероятность подбора пароля

# Решение задачи
A, L = find_alphabet_and_length(V, T, P)

# Вывод результата
if A is not None and L is not None:
    print(f"Минимальная мощность алфавита паролей: {A}")
    print(f"Минимальная длина паролей: {L}")
else:
    print("Решение не найдено. Увеличьте диапазон поиска.")
