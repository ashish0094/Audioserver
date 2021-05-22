from django.contrib import admin
from .models import Song
from .models import Podcast
from .models import Audiobook
from .models import Participant
# from .models import Participants

# Register your models here.
# class ParticipantsInline(admin.TabularInline):
#     model = Participants

# class PodcastAdmin(admin.ModelAdmin):
#     inlines = [ParticipantsInline]


admin.site.register(Song),
admin.site.register(Podcast),
admin.site.register(Audiobook),
admin.site.register(Participant)
# admin.site.register(Participants)
