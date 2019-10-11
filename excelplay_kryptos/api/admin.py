from redis_leaderboard.wrapper import RedisLeaderboard

from django.contrib import admin
from .models import(
    Level,
    KryptosUser,
    AnswerLog,
    Hint,
)
# Register your models here.

rdb = RedisLeaderboard('redis', 6379, 0)

class HintsInline(admin.StackedInline):
    model = Hint
    max_num = 30
    extra = 1


class LevelAdmin(admin.ModelAdmin):
    inlines = (HintsInline,)
    list_display = ('level', 'source_hint', 'level_file')


class AnswerLogAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'level', 'answer', 'anstime')
    search_fields = ('user_id',)


class KryptosUserAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'level', 'last_anstime')
    search_fields = ('user_id',)

    def delete_model(self, request, obj):
        rdb.remove('kryptos', obj.user_id)
        super().delete_model(request, obj)


admin.site.register(Level, LevelAdmin)
admin.site.register(KryptosUser, KryptosUserAdmin)
admin.site.register(AnswerLog, AnswerLogAdmin)