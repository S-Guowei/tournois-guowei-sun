from django.contrib import admin

from .models import Player
from .models import Equipe
from .models import Match
from .models import Poule
from .models import Tournoi


admin.site.register(Player)
admin.site.register(Equipe)
admin.site.register(Match)
admin.site.register(Poule)
admin.site.register(Tournoi)
