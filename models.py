from django.db import models

# Create your models here.
class klmn(models.Model):
    name=models.CharField(max_length=300)
    description=models.TextField()
    costperitem=models.DecimalField(max_digits=20,decimal_places=3)
    stockquantity=models.DecimalField(max_digits=15,decimal_places=2)
    volume=models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True )

    def calc_volume(self):
        v=self.costperitem * self.stockquantity
        return v
    def save(self, *args, **kwargs):
        self.volume=self.calc_volume()
        super(klmn, self).save()
    def __str__(self):
        return self.name
