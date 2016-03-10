from django.contrib import admin
from .models import Question, Choice

class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
	# 방법1-1. 필드 추가하기.
	#fields = ['pub_date', 'question_text']
	
	# 방법1-2. 필드 추가시.
	fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date']}),
    ]
	
	# 관련 필드까지 같이 여러개 동시에 추가하기
	inlines = [ChoiceInline]
	
	# 테이블 전체필드를 보여주는 방식.
	list_display = ('question_text', 'pub_date', 'was_published_recently')
	
	# 'pub_date'로 필터해서 보여줌.
	list_filter = ['pub_date']

admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
