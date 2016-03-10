from django.contrib import admin
from .models import Question, Choice

class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
	# ���1-1. �ʵ� �߰��ϱ�.
	#fields = ['pub_date', 'question_text']
	
	# ���1-2. �ʵ� �߰���.
	fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date']}),
    ]
	
	# ���� �ʵ���� ���� ������ ���ÿ� �߰��ϱ�
	inlines = [ChoiceInline]
	
	# ���̺� ��ü�ʵ带 �����ִ� ���.
	list_display = ('question_text', 'pub_date', 'was_published_recently')
	
	# 'pub_date'�� �����ؼ� ������.
	list_filter = ['pub_date']

admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
