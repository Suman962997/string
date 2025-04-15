from django.db import models
from django.utils.translation import gettext_lazy as _

class Gateway(models.Model):
    Company=models.CharField(max_length=30)
    Block=models.CharField(max_length=5)
    Floar=models.IntegerField()
    Rent=models.IntegerField()


 
class Company(models.Model):
    """
    Company model
    """

    company = models.CharField(max_length=50)
    hq = models.BooleanField(default=False)
    address = models.CharField(max_length=255)
    country = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    zip = models.CharField(max_length=20)
    icon = models.FileField(
        upload_to="base/icon",
        null=True,
    )
    objects = models.Manager()
    date_format = models.CharField(max_length=30, blank=True, null=True)
    time_format = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        """
        Meta class to add additional options
        """

        verbose_name = _("Company")
        verbose_name_plural = _("Companies")
        unique_together = ["company", "address"]
        # app_label = "base"

    def __str__(self) -> str:
        return str(self.company)

