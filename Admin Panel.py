from django import forms
from django.contrib import admin
from ckeditor.widgets import CKEditorWidget
from .models import FAQ

class FAQAdminForm(forms.ModelForm):
    class Meta:
        model = FAQ
        fields = '__all__'
        widgets = {
            'answer_en': CKEditorWidget(),
            'answer_hi': CKEditorWidget(),
            'answer_bn': CKEditorWidget(),
        }

@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    form = FAQAdminForm
    list_display = ('question_en', 'created_at')
    fieldsets = [
        ('English', {'fields': ['question_en', 'answer_en']}),
        ('Hindi', {'fields': ['question_hi', 'answer_hi']}),
        ('Bengali', {'fields': ['question_bn', 'answer_bn']}),
    ]
