# service/signals.py

import os
from django.contrib.auth import get_user_model
from django.db.models.signals import post_migrate
from django.dispatch import receiver

@receiver(post_migrate)
def create_superuser(sender, **kwargs):
    if os.getenv("CREATE_SUPERUSER") == "True":
        User = get_user_model()
        username = os.getenv("DJANGO_SUPERUSER_USERNAME")
        email = os.getenv("DJANGO_SUPERUSER_EMAIL")
        password = os.getenv("DJANGO_SUPERUSER_PASSWORD")

        if username and not User.objects.filter(username=username).exists():
            print("✅ Creating superuser...")
            User.objects.create_superuser(username=username, email=email, password=password)
        else:
            print("⚠️ Superuser already exists or username not provided.")
    # At the end of your signal or post_migrate handler
    print("🧪 Existing superusers:", User.objects.filter(is_superuser=True))
