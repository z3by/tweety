from django.contrib import admin

from .models import Tweet


@admin.register(Tweet)
class TweetAdmin(admin.ModelAdmin):
    list_display = ["id", "text", "author"]
    fields = ["text", "author", "in_reply_to_status", "created_date", "modified_date"]
    readonly_fields = ["created_date", "modified_date"]
