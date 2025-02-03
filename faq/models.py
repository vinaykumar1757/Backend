from django.db import models
from ckeditor.fields import RichTextField
from googletrans import Translator

class FAQ(models.Model):
    question_en = models.TextField()
    question_hi = models.TextField(blank=True)
    question_bn = models.TextField(blank=True)
    answer_en = RichTextField()
    answer_hi = RichTextField(blank=True)
    answer_bn = RichTextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_translated_question(self, lang):
        return getattr(self, f'question_{lang}', self.question_en)
    
    def get_translated_answer(self, lang):
        return getattr(self, f'answer_{lang}', self.answer_en)
    
    def save(self, *args, **kwargs):
        if not self.pk:  # Only on creation
            translator = Translator()
            try:
                if not self.question_hi:
                    self.question_hi = translator.translate(self.question_en, dest='hi').text
                if not self.question_bn:
                    self.question_bn = translator.translate(self.question_en, dest='bn').text
                if not self.answer_hi:
                    self.answer_hi = translator.translate(self.answer_en, dest='hi').text
                if not self.answer_bn:
                    self.answer_bn = translator.translate(self.answer_en, dest='bn').text
            except Exception as e:
                # Fallback to English if translation fails
                pass
        super().save(*args, **kwargs)
