#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
from kernel.settings import base


def main():
    """Run administrative tasks."""
    status = base.DEBUG
    if status == 'True':
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "kernel.settings.development")
    elif status == 'False':
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "kernel.settings.production")
    else:
        raise ValueError("Unknown status you should set it throught the environment variables.")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()
