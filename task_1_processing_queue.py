from queue import Queue
import time
import random

# Створення черги 
request_queue = Queue()
# Глобальна змінна для генерації унікальних id
request_counter = 0

# Генерація нової заявки -> до черги
def generate_request():
    
    global request_counter
    # Випадкове надходження заявок
    if random.choice([True, False]):
        request_counter += 1
        request_data = f"Заявка №{request_counter}"
        request_queue.put(request_data)
        print(f"Додано заявку: {request_data}")

# Обробка заявки і видалення з черги
def process_request():
    
    if not request_queue.empty():
        current_request = request_queue.get()
        print(f"Обробка заявки: {current_request}")
        
        # Затримка на обробку
        time.sleep(2)
        print(f"Заявку {current_request} оброблено.\n")
        # Затримка 
        # time.sleep(2)
    else:
        print("Черга пуста\n")
        # Затримка
        time.sleep(1)
        
# Головний блок виконання програми
if __name__ == "__main__":
    
    print("\n\nОбробка заявок запущена (Ctrl+C - вихід).\n")
    
    try:
        # Головний цикл програми виконується тут
        while True:
            # Створення нових заявок
            generate_request()
            
            # Обробка заявок
            process_request()
            
            # Затримка 
            # time.sleep(1)

    except KeyboardInterrupt:
        # Переривання обробки користувачем
        print("\nРоботу черги завершено.")
