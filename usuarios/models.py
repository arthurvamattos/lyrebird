from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, UserManager
from django.contrib.auth.base_user import BaseUserManager


class CustomUserManager(BaseUserManager):

    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError("O campo email é obrigatório")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self.create_user(email, password, **extra_fields)


class Usuario(AbstractBaseUser, PermissionsMixin):
    # username = models.CharField(
    #     'Nome de Usuário', max_length=30, unique=True,
    #     validators=[validators.RegexValidator(re.compile('^[\w.@+-]+$'),
    #         'O nome de usuário só pode conter letras, digitos ou os '
    #         'seguintes caracteres: @/./+/-/_', 'invalid')]
    # )
    email = models.EmailField('E-mail', unique=True)
    fullname = models.CharField('Nome', max_length=255, blank=False, null=False)
    is_active = models.BooleanField('Está ativo?', blank=True, default=True)
    is_staff = models.BooleanField('É da equipe?', blank=True, default=False)
    is_superuser = models.BooleanField('É da equipe?', blank=True, default=False)
    date_joined = models.DateTimeField('Data de entrada', auto_now_add=True)
    last_login = models.DateTimeField('Último login', null=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['fullname', ]
    EMAIL_FIELD = 'email'

    def __str__(self):
        return self.fullname

    class Meta:
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'


# class PasswordReset(models.Model):
#    user = models.ForeignKey(
#        settings.AUTH_USER_MODEL, verbose_name='Usuário',
#        related_name='resets', on_delete=models.CASCADE,
#    )
#    key = models.CharField('Chave', max_length=100, unique=True)
#    created_at = models.DateTimeField('Criado em', auto_now_add=True)
#    confirmed = models.BooleanField('Confirmado?', default=False, blank=True)
#
#    def __str__(self):
#        return '{0} em {1}'.format(self.user, self.created_at)
#
#    class Meta:
#        verbose_name = 'Nova Senha'
#        verbose_name_plural = 'Novas Senhas'
#        ordering = ['-created_at']

