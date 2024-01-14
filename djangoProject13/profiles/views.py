from django.shortcuts import render, redirect
from .models import Profile
from .form import ProfileForm
from django.db.models import Q


def profile_list(request):
    query = request.GET.get('q', '')
    gender_filter = request.GET.get('gender_filter', '')
    age_filter = request.GET.get('age_filter', '')
    institute_filter = request.GET.get('institution_filter', '')

    profiles = Profile.objects.all()

    if query:
        profiles = profiles.filter(
            Q(gender__icontains=query) |
            Q(age__icontains=query) |
            Q(institution__icontains=query) |
            Q(first_name__icontains=query) |  # Поиск по полю "first_name", без учета регистра
            Q(last_name__icontains=query) |
            Q(interests__icontains=query)
        )

    if gender_filter:
        profiles = profiles.filter(gender=gender_filter)
    if age_filter:
        profiles = profiles.filter(age=age_filter)
    if institute_filter:
        profiles = profiles.filter(institution=institute_filter)

    if not profiles:
        message = "Извините, но людей с такими критериями пока не зарегистрировано."
    else:
        message = ""

    return render(request, 'profile_list.html', {'profiles': profiles, 'message': message})


def create_profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('profile_list')  # после успешного сохранения переходим на страницу с профилями
    else:
        form = ProfileForm()
    return render(request, 'profile_form.html', {'form': form})



def profile_detail(request, profile_id):
    profile = Profile.objects.get(pk=profile_id)
    return render(request, 'profile_detail.html', {'profile': profile})
