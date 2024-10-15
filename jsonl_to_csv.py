import json
import csv

# Открываем JSONL и CSV файлы
with open('transformed_dataset.jsonl', 'r', encoding='utf-8') as jsonl_file, open('../output.csv', 'w', newline='',
                                                                                  encoding='utf-8') as csv_file:
    # Определяем поле заголовка для CSV файла
    fieldnames = ['prompt', 'completion']  # Укажите нужные поля

    # Создаем writer для CSV
    csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

    # Записываем заголовки в CSV файл
    csv_writer.writeheader()

    # Читаем каждую строку из JSONL файла
    for line in jsonl_file:
        # Преобразуем строку JSON в словарь
        json_obj = json.loads(line)

        # Записываем словарь в CSV файл
        csv_writer.writerow(json_obj)

print("Конвертация завершена.")
