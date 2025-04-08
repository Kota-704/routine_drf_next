from django.db import models
import uuid
from datetime import date
from django.core.validators import MinValueValidator
from django.contrib.auth.models import User


class RoutineModels(models.Model):
  id=models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, verbose_name='ID')
  user=models.ForeignKey(User, on_delete=models.CASCADE)
  title=models.CharField(max_length=100, verbose_name='タイトル')
  period=models.IntegerField(null=True, blank=True, validators=[MinValueValidator(1)], help_text='例：7 = 毎週、30 = 毎月', verbose_name='周期')
  start_date=models.TimeField(default=date.today, verbose_name='開始日時')
  create_at=models.TimeField(auto_now_add=True, verbose_name='作成日時')
  url=models.URLField(null=True, blank=True, verbose_name='URL')
  notice_text=models.TextField(max_length=1000, verbose_name='通知内容')
