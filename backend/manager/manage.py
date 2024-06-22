#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
from concurrent.futures import ThreadPoolExecutor


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'manager.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)

    def run_django():
        execute_from_command_line(sys.argv)

    def run_telegram_bot():
        import echo_bot
        echo_bot.main()

    with ThreadPoolExecutor(max_workers=2) as executor:
        executor.submit(run_django)
        executor.submit(run_telegram_bot)

if __name__ == '__main__':
    main()
