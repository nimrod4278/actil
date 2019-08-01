from django.shortcuts import render
from django.contrib.auth.decorators import login_required


from mission.models import Mission


@login_required
def home(request):
    missions = Mission.objects.user_active_missions(request.user)
    num_of_missions = Mission.objects.count_user_active_missions(request.user)
    return render(request, "player/home.html",
                  {'num_of_missions': num_of_missions,
                   'missions': missions})
