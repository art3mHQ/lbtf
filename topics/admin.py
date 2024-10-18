from django.contrib import admin

from .models import Comment
from .models import Customfield
from .models import Field
from .models import JoinRequest
from .models import Like
from .models import MyCustomTimeZones
from .models import Subfield
from .models import Topic

admin.site.register(Topic)
admin.site.register(Comment)
admin.site.register(JoinRequest)
admin.site.register(Like)
admin.site.register(Field)
admin.site.register(Subfield)
admin.site.register(Customfield)
admin.site.register(MyCustomTimeZones)
