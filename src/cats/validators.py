import requests
from rest_framework.exceptions import ValidationError


def validate_breed(value: str):
    response = requests.get(f"https://api.thecatapi.com/v1/breeds/search?q={value}")

    if not response.ok:
        raise ValidationError("Breed not found")

    for breed in response.json():
        if value.lower() == breed["name"].lower():
            return value

    raise ValidationError("Breed not found")
