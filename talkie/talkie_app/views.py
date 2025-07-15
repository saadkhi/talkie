from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponse, Http404

from .models import talkie_user_models

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