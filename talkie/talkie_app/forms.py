from django import forms
from .models import talkie_user_models, talkie_review, talkie_favourite, talkie_user_profile

class TalkieUserModelForm(forms.Form):
    subscription_type = forms.ModelChoiceField(queryset=talkie_user_models.objects.all(), empty_label="Select Plan")
    # name = forms.CharField(max_length=100, required=True)
