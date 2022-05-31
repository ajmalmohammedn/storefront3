from django.core.validators import ValidationError


def validate_file_size(file):
    max_file_size = 50
    if file.size > max_file_size * 1024:
        raise ValidationError(f'Files cannot be larger than {max_file_size}kb!')