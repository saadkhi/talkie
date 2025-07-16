from django.contrib import admin
from .models import talkie_user_models, talkie_review, talkie_favourite, talkie_user_profile

# Inline review admin to show reviews inside plan admin
class TalkieReviewInline(admin.TabularInline):
    model = talkie_review
    extra = 2

# Admin for talkie_user_models (plans)
class TalkieUserModelsAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'price', 'duration', 'date_time')
    search_fields = ('name', 'type')
    list_filter = ('type',)
    ordering = ('-date_time',)
    inlines = [TalkieReviewInline]  # ✅ Add inline reviews here

# Admin for talkie_favourite
class TalkieFavouriteAdmin(admin.ModelAdmin):
    list_display = ('user', 'date_time')
    filter_horizontal = ('talkie_plan_favourite',)  # ✅ valid for ManyToManyField

# Admin for talkie_user_profile
class TalkieUserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'talkie_plan', 'profile_created_data_time', 'date_time')

# Register the models with appropriate admin classes
admin.site.register(talkie_user_models, TalkieUserModelsAdmin)
admin.site.register(talkie_favourite, TalkieFavouriteAdmin)
admin.site.register(talkie_user_profile, TalkieUserProfileAdmin)
admin.site.register(talkie_review)  # ✅ Register normally, not inline
