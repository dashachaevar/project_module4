from django.contrib import admin
from .models import Advertisements
from django.utils import timezone
from django.utils.html import format_html
from django.db.models.query import QuerySet


class AdvertisementsAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "description", "price", "auction", "created_at", "created_date"]
    list_filter = ["auction", "created_at", "price"]
    actions = ["make_action_as_false", "make_action_as_true"]
    fieldsets = (
        ("Общие", {
            "fields": (
                "title", "description"
            ),
        }),
        ("Финансы", {
            "fields": (
                "price", "auction"
            ),
            "classes": ['collapse']
        }),
    )
    



    @admin.action(description = "Убрать возможность торга")
    def make_action_as_false(self, request, queryset:QuerySet):
        queryset.update(auction = False)

    @admin.action(description = "Добавить возможность торга")
    def make_action_as_true(self, request, queryset:QuerySet):
        queryset.update(auction = True)

    @admin.display(description = "дата создания")
    def created_date(self):
        if self.created_at.date() == timezone.now().date():
            created_time = self.created_at.time().strftime("%H:%M:%S")
            return format_html(
                "<span style = 'color:green; font-weight: bold'>Сегодня в {}</span>",
                created_time
            )
        return self.created_at.strftime("%d.%m.%Y at %H:%M:%S")

admin.site.register(Advertisements, AdvertisementsAdmin)