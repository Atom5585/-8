from django.db import models
from django.contrib import admin
from django.utils.html import format_html
from django.utils import timezone
class Advertisiment(models.Model):
    title = models.CharField(verbose_name="Название", max_length=128)
    description = models.TextField("Описание")
    price = models.DecimalField("Цена", max_digits=10, decimal_places=3)
    auction = models.BooleanField("Торг", help_text="укажите, если возможен торг")
    create_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @admin.display(description="дата создания")
    def created_date(self):
        if self.create_at.date() == timezone.now().date():
            created_time = self.create_at.time().strftime("%H:%M:%S")
            return format_html(
                "<span style='color: green; font-weight: bold;'>Сегодня в {}</span>", created_time
            )
        return self.create_at.strftime("%d:%m:%Y")

    @admin.display(description="дата обновления")
    def update_date(self):
        if self.updated_at.date() == timezone.now().date():
            updated_time = self.create_at.time().strftime("%H:%M:%S")
            return format_html(
                "<span style='color: blue;'>Сегодня в {}</span>", updated_time
            )
        return self.updated_at.strftime("%d:%m:%Y")

    class Meta:
        db_table = "advertisiments"
        verbose_name = "App_Advertisiments"
        verbose_name_plural = "Объявления"
    def __str__(self):
        return f"Advertisement(id={self.id}, title={self.title}, price={self.price})"

