import os
import shutil
import re

# Абсолютный путь к скрипту
cur_dir = os.path.dirname(__file__)

# Исходная папка находится рядом с папкой python
src_dir = os.path.abspath(os.path.join(cur_dir, '..', 'patt'))

# Корневая папка (там где лежат папки 01, 02, ..., 45)
root_dir = os.path.abspath(os.path.join(cur_dir, '..'))

# Регулярное выражение для поиска номеров
file_re = re.compile(r'pattern-(\d+)\.(patt|png)$')

print("Исходная папка:", src_dir)
print("Целевая папка:", root_dir)

for fname in os.listdir(src_dir):
    match = file_re.match(fname)
    if match:
        num = match.group(1)
        ext = match.group(2)
        target_dir = os.path.join(root_dir, num.zfill(2), 'qr')
        os.makedirs(target_dir, exist_ok=True)
        src_file = os.path.join(src_dir, fname)
        dst_file = os.path.join(target_dir, fname)
        shutil.copy2(src_file, dst_file)
        print(f"Скопировано: {src_file} -> {dst_file}")

print("Готово.")
