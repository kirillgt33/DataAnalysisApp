# Проверка на float число
def is_numeric_with_dots(s):
    # Удаляем точки, проверяем, состоит ли строка из чисел,
    # затем восстанавливаем точки, если они были в оригинальной строке
    s_without_dots = s.replace('.', '')
    is_numeric = s_without_dots.isdigit()
    return is_numeric and (s.count('.') <= 1)