import numpy as np

def linear(x, w, b):
    # [m, in] * [in, out] + [out] -> [m, out]
    return x @ w + b  # @ означает матричное умножение в Python

def gelu(x):
    # Gaussian Error Linear Unit (GELU)
    return 0.5 * x * (1 + np.tanh(np.sqrt(2 / np.pi) * (x + 0.044715 * np.power(x, 3))))

def ffn(x, c_fc, c_proj):
    # Применение первого линейного слоя
    hidden = linear(x, c_fc['w'], c_fc['b'])
    # Применение GELU
    hidden = gelu(hidden)
    # Применение второго линейного слоя
    return linear(hidden, c_proj['w'], c_proj['b'])

# # Пример использования
# x = np.array([[1.0, 2.0], [3.0, 4.0]])  # Пример входных данных
# c_fc = {'w': np.array([[1.0, 2.0], [3.0, 4.0]]), 'b': np.array([1.0, 1.0])}  # Веса и смещение для первого линейного слоя
# c_proj = {'w': np.array([[1.0, 2.0], [3.0, 4.0]]), 'b': np.array([1.0, 1.0])}  # Веса и смещение для второго линейного слоя
#
# output = ffn(x, c_fc, c_proj)
# print(output)


# Для реализации функций linear, gelu и ffn, нам нужно точно понимать, что каждая из них делает:
#
# Линейный слой (linear): Это просто матричное умножение входных данных x на матрицу весов w, плюс добавление смещения b. Формула: x * w + b.
#
# Функция активации GELU (gelu): GELU (Gaussian Error Linear Unit) — это нелинейная функция активации, которая используется для моделирования стохастических шлюзов.
# Она определяется как: x * Φ(x), где Φ(x) — это кумулятивное распределение стандартного нормального распределения.
#
# Feed-Forward Network (ffn): FFN проектирует входные эмбеддинги x в новое пространство с помощью линейного слоя c_fc, применяет нелинейное преобразование (в данном случае GELU), и затем проектирует обратно с помощью другого линейного слоя c_proj.
#
