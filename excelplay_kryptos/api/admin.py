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


admin.site.register(Level, LevelAdmin)
admin.site.register(KryptosUser)
admin.site.register(AnswerLog)