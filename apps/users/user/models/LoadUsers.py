import uuid
from django.db import models
from django.contrib.auth.hashers import make_password


from apps.core.validators import UniqueInValidator
from apps.users.custom_auth.models import Auth
from apps.users.user.models.Profile import Profile


class LoadUsersManager(models.Manager):
    def create_profiles(self, auth_list, queryset=None, update_status=False):
        if queryset is None:
            self.filter(status=4)

        profile_list = []

        # init instances of profiles and add in profile list
        for profile in queryset:
            try:
                auth = next(
                    (obj for obj in auth_list if obj.email ==
                        profile.email and obj.username == profile.username)
                )
                instance = Profile(
                    auth=auth,
                    city_id=profile.city,
                    identification_type_id=profile.identification_type,
                    identification=profile.identification,
                    name=profile.name,
                    last_name=profile.last_name,
                    phone=profile.phone,
                    phone2=profile.phone2,
                    address=profile.address,
                    postal_code=profile.postal_code)
                profile_list.append(instance)
            except Exception as e:
                if update_status:
                    auth.status = 2
                    auth.save()
                print(e)
        # change status to loaded
        if update_status:
            queryset.update(status=3)

        # create all profiles
        return Profile.objects.bulk_create(profile_list)

    def create_users(self, queryset=None, update_status=False):
        if queryset is None:
            self.filter(
                pk__in=models.Subquery(
                    queryset.filter(status=4).values('pk')
                )
            ).values('email', 'username') \
                .distinct('email', 'username')

        auth_list = []

        # init auth instances and add in auth list
        for auth in queryset:
            try:
                password = Auth.objects.make_random_password()
                user = Auth(**auth, password=make_password(password))
                user._password = password
                auth_list.append(user)

            except Exception as e:
                if update_status:
                    auth.status = 2
                    auth.save()
                print(e)
        if update_status:
            queryset.update(status=3)
        return Auth.objects.bulk_create(auth_list, batch_size=1000)


class LoadUsers(models.Model):

    CHOICE_STATUS = (
        (1, 'OK'),
        (2, 'ERROR'),
        (3, 'CARGADO'),
        (4, 'LOADING'),
    )

    # auth
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    import_id = models.IntegerField(
        "import_id", blank=True, null=True, unique=True)
    email = models.EmailField('email', max_length=250,
                              blank=True, unique=True, validators=[
                                  UniqueInValidator(
                                      Auth, "email")
                              ])
    username = models.CharField(max_length=255, unique=True,
                                validators=[
                                    UniqueInValidator(Auth, "username")
                                ])
    # profile
    identification_type = models.CharField(
        max_length=150, blank=True)
    identification = models.CharField(
        'identification', max_length=150, unique=True, validators=[
            UniqueInValidator(Profile, "identification")
        ])
    city = models.CharField(max_length=150)
    name = models.CharField('name', max_length=150)
    last_name = models.CharField('last name', max_length=150)
    phone = models.CharField('phone number', max_length=50)
    phone2 = models.CharField(
        'phone extra', max_length=50, blank=True, null=True)
    address = models.CharField('address', max_length=250, blank=True)
    postal_code = models.CharField(max_length=50, blank=True, null=True)
    status = models.SmallIntegerField(
        'load status', choices=CHOICE_STATUS, default=4)
    objects = LoadUsersManager()

    def __str__(self) -> str:
        return f'{self.email}|{self.username}|{self.identification_type}|{self.identification}|{self.status}'

    class Meta:
        verbose_name = 'LoadUser'
        verbose_name_plural = 'LoadUser'
        constraints = [
            models.UniqueConstraint(fields=[
                                    "username", "email", "identification"], name="username_email_identification_contraint")
        ]
