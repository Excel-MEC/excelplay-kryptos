from django.contrib import admin
from .models import(
    Level,
    KryptosUser,
    AnswerLog,
    Hint,
)
# Register your models here.


class HintsInline(admin.StackedInline):
    model = Hint
    max_num = 30
    extra = 1


class LevelAdmin(admin.ModelAdmin):
    inlines = (HintsInline,)
    list_display = ('level', 'answer', 'source_hint',)

class AnswerLogAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'level', 'answer', 'anstime')

class KryptosUserAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'level', 'last_anstime')


admin.site.register(Level, LevelAdmin)
admin.site.register(KryptosUser, KryptosUserAdmin)
admin.site.register(AnswerLog, AnswerLogAdmin)