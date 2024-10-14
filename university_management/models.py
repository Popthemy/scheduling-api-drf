from django.db import models
from django.conf import settings
from uuid import uuid4
# Create your models here.

User = settings.AUTH_USER_MODEL


class Institution(models.Model):
    id = models.UUIDField(default=uuid4, primary_key=True,
                          unique=True, editable=True)
    name = models.CharField(max_length=255, unique=True,
                            help_text='The name of the university in full e.g Ladoke Akintola University of Technology')
    slug = models.SlugField(null=True,blank=True)
    phone = models.JSONField(
        help_text='Enter your phone number in a standard json form. A university can have more than one number')
    email = models.EmailField(unique=True)
    website = models.URLField(unique=True)
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name', 'email', 'website')

    def __str__(self) -> str:
        return f'{self.name}'


class Faculty(models.Model):
    '''An institution has many faculty'''

    institution = models.ForeignKey(Institution, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, help_text='name of your faculty')
    dean = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    email = models.EmailField(unique=True)
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name', 'email')
        verbose_name = 'Faculty'
        verbose_name_plural = 'Faculties'

    def __str__(self) -> str:
        return f'Dean :{self.dean} of {self.name} '


class Department(models.Model):
    '''A Faculty has many department'''

    name = models.CharField(
        max_length=255, help_text='name of your department')
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    head_of_department = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True)
    email = models.EmailField(unique=True)
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name',)

    def __str__(self) -> str:
        return f'HOD of {self.head_of_department} of {self.name}'


class Program(models.Model):
    '''University runs program such as B.Sc , B.Tech ...'''

    BACHELOR_OF_SCIENCE = 'Bachelor of Science'
    BACHELOR_OF_TECHNOLOGY = 'Bachelor of Technology'
    MASTER_OF_ARTS = 'Master of Arts'
    DOCTOR_OF_PHILOSOPHY = 'Doctor of Philosophy'

    DEGREE_CHOICES = (
        (BACHELOR_OF_SCIENCE, 'B.Sc'),
        (BACHELOR_OF_TECHNOLOGY, 'B.Tech'),
        (MASTER_OF_ARTS, 'MA'),
        (DOCTOR_OF_PHILOSOPHY, 'PhD'),
    )

    WEEKLY_TYPE = 'WEEKLY'
    MONTHLY_TYPE = 'MONTHLY'
    YEARLY_TYPE = 'YEARLY'

    DURATION_TYPE_CHOICES = (
        (WEEKLY_TYPE, 'weekly'),
        (MONTHLY_TYPE, 'monthly'),
        (YEARLY_TYPE, 'yearly'),

    )

    degree_type = models.CharField(
        max_length=50, choices=DEGREE_CHOICES, default=BACHELOR_OF_SCIENCE)
    duration = models.PositiveSmallIntegerField()
    duration_type = models.CharField(
        max_length=30, choices=DURATION_TYPE_CHOICES, default=WEEKLY_TYPE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    class Meta:
        ordering = ('degree_type', 'duration')

    def __str__(self) -> str:
        return f'{self.degree_type} is {self.duration} {self.duration_type}'
