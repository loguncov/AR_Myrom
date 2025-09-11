import os
import re

COMMON_FILES = ['gesture-handler.js', 'gesture-detector.js', 'styles.css']
ROOT = os.path.dirname(os.path.abspath(__file__))

# Проверка, что папка — только цифры
is_target_folder = lambda name: name.isdigit()

# Обновление html-файлов
def update_html_file(file_path):
    if not os.path.exists(file_path):
        return
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    orig = content
    # Заменить подключения стилей
    content = re.sub(r'<link rel="stylesheet" href="styles.css"\s*/?>', '<link rel="stylesheet" href="../common/styles.css">', content)
    # Заменить подключения gesture-detector.js и gesture-handler.js
    content = re.sub(r'<script src="gesture-detector.js"></script>', '<script src="../common/gesture-detector.js"></script>', content)
    content = re.sub(r'<script src="gesture-handler.js"></script>', '<script src="../common/gesture-handler.js"></script>', content)
    # Для self-closing <script ... />
    content = re.sub(r'<script src="gesture-detector.js"\s*/>', '<script src="../common/gesture-detector.js" />', content)
    content = re.sub(r'<script src="gesture-handler.js"\s*/>', '<script src="../common/gesture-handler.js" />', content)
    if content != orig:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)

# Удаление файлов и обновление html
for name in os.listdir(ROOT):
    folder = os.path.join(ROOT, name)
    if os.path.isdir(folder) and is_target_folder(name):
        # Удалить дублирующие js/css
        for fname in COMMON_FILES:
            fpath = os.path.join(folder, fname)
            if os.path.exists(fpath):
                os.remove(fpath)
        # Обновить index.html и image-tracking.html
        update_html_file(os.path.join(folder, 'index.html'))
        update_html_file(os.path.join(folder, 'image-tracking.html'))
        print(f'Обработана папка: {name}')
print('Готово! Все папки обработаны.')
