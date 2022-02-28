from django.contrib import admin
from .models import Blog,Comment,Like,Category,Contact,Quote,Replycomment,Profile

# Register your models here.

admin.site.register(Blog)

admin.site.register(Comment)

admin.site.register(Like)


admin.site.register(Category)

admin.site.register(Contact)
admin.site.register(Quote)


admin.site.register(Replycomment)

admin.site.register(Profile)

# admin.site.register(Tag)