from django.contrib import admin

from .models import Question, Choice

class ChoiceInline(admin.TabularInline): # StackedInline/TabularInline형태옵션
    model = Choice
    extra = 3  # 기본으로 3가지 선택 항목을 제공

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]

admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
