from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField('Categoriya', max_length=200)
    slug = models.SlugField('*', max_length=200)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Categoriyes'


class Turnir(models.Model):
    title = models.CharField('Musobaqaning-Nomi', max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField('Rasimi', upload_to='images/')
    description = models.TextField('Matn', blank=True, null=True)
    address = models.CharField('Manzil', max_length=200)
    date = models.DateTimeField('Qachon va nechida boshlanishi', blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta: 
        verbose_name_plural = 'Turnirs'


class TurnirsTime(models.Model):
    turnir = models.ForeignKey(Turnir,
        default=None,
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name='turnirs_time')
    timeline = models.TimeField('Time Line', blank=True, null=True)
    text = models.CharField("Nima bo'lishi", max_length=200)

    def __str__(self):
        return self.turnir.title

    class Meta:
        verbose_name_plural = 'Turnirs Time'


class TurnirQuestion(models.Model):
    name_surname = models.CharField('Ism Familiya: ', max_length=400)
    age = models.FloatField('Yosh', max_length=3)
    telephone = models.CharField('Telefon: ', max_length=20)
    text = models.TextField('Qoshimcha fikringiz: ', blank=True, null=True)
    turnir = models.ForeignKey(Turnir, on_delete=models.CASCADE, related_name='questions')

    def __str__(self):
        return self.name_surname


class TurnirAuth(models.Model):
    name_surname = models.CharField('Ism Familiya', max_length=400)
    age = models.FloatField('Yosh', max_length=3)
    staj = models.CharField('Tajribangiz necha oy/yil ?', max_length=20)
    telephone = models.CharField('Telefon: ', max_length=20)
    text = models.TextField('Qoshimcha fikringiz: ', blank=True, null=True)

    def __str__(self):
        return self.name_surname


class Contact(models.Model):
    name = models.CharField('Ism: ', max_length=200)
    phone = models.CharField('Telefon raqam: ', max_length=30)
    text = models.TextField('XAbar Matni', blank=True, null=True)

    def __str__(self):
        return self.name


class Tadbir(models.Model):
    title = models.CharField('Tadbirning-Nomi', max_length=200)
    image = models.ImageField('Rasimi', upload_to='images/')
    description = models.TextField('Matn', blank=True, null=True)
    address = models.CharField('Manzil', max_length=200)
    date = models.DateTimeField('Qachon va nechida boshlanishi', blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta: 
        verbose_name_plural = 'Tadbir'


class TadbirsTime(models.Model):
    turnir = models.ForeignKey(Tadbir,
        default=None,
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name='tadbir_time')
    timeline = models.TimeField('Time Line', blank=True, null=True)
    text = models.CharField("Nima bo'lishi", max_length=200)

    def __str__(self):
        return self.turnir.title

    class Meta:
        verbose_name_plural = 'Tadbirs Time'