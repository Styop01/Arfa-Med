from django.db import models

# _______________________________________________________
# aboutUs _______________________________________________
# _______________________________________________________


class AboutUsAccordion(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    img = models.CharField(max_length=50)
    title = models.CharField(max_length=20)
    toggle = models.CharField(max_length=20, blank=True)
    body = models.TextField()

    def __str__(self):
        return self.title

# ________________________________________________________
# device _________________________________________________
# ________________________________________________________


class DeviceBanner(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    img = models.CharField(max_length=20)

    def __str__(self):
        return self.img


class DeviceProduct(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    img = models.CharField(max_length=70)
    title = models.CharField(max_length=50)
    price = models.CharField(max_length=20)
    discount = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return self.title

# _________________________________________________________
# sideBar _________________________________________________
# _________________________________________________________


class SideBarCategories(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    text = models.CharField(max_length=20)
    number = models.PositiveIntegerField()

    def __str__(self):
        return self.text


# _________________________________________________________
# servicesSideBar _________________________________________
# _________________________________________________________

class ServiceNavbar(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    title = models.CharField(max_length=50)
    link = models.CharField(max_length=50)

    def __str__(self):
        return self.title

# _________________________________________________________
# faq _____________________________________________________
# _________________________________________________________


class FaqQuestions(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    title = models.CharField(max_length=150)
    toggle = models.CharField(max_length=20, blank=True)
    body = models.TextField()

    def __str__(self):
        return self.title

# ___________________________________________________________
# contactUs _________________________________________________
# ___________________________________________________________


class ContactUsForm(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    icon = models.TextField(max_length=70)
    title = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    type = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.title


class ContactUsCard(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    icon = models.TextField(max_length=70)
    title = models.CharField(max_length=50)
    subtitle = models.CharField(max_length=50)

    def __str__(self):
        return self.title

# ___________________________________________________________
# GLOBAL ____________________________________________________
# ___________________________________________________________


class GlobalTeam(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    img = models.TextField(max_length=100)
    content = models.CharField(max_length=50)
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class GlobalTestimonial(models.Model):
    id = models.IntegerField(primary_key=True)
    img = models.CharField(max_length=50)
    name = models.CharField(max_length=30)
    subtitle = models.CharField(max_length=30)
    body = models.TextField()

    def __str__(self):
        return self.name


class GlobalClients(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    img = models.CharField(max_length=50)
    hover = models.CharField(max_length=20)

    def __str__(self):
        return self.hover


class GlobalHeader(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    title = models.CharField(max_length=60)
    link = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class ForBlog(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    img = models.CharField(max_length=20)
    dateAttr = models.CharField(max_length=30)
    day = models.PositiveIntegerField()
    month = models.CharField(max_length=10)
    year = models.PositiveIntegerField()
    commCount = models.IntegerField()
    publisher = models.CharField(max_length=20)
    title = models.CharField(max_length=50)
    to = models.CharField(max_length=10)
    subtitle = models.TextField()
    single = models.TextField()

    def __str__(self):
        return self.title


# ________________________________________________________
# HOME ___________________________________________________
# ________________________________________________________

class IconBox(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    icon = models.CharField(unique=True, max_length=70)
    title = models.CharField(max_length=70)
    subtitle = models.TextField(max_length=250)

    def __str__(self):
        return self.title


class ServiceBox(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    icon = models.CharField(unique=True, max_length=30)
    title = models.CharField(max_length=30)
    subtitle = models.TextField(max_length=250)

    def __str__(self):
        return self.title


class Appointments(models.Model):
    fullName = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    gender = models.CharField(max_length=20)
    phoneNumber = models.PositiveIntegerField()
    eMail = models.EmailField(max_length=50)
    healthComplaints = models.CharField(max_length=50)

    def __str__(self):
        return self.fullName


class Message(models.Model):
    name = models.CharField(max_length=50)
    phone = models.PositiveIntegerField()
    email = models.EmailField(max_length=50)
    venue = models.CharField(max_length=50)
    message = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.name




