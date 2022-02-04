import numpy as np

def random_predict(number:int) -> int:
    """Угадываем число случайным образом

    Args:
        number (int, optional): Загаданное целое число от 1 до 100

    Returns:
        int: Количество попыток
    """
    count = 0
    min_value = 1    #Инициализируем минимально возможное загаданное число
    max_value = 101  #Инициализируем максимально возможное загаданное число + 1
    
    while True:
        count += 1 
        
        # Используем дихотомию
        predict_number = (min_value + max_value) // 2 
        
        if number == predict_number:
            break
        
        elif number > predict_number:
            min_value = predict_number
        else:
            max_value = predict_number
        
        
    return(count)


def score_game(random_predict) -> int:
    """За какое количество попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция для отгадывания

    Returns:
        int: Среднее количество попыток
    """
    count_ls = []
    np.random.seed(1) # Фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size = 1000) # Загадываем список чисел
    
    for number in random_array:
        count_ls.append(random_predict(number))       
        
    score = int(np.mean(count_ls)) # Высчитываем среднее
    
    print(f"Алгоритм угадывает число в среднем за {score} попыток")
    return(score)

#Запуск программы
if __name__ == '__main__':
    score_game(random_predict)