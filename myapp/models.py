from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class CaretakerManager(BaseUserManager):
	def create_user(self, email, password=None, **extra_fields):
		if not email:
			raise ValueError("The Email field must be set")
		email = self.normalize_email(email)
		caretaker = self.model(email=email, **extra_fields)
		caretaker.set_password(password)
		caretaker.save()
		return caretaker

	def create_superuser(self, email, password=None, **extra_fields):
		extra_fields.setdefault('is_staff', True)
		extra_fields.setdefault('is_superuser', True)
		return self.create_user(email, password, **extra_fields)


class Caretaker(AbstractBaseUser):
	start_at = models.DateTimeField(auto_now_add=True)
	image = models.FileField()
	firstname = models.TextField(max_length=60)
	lastname = models.TextField(max_length=60)
	age = models.IntegerField()
	gender = models.TextField()
	email = models.EmailField(max_length=254, unique=True)
	phone = models.BigIntegerField()
	profession = models.TextField()
	experience = models.IntegerField()
	id_card_number = models.BigIntegerField()
	objective = models.TextField(max_length=300)
	last_login = models.DateTimeField(null=True, blank=True)

	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = []

	objects = CaretakerManager()


class CareseekerManager(BaseUserManager):
	def create_user(self, email, password=None, **extra_fields):
		if not email:
			raise ValueError("The Email field must be set")
		email = self.normalize_email(email)
		careseeker = self.model(email=email, **extra_fields)
		careseeker.set_password(password)
		careseeker.save()
		return careseeker

	def create_superuser(self, email, password=None, **extra_fields):
		extra_fields.setdefault('is_staff', True)
		extra_fields.setdefault('is_superuser', True)
		return self.create_user(email, password, **extra_fields)


class Careseeker(AbstractBaseUser):
	start_at = models.DateTimeField(auto_now_add=True)
	image = models.FileField()
	firstname = models.TextField(max_length=60)
	lastname = models.TextField(max_length=60)
	age = models.IntegerField()
	gender = models.TextField()
	email = models.EmailField(max_length=254)
	phone = models.BigIntegerField()
	state = models.TextField(max_length=60)
	city = models.TextField(max_length=60)
	address = models.TextField(max_length=80)
	order = models.TextField(max_length=100)
	last_login = models.DateTimeField(null=True, blank=True)

	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = []

	objects = CareseekerManager()
