# HostShield · УБИ.099

Учебный Django-компонент `security-service` к ТЗ «Разработка паттерна для обеспечения безопасности приложения при угрозе обнаружения хостов». Веб-страница демонстрирует четыре сценария и расчёт метрики H (число уникальных запрещённых адресов назначения одного источника в одной входной зоне за 10 секунд). При H ≥ 20 отображается проектное решение о временном правиле на 300 секунд.

Это имитация на заранее заданных событиях. Она не сканирует сеть, не изменяет правила межсетевого экрана и не доказывает фактическую блокировку.

## Запуск в Replit

Replit устанавливает `requirements.txt`; команда запуска указана в `.replit`. После запуска открыть Preview. Для непубличного учебного стенда рекомендуется задать `DJANGO_SECRET_KEY` в Secrets.

## Локальная проверка

```bash
python -m pip install -r requirements.txt
python manage.py migrate
python manage.py test
python manage.py runserver
```

## Структура

- `security_console/detector.py` — функция оценки событий по F04/F05;
- `security_console/views.py` — четыре учебных сценария и Django-представление;
- `security_console/urls.py` — маршруты;
- `security_console/templates/security_console/index.html` — веб-интерфейс;
- `security_console/tests.py` — проверки порога, повторов, зоны и страницы.
