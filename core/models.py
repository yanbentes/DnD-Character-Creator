from django.db import models
from django.conf import settings

# django tem objeto User pra login
# https://docs.djangoproject.com/en/4.1/topics/auth/default/

# precisa relacionar as classes
# documentacao de models https://docs.djangoproject.com/en/4.1/topics/db/models/

# depois de modificar as classes
# python3 manage.py makemigrations
# python3 manage.py migrate


class Character(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, unique=True)

    class Race(models.TextChoices):
        Human = 'Human'
        Orc = 'Orc'
        Elf = 'Elf'
        Centaur = 'Centaur'
        Dragonborn = 'Dragonborn'
        Dwarf = 'Dwarf'
        Hobbit = 'Hobbit'

    race = models.CharField(max_length=10, choices=Race.choices, default='None')

    class Class(models.TextChoices):
        Artificer = 'Artificer'
        Barbarian = 'Barbarian'
        Bard = 'Bard'
        Cleric = 'Cleric'
        Druid = 'Druid'
        Fighter = 'Fighter'
        Monk = 'Monk'
        Paladin = 'Paladin'
        Ranger = 'Ranger'
        Rogue = 'Rogue'
        Sorcerer = 'Sorcerer'
        Warlock = 'Warlock'
        Wizard = 'Wizard'

    Class = models.CharField(max_length=10, choices=Class.choices, default='None')

    # Stats
    level = models.IntegerField()
    life = models.IntegerField()
    points = models.IntegerField()
    feets = models.IntegerField()
    initiative = models.IntegerField()

    # Atributes
    strength = models.IntegerField()
    dexterity = models.IntegerField()
    constituition = models.IntegerField()
    intelligence = models.IntegerField()
    wisdom = models.IntegerField()
    charisma = models.IntegerField()

    # About
    about = models.TextField(default='')

    def __str__(self):
        return "%s %s" % (self.user, self.name)
