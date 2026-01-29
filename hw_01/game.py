import numpy as np

def game_core_v3(number):
    """Угадываем число бинарным поиском
    
    Загадываем число и пытаемся его угадать за минимальное количество попыток:
        number (int): Загаданное число от 1 до 100
    
    Возвращаем:
        int: Количество попыток
    """
    count = 0
    low = 1
    high = 100
    
    while True:
        count += 1
        # Берём середину диапазона
        predict = (low + high) // 2
        
        if predict == number:
            return count  # Угадали!
        elif predict < number:
            low = predict + 1  # Число больше
        else:
            high = predict - 1  # Число меньше

def score_game(game_core):
    """Запускаем игру 1000 раз, чтобы узнать среднее количество попыток"""
    count_ls = []
    np.random.seed(1)  # генерация повторяемых случайных чисел
    random_array = np.random.randint(1, 101, size=1000)
    
    for number in random_array:
        count_ls.append(game_core(number))
    
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return score

# Запускаем проверку
score_game(game_core_v3)