from django.contrib import admin

from . import models


admin.site.register(models.Player)
admin.site.register(models.Equipe)
admin.site.register(models.Match)
admin.site.register(models.Poule)
admin.site.register(models.Tournoi)
admin.site.register(models.User)
