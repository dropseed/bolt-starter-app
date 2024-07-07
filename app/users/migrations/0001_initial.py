# Generated by Plain 5.0.dev20240612160253 on 2024-06-12 21:17

import plain.passwords.models
import plain.passwords.validators
from plain import models
from plain.models import migrations


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="User",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True, primary_key=True, serialize=False
                    ),
                ),
                ("email", models.EmailField(max_length=254, unique=True)),
                (
                    "password",
                    plain.passwords.models.PasswordField(
                        validators=[
                            plain.passwords.validators.MinimumLengthValidator(),
                            plain.passwords.validators.CommonPasswordValidator(),
                            plain.passwords.validators.NumericPasswordValidator(),
                        ]
                    ),
                ),
                ("is_staff", models.BooleanField(default=False)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
