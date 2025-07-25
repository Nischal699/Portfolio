import os
from django.contrib.auth import get_user_model
from django.db.models.signals import post_migrate
from django.dispatch import receiver

@receiver(post_migrate)
def create_or_update_superuser(sender, **kwargs):
    if sender.label != "auth":
        return

    User = get_user_model()

    if os.getenv("CREATE_SUPERUSER") == "True":
        username = os.getenv("DJANGO_SUPERUSER_USERNAME")
        email = os.getenv("DJANGO_SUPERUSER_EMAIL")
        password = os.getenv("DJANGO_SUPERUSER_PASSWORD")

        if not username:
            print("❌ DJANGO_SUPERUSER_USERNAME not set in env")
            return

        try:
            user = User.objects.get(username=username)
            updated = False
            if not user.is_superuser or not user.is_staff:
                user.is_superuser = True
                user.is_staff = True
                updated = True
            # Update password every time on deploy — careful with this in prod!
            user.set_password(password)
            updated = True

            if updated:
                user.save()
                print(f"🔄 Updated existing superuser '{username}' with new password and flags.")
            else:
                print(f"✅ Superuser '{username}' already up-to-date.")

        except User.DoesNotExist:
            User.objects.create_superuser(username=username, email=email, password=password)
            print(f"✅ Created new superuser '{username}'.")

    print("🧪 Existing superusers:", User.objects.filter(is_superuser=True))
