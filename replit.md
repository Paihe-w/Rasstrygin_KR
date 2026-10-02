# HostShield

## Scope
Keep the imported Django structure and stack. This is a Russian-language educational simulation, not a network scanner or firewall controller.

## Running on Replit
- Click Run to start the `Start application` workflow.
- Command: `python manage.py migrate --noinput && python manage.py runserver 0.0.0.0:5000`.
- Open Preview to see the dashboard and try its four scenario buttons.
- Dependencies are declared in `requirements.txt`.
- SQLite stores Django sessions locally in the ignored `db.sqlite3`.
- Django uses `DJANGO_SECRET_KEY` when supplied, otherwise the existing `SESSION_SECRET` workspace secret. Never print these values.
- Development mode allows embedding in Replit Preview; production mode (`DJANGO_DEBUG=0`) retains Django's clickjacking protection.

## Verification
Run `python manage.py check` and `python manage.py test`.

## Deployment boundary
The configured server is for development only. Before public production use, configure a production WSGI server, disable debug mode, and review host/CSRF settings and database persistence.