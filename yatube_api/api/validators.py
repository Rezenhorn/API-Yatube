from rest_framework.serializers import ValidationError


class UniqueFieldsValidator:
    """Валидатор уникальности значения полей."""
    def __init__(self, fields):
        self.fields = fields

    def __call__(self, value):
        try:
            fields_values = [value[var] for var in self.fields]
        except KeyError as error:
            raise KeyError(f'Поля {error} не существует.')
        if len(self.fields) != len(set(fields_values)):
            raise ValidationError('Ошибка валидации.')
        return value
