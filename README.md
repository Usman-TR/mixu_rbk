## РБК

### Разработка программного решения конвертации видео в текст для рекомендательной системы РБК Xavier

«Мы представляем платформу оцифровки видеофайлов в текст».
Платформа позволяет в автоматическом режиме получить видео со стороннего сервиса и перевести его в текстовые данные. После завершения процедуры текст передается рекомендательной системе для персонализации контента. Система выделит аудио, переведет его в текст, распознает текст и, при необходимости, выделит ключевые слова. 
Стек решения: Python, Django, Django Rest Framework, Postgresql, JavaScript, Gensim, Docker, Docker-Compose
Уникальность: полностью автоматическое распознавание видео, наличие дашборда для контроля за эффективностью рекомендаций, выделение тегов, возможность потоковая обработки, возможность поиска таймлайна в видео по распознанному тексту.

### Установка

#### Docker

Перед установкой убедитесь в том что ваша хост машина подерживает виртуализацию, и в том что она включена.

Для Windows: убедитесь в том что у вас включен компонент Hyper-V.

Затем скачайте и установите Docker, Docker-Compose

#### Запуск

Склонируйте репорзиторий к себе!

Для запуска программы используйте:

Команду  docker compose up --build

Приложение доступно по адресу http://127.0.0.1:8000/

#### REST API

Первый endpoint http://127.0.0.1:8000/api/videos_list/ для отображения всех распознанных/обработанных видео.

Второй endpoint http://127.0.0.1:8000/api/video_recognize/ для распознования и обработки видео который возвращает JSON. Принимает post запрос, в теле запроса надо передать {'video': сам_видео_файл}

Придется чуть чуть подождать, нейронка мощная)