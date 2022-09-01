from django.contrib import admin

# Parte 02
from .models import Question
# Fim da parte 02

# Parte 07
from .models import Choice, Question
# Fim da parte 07

# Parte 07
class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date']}),
    ]

admin.site.register(Question, QuestionAdmin)
# Fim da parte 07

# Parte 07
admin.site.register(Choice)
# Fim da parte 07

# Register your models here.
