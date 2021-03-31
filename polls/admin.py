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
    list_display = ('question_text', 'pub_date', 'was_published_recently') #리스트에 보이는 것들 커스텀
    list_filter = ['pub_date'] # 오른쪽에 filter 사이드바 추가
    search_fields = ['question_text'] # 맨 위에 검색창 추가

admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
