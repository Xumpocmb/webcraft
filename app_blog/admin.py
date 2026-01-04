from django.contrib import admin
from modeltranslation.admin import TabbedTranslationAdmin
from .models import Article, ArticleComment

class ArticleCommentInline(admin.TabularInline):
    model = ArticleComment
    extra = 1
    readonly_fields = ('author', 'created_at')

    def save_formset(self, request, form, formset, change):
        instances = formset.save(commit=False)
        for instance in instances:
            if not instance.pk:
                instance.author = request.user
            instance.save()
        formset.save_m2m()

@admin.register(Article)
class ArticleAdmin(TabbedTranslationAdmin):
    list_display = ('title', 'likes', 'created_at')
    search_fields = ('title', 'content')
    readonly_fields = ('likes', 'created_at')
    inlines = [ArticleCommentInline]

@admin.register(ArticleComment)
class ArticleCommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'article', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('author__username', 'comment')
    readonly_fields = ('author', 'article', 'created_at')