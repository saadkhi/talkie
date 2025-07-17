from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponse, Http404

from .models import talkie_user_models
from .forms import TalkieUserModelForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    all_plans = talkie_user_models.objects.all()
    return render(request, 'website/index.html', {'all_plans': all_plans})

def plan_details(request, plan_id):
    plan = get_object_or_404(talkie_user_models, pk=plan_id)
    return render(request, 'website/plan_details.html', {'plan': plan})

# ...existing code...

def download_plan(request, plan_id):
    plan = get_object_or_404(talkie_user_models, pk=plan_id)
    if not plan.image:
        raise Http404("No file associated with this plan.")
    response = HttpResponse(plan.image, content_type='application/octet-stream')
    response['Content-Disposition'] = f'attachment; filename="{plan.image.name.split("/")[-1]}"'
    return response

def about(request):
    return render(request, 'website/about.html')

def contact(request):
    return render(request, 'website/contact.html')

def plan_available(request):
    plan = None
    if request.method == 'POST':
        form = TalkieUserModelForm(request.POST)
        if form.is_valid():
            subscription_type = form.cleaned_data['subscription_type']
            plan = talkie_user_models.objects.filter(type=subscription_type).first()
    else:
        form = TalkieUserModelForm()
    return render(request, 'website/plan_available.html', {'form': form, 'plan': plan})


def plan_store(request):
    plans = talkie_user_models.objects.all()
    return render(request, 'website/plan_store.html', {'plans': plans}) 