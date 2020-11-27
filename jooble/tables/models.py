from django.db import models


class JoobleIndia(models.Model):
    objects = None
    title = 'India'
    vacancy = models.CharField(max_length=20000)
    link_to_a_vacancy = models.CharField(max_length=20000)
    salary = models.CharField(max_length=20000)
    company = models.CharField(max_length=20000)
    short_description = models.CharField(max_length=20000)
    location = models.CharField(max_length=20000)
    date_from_creation = models.CharField(max_length=20000)
    full_description = models.CharField(max_length=20000)
    link_to_a_company = models.CharField(max_length=20000)

    def __str__(self):
        return self.title


class JoobleCanada(models.Model):
    objects = None
    title = 'Canada'
    vacancy = models.CharField(max_length=20000)
    link_to_a_vacancy = models.CharField(max_length=20000)
    salary = models.CharField(max_length=20000)
    company = models.CharField(max_length=20000)
    short_description = models.CharField(max_length=20000)
    location = models.CharField(max_length=20000)
    date_from_creation = models.CharField(max_length=20000)
    full_description = models.CharField(max_length=20000)
    link_to_a_company = models.CharField(max_length=20000)

    def __str__(self):
        return self.title


class JoobleNewZealand(models.Model):
    objects = None
    title = 'New_Zealand'
    vacancy = models.CharField(max_length=20000)
    link_to_a_vacancy = models.CharField(max_length=20000)
    salary = models.CharField(max_length=20000)
    company = models.CharField(max_length=20000)
    short_description = models.CharField(max_length=20000)
    location = models.CharField(max_length=20000)
    date_from_creation = models.CharField(max_length=20000)
    full_description = models.CharField(max_length=20000)
    link_to_a_company = models.CharField(max_length=20000)

    def __str__(self):
        return self.title


class JoobleAustralia(models.Model):
    objects = None
    title = 'Australia'
    vacancy = models.CharField(max_length=20000)
    link_to_a_vacancy = models.CharField(max_length=20000)
    salary = models.CharField(max_length=20000)
    company = models.CharField(max_length=20000)
    short_description = models.CharField(max_length=20000)
    location = models.CharField(max_length=20000)
    date_from_creation = models.CharField(max_length=20000)
    full_description = models.CharField(max_length=20000)
    link_to_a_company = models.CharField(max_length=20000)

    def __str__(self):
        return self.title


class JoobleNigeria(models.Model):
    objects = None
    title = 'Nigeria'
    vacancy = models.CharField(max_length=20000)
    link_to_a_vacancy = models.CharField(max_length=20000)
    salary = models.CharField(max_length=20000)
    company = models.CharField(max_length=20000)
    short_description = models.CharField(max_length=20000)
    location = models.CharField(max_length=20000)
    date_from_creation = models.CharField(max_length=20000)
    full_description = models.CharField(max_length=20000)
    link_to_a_company = models.CharField(max_length=20000)

    def __str__(self):
        return self.title


class JoobleSouthAfrica(models.Model):
    objects = None
    title = 'South_Africa'
    vacancy = models.CharField(max_length=20000)
    link_to_a_vacancy = models.CharField(max_length=20000)
    salary = models.CharField(max_length=20000)
    company = models.CharField(max_length=20000)
    short_description = models.CharField(max_length=20000)
    location = models.CharField(max_length=20000)
    date_from_creation = models.CharField(max_length=20000)
    full_description = models.CharField(max_length=20000)
    link_to_a_company = models.CharField(max_length=20000)

    def __str__(self):
        return self.title


class JoobleUnitedKingdom(models.Model):
    objects = None
    title = 'United_Kingdom'
    vacancy = models.CharField(max_length=20000)
    link_to_a_vacancy = models.CharField(max_length=20000)
    salary = models.CharField(max_length=20000)
    company = models.CharField(max_length=20000)
    short_description = models.CharField(max_length=20000)
    location = models.CharField(max_length=20000)
    date_from_creation = models.CharField(max_length=20000)
    full_description = models.CharField(max_length=20000)
    link_to_a_company = models.CharField(max_length=20000)

    def __str__(self):
        return self.title


class JoobleIreland(models.Model):
    objects = None
    title = 'Ireland'
    vacancy = models.CharField(max_length=20000)
    link_to_a_vacancy = models.CharField(max_length=20000)
    salary = models.CharField(max_length=20000)
    company = models.CharField(max_length=20000)
    short_description = models.CharField(max_length=20000)
    location = models.CharField(max_length=20000)
    date_from_creation = models.CharField(max_length=20000)
    full_description = models.CharField(max_length=20000)
    link_to_a_company = models.CharField(max_length=20000)

    def __str__(self):
        return self.title


class JoobleSingapore(models.Model):
    objects = None
    title = 'Singapore'
    vacancy = models.CharField(max_length=20000)
    link_to_a_vacancy = models.CharField(max_length=20000)
    salary = models.CharField(max_length=20000)
    company = models.CharField(max_length=20000)
    short_description = models.CharField(max_length=20000)
    location = models.CharField(max_length=20000)
    date_from_creation = models.CharField(max_length=20000)
    full_description = models.CharField(max_length=20000)
    link_to_a_company = models.CharField(max_length=20000)

    def __str__(self):
        return self.title


class JooblePakistan(models.Model):
    objects = None
    title = 'Pakistan'
    vacancy = models.CharField(max_length=20000)
    link_to_a_vacancy = models.CharField(max_length=20000)
    salary = models.CharField(max_length=20000)
    company = models.CharField(max_length=20000)
    short_description = models.CharField(max_length=20000)
    location = models.CharField(max_length=20000)
    date_from_creation = models.CharField(max_length=20000)
    full_description = models.CharField(max_length=20000)
    link_to_a_company = models.CharField(max_length=20000)

    def __str__(self):
        return self.title


class JoobleUSA(models.Model):
    objects = None
    title = 'USA'
    vacancy = models.CharField(max_length=20000)
    link_to_a_vacancy = models.CharField(max_length=20000)
    salary = models.CharField(max_length=20000)
    company = models.CharField(max_length=20000)
    short_description = models.CharField(max_length=20000)
    location = models.CharField(max_length=20000)
    date_from_creation = models.CharField(max_length=20000)
    full_description = models.CharField(max_length=20000)
    link_to_a_company = models.CharField(max_length=20000)

    def __str__(self):
        return self.title


class JooblePhilippines(models.Model):
    objects = None
    title = 'Philippines'
    vacancy = models.CharField(max_length=20000)
    link_to_a_vacancy = models.CharField(max_length=20000)
    salary = models.CharField(max_length=20000)
    company = models.CharField(max_length=20000)
    short_description = models.CharField(max_length=20000)
    location = models.CharField(max_length=20000)
    date_from_creation = models.CharField(max_length=20000)
    full_description = models.CharField(max_length=20000)
    link_to_a_company = models.CharField(max_length=20000)

    def __str__(self):
        return self.title


class JoobleMalaysia(models.Model):
    objects = None
    title = 'Malaysia'
    vacancy = models.CharField(max_length=20000)
    link_to_a_vacancy = models.CharField(max_length=20000)
    salary = models.CharField(max_length=20000)
    company = models.CharField(max_length=20000)
    short_description = models.CharField(max_length=20000)
    location = models.CharField(max_length=20000)
    date_from_creation = models.CharField(max_length=20000)
    full_description = models.CharField(max_length=20000)
    link_to_a_company = models.CharField(max_length=20000)

    def __str__(self):
        return self.title
