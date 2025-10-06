# AR_WEB_Myrom

Веб-приложение дополненной реальности для сканирования QR-кодов и просмотра 3D моделей через камеру устройства. Построено на A-Frame и AR.js, содержит 45 AR-сцен с уникальными маркерами.

## 🚀 Демо

**Живая версия:** `https://[username].github.io/[repository-name]/`

> После деплоя на GitHub Pages замените ссылку выше на актуальный URL

## Возможности

- **45 AR-сцен** - каждая с уникальным QR-маркером и 3D моделью
- **Marker Tracking** - отслеживание по паттернам QR-кодов
- **Image Tracking** - поддержка NFT (Natural Feature Tracking)
- **Управление жестами** - вращение (1 палец) и масштабирование (2 пальца)
- **Модульная архитектура** - общие скрипты в `common/`

## Быстрый старт

### Онлайн
1. Откройте демо-ссылку на мобильном устройстве
2. Разрешите доступ к камере
3. Выберите AR-сцену из главного меню
4. Наведите камеру на QR-код
5. Управляйте моделью жестами

### Локально
```bash
# Откройте index.html в браузере
open index.html
```

## Требования

- Современный браузер с WebXR
- HTTPS соединение (для доступа к камере)
- Мобильное устройство (рекомендуется)

## Структура проекта

```
/
├── index.html              # Главная страница навигации
├── common/                 # Общие ресурсы
│   ├── gesture-detector.js
│   ├── gesture-handler.js
│   └── styles.css
├── 01/ ... 45/             # AR-сцены
│   ├── index.html
│   ├── image-tracking.html
│   ├── obj/                # 3D модели (GLTF)
│   └── qr/                 # QR паттерны
└── cleanup_ar_folders.py   # Утилита обслуживания
```

## Деплой на GitHub Pages

### Настройка автоматического развертывания:

1. Отправьте код на GitHub:
   ```bash
   git add .
   git commit -m "Deploy to GitHub Pages"
   git push origin main
   ```

2. В настройках репозитория:
   - **Settings** → **Pages**
   - **Source**: выберите **"GitHub Actions"**

3. Готово! Каждый коммит автоматически обновит сайт  
   Следите за процессом во вкладке **Actions**

## Разработка

### Добавление новой сцены

1. Создайте папку (например, `46/`)
2. Добавьте 3D модель в `46/obj/`
3. Добавьте QR паттерн в `46/qr/`
4. Скопируйте `index.html` и `image-tracking.html` из любой сцены
5. Подключите общие скрипты:

```html
<link rel="stylesheet" href="../common/styles.css">
<script src="../common/gesture-detector.js"></script>
<script src="../common/gesture-handler.js"></script>
```

6. Обновите главную страницу `index.html`

### Автоматизация

```bash
python cleanup_ar_folders.py
```

Скрипт удаляет дублирующиеся файлы и обновляет подключения к общим модулям.

## Технологии

- [A-Frame 1.0.4](https://aframe.io/) - VR/AR фреймворк
- [AR.js 3.4.7](https://ar-js-org.github.io/AR.js-Docs/) - AR библиотека
- GLTF - формат 3D моделей
- GitHub Actions - CI/CD

## Документация

- [DEVELOPER.md](DEVELOPER.md) - для разработчиков
- [replit.md](replit.md) - настройка Replit

## Лицензия

См. [LICENSE](LICENSE)

---

Вопросы и предложения - через Issues на GitHub
