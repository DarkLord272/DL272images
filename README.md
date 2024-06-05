# DL272images

Проект DL272images предназначен для обработки и изменения изображений.

## Установка и запуск

1. Откройте проект в PyCharm.
2. Откройте терминал в PyCharm.
3. При необходимости установите все пакеты из requirements.txt.
     ```bash
    pip install <packet_name>
    ``` 
4. Перейдите в директорию imageconverter:
    ```bash
    cd imageconverter
    ```
5. Запустите сервер командой:
    ```bash
    python manage.py runserver
    ```

После выполнения этих шагов сайт будет доступен по адресу [127.0.0.1:8000](http://127.0.0.1:8000).

## Работа с API
### Для того, чтобы взаимодействовать с сайтом в автоматизированном режиме, вы можете использовать curl

### Примеры:

Получение обработанного изображения
```bash
curl -X POST http://localhost:8000/api/resize/ -F image=@C:/test/path/image.png -F left=1 -F right=150 -F top=1 -F bottom=150 -F wnsize=300 -F hnsize=300
```
На этот запрос будет прислан ответ в формате:

{
  "output_image": "base64 code"
}
