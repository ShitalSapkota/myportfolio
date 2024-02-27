from django.db import models
import datetime

# Create your models here.


class About(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=50)
    email = models.EmailField()
    age = models.CharField(max_length=50)
    degree = models.CharField(max_length=100)
    linkedIn = models.URLField(max_length=200)
    git_hub = models.URLField(max_length=200)
    image_name = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.name} {self.title} {self.description}'


class Image(models.Model):
    image_id = models.ForeignKey(About, default=None,on_delete=models.CASCADE)
    image_items = models.ImageField(upload_to='portfolio/', verbose_name='Image', blank=True, null=True)

    def __str__(self):
        return self.image_items


class Skill(models.Model):
    skills_name = models.CharField(max_length=100)

    def __str__(self):
        return self.skills_name


class Certificate(models.Model):
    certificate_name = models.CharField(max_length=100)
    certificate_url = models.URLField(max_length=200)

    def __str__(self):
        return f'{self.certificate_name} {self.certificate_url}'


class Education(models.Model):
    school_name = models.CharField(max_length=100)
    course_name = models.CharField(max_length=100)
    school_address = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return f'{self.school_name} {self.school_address} {self.description}'


class Experience(models.Model):
    company_name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    company_address = models.CharField(max_length=100)
    tasks = models.CharField(max_length=300)      ## description
    url = models.URLField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return f'{self.company_name} {self.role} {self.tasks}'


class ResumeList(models.Model):
    skill_id = models.ForeignKey(Skill, default=None,on_delete=models.CASCADE)
    certificate_id = models.ForeignKey(Certificate, default=None, on_delete=models.CASCADE)
    education_id = models.ForeignKey(Education, default=None, on_delete=models.CASCADE)
    experience_id = models.ForeignKey(Experience, default=None,on_delete=models.CASCADE)




