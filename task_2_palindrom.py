from collections import deque

# Перевирка на паліндром
def is_palindrome(text):
    
    # Робимо все lower та видаляємо пробіли
    processed_text = text.lower().replace(" ", "")
    
    # Створення deque та додавання туди символів
    char_deque = deque(processed_text)
    
    # Порівняння символів з обох боків
    # Доки в черзі > 1 символу
    while len(char_deque) > 1:
        # Беремо і порівнюємо символів в deque зліва та зправа
        if char_deque.popleft() != char_deque.pop():
            return False # Символи не збігаються — не паліндром
            
    # Якщо успіх - паліндром
    return True

if __name__ == "__main__":
    
    test_cases = [
        "Я несу гусеня",  # пробіли та різні регістри
        "ротатор",        # непарна кількість
        "Abba",           # парна кількість
        "Python",         # Не паліндром
        "12321",          # цифри
    ]

    for string in test_cases:
        result = is_palindrome(string)
        status = "Паліндром" if result else "Не паліндром"
        print(f"{string:<15} -> {status}")
    