from django.db.models import TextChoices
import pytz

USER_TIMEZONES = [(zone, zone) for zone in pytz.all_timezones]
DEFAULT_TIMEZONE = "Asia/Kolkata"


class OrgUserRoleChoices(TextChoices):
    USER = "user"
    MANAGER = "manager"
