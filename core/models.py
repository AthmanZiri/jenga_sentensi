import uuid

from cloudinary_storage.storage import RawMediaCloudinaryStorage
from django.db import models
from django.urls.base import reverse


class Record(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # voice_record = models.FileField(
    #     upload_to="records", storage=RawMediaCloudinaryStorage())
    word = models.CharField(max_length=50, null=True, blank=True)
    # meaning = models.CharField(max_length=100, null=True, blank=True)
    meaning_in_english = models.CharField(max_length=100, null=True, blank=True)
    meaning_in_swahili = models.CharField(max_length=100, null=True, blank=True)
    language = models.CharField(max_length=50, null=True, blank=True)
    voice_record = models.FileField(upload_to="records", null=True, blank=True)
    voice_record_use_case = models.FileField(upload_to="use_cases", null=True, blank=True)

    class Meta:
        verbose_name = "Record"
        verbose_name_plural = "Records"

    def __str__(self):
        return str(self.id)

    def get_absolute_url(self):
        return reverse("core:record_detail", kwargs={"id": str(self.id)})
