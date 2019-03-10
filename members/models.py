from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

class MemberManager(BaseUserManager):

	use_in_migrations = True

	def _create_user(self, email, password, **extra_fields):
		if not email:
			raise ValueError("Email can't be blank.")
		email = self.normalize_email(email)
		user = self.model(email=email, **extra_fields)
		user.set_password(password)
		user.save(using=self._db)
		return user

	def create_user(self, email, password=None, **extra_fields):
		extra_fields.setdefault('is_staff', False)
		extra_fields.setdefault('is_superuser', False)
		return self._create_user(email, password, **extra_fields)

	def create_superuser(self, email, password, **extra_fields):
		extra_fields.setdefault('is_staff', True)
		extra_fields.setdefault('is_superuser', True)
		if extra_fields.get('is_staff') is not True:
			raise ValueError('Superuser must have is_staff=True.')
		if extra_fields.get('is_superuser') is not True:
			raise ValueError('Superuser must have is_superuser=True.')
		super_user = self._create_user(email, password, **extra_fields)
		return super_user

class Member(AbstractUser):
	username = None
	email = models.EmailField(max_length=100, unique=True)
	first_name = models.CharField(max_length=200)
	last_name = models.CharField(max_length=200)
	date_of_birth = models.DateField()
	email_activated = models.BooleanField(default=False)
	user_salt = models.CharField(max_length = 32, default=0)
	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = ['date_of_birth', 'first_name', 'last_name']
	objects = MemberManager()

	def __str__(self):
		return u"%s %s %s" % (self.email, self.user_salt, self.email_activated)

class Preference(models.Model):
	user = models.ForeignKey(Member, on_delete=models.CASCADE)
	preferences = models.CharField(max_length=500)
	REQUIRED_FIELDS = ['preferences']

	def __str__(self):
		return u"%s" % (self.preferences)