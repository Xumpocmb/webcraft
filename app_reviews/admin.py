from django.contrib import admin
from .models import Review, Reply

class ReplyInline(admin.TabularInline):
    model = Reply
    extra = 1
    readonly_fields = ('author', 'created_at')

    def save_formset(self, request, form, formset, change):
        instances = formset.save(commit=False)
        for instance in instances:
            if not instance.pk:
                instance.author = request.user
            instance.save()
        formset.save_m2m()

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('author', 'rating', 'likes', 'created_at')
    list_filter = ('rating', 'created_at')
    search_fields = ('author', 'comment')
    readonly_fields = ('likes', 'created_at')
    inlines = [ReplyInline]

@admin.register(Reply)
class ReplyAdmin(admin.ModelAdmin):
    list_display = ('author', 'review', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('author__username', 'comment')
    readonly_fields = ('author', 'created_at')