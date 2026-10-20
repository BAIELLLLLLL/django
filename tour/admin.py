from django.contrib import admin
from .models import Person, Tour, Comment, Category, Ticket

admin.site.register(Person)
admin.site.register(Tour)
admin.site.register(Comment)
admin.site.register(Category)
admin.site.register(Ticket)
