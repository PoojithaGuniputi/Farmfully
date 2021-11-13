from django.contrib import admin
from interface.models import Contact
from interface.models import Forum_query, Reply

# Register your models here.
admin.site.register(Contact)


# # Register your models here.
admin.site.register(Forum_query)

admin.site.register(Reply)