from datasets import load_dataset

dataset = load_dataset('json', data_files='dataset.jsonl')
# print(dataset['train'][:10])  # Вывести первую строку
def transform_to_prompt_completion(example):
    return {
        "prompt": example["question"],   # Используем поле "question" как "prompt"
        "completion": example["answer"]  # Используем поле "answer" как "completion"
    }

# Применяем трансформацию к каждому элементу датасета
transformed_dataset = dataset.map(transform_to_prompt_completion)

# Удаляем старые поля, если они больше не нужны
transformed_dataset = transformed_dataset.remove_columns(["question", "answer", "relevance"])

# Проверяем результат
print(transformed_dataset['train'][:5])
transformed_dataset['train'].to_json('transformed_dataset.jsonl', orient='records', lines=True)

