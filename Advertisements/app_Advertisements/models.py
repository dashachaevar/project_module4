from django.db import models

from django.contrib import admin
from django.utils import timezone
from django.utils.html import format_html
from django.contrib.auth import get_user_model
from django.urls import reverse


User = get_user_model()


class Advertisements(models.Model):
    title = models.CharField("заголовок", max_length = 128)
    description = models.TextField("описание")
    price = models.DecimalField("цена", max_digits = 10, decimal_places = 2)
    auction = models.BooleanField("торг", help_text = "Отметьте, если торг уместен")
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    user = models.ForeignKey(User, verbose_name = 'пользователь', on_delete = models.CASCADE)
    image = models.ImageField("изображение", upload_to = 'advertisements/', blank = True)


    @admin.display(description = "дата создания")
    def created_date(self):
        if self.created_at.date() == timezone.now().date():
            created_time = self.created_at.time().strftime("%H:%M:%S")
            return format_html(
                "<span style = 'color: green; font-weight: bold'>Сегодня в {}</span>",
                created_time
            )
        return self.created_at.strftime("%d.%m.%Y at %H:%M:%S")
    
    @admin.display(description = "дата обновления")
    def updated_date(self):
        if self.updated_at.date() == timezone.now().date():
            updated_time = self.updated_at.time().strftime("%H:%M:%S")
            return format_html(
                "<span style = 'color: blue; font-weight: bold'>Сегодня в {}</span>",
                updated_time
            )
        return self.created_at.strftime("%d.%m.%Y at %H:%M:%S")
    
    @admin.display(description = "изображене")
    def image_display(self):
        if self.image:
            return format_html(
                '<img src = "{}" style = "width: 55px;">', self.image.url
            )
        else:
            return "No Image"
        

    def get_absolute_url(self):
        return reverse('adv-detail', kwargs ={'pk':self.pk})


    class Meta: 
        db_table = 'advertisements'

    def __str__(self): 
        return f"<Advertisement: Advertisement(id={self.id}, title={self.title}, price={self.price})>"