import re

def transform_name(full_name):
    return re.sub(r'\b(\w+)\s+(\w)\w*\s+(\w)\w*\b', r'\1 \2. \3.', full_name)

# Пример использования
full_name = "Иванов Петр Алексеевич"
transformed_name = transform_name(full_name)
print(transformed_name)  # Выведет: Иванов П. А.