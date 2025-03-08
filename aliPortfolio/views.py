from django.shortcuts import render
from .models import home, abouts, information, skills, experience, education, gallerys, clients, bts
from django.urls import reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout


# Create your views here.

def index(request):
    homeDB = home.objects.get(pk=1)
    infoDB = information.objects.get(pk=1)
    clientDB = clients.objects.all()
    return render(request, 'index.html',{
        'homeDB': homeDB,
        'infoDB': infoDB,
        'clientDB': clientDB
    })

def about(request):
    aboutsDB = abouts.objects.get(pk=1)
    infoDB = information.objects.get(pk=1)
    experienceDB = experience.objects.order_by('-sort_date')
    educationDB = education.objects.order_by('-sort_date')
    skillsDB = skills.objects.all()
    return render(request, 'about.html',{
        'aboutDB': aboutsDB,
        'infoDB': infoDB,
        'skillsDB': skillsDB,
        'experienceDB': experienceDB,
        'educationDB': educationDB,
    })

def gallery(request):
    infoDB = information.objects.get(pk=1)
    galleryTitle = gallerys.objects.get(pk=1)
    gallery = gallerys.objects.all()
    return render(request, 'gallery.html',{
        'infoDB': infoDB,
        'galleryTitle': galleryTitle,
        'gallery': gallery,
    })
def dashboard(request):
    infoDB = information.objects.get(pk=1)
    if not request.user.is_authenticated:
        if request.method == 'POST':
            user = authenticate(
                username=request.POST['username'], password=request.POST['password'])
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse('dashboard_home'))
            else:
                return render(request, "dashboard_login.html", {
                    "message": "Invalid username and/or password.",
                    'infoDB': infoDB,
                })
        else:
            return render(request, 'dashboard_login.html',{
                'infoDB': infoDB,
            })
    else:
        return HttpResponseRedirect(reverse(dashboard_home))

def dashboard_home(request):
    homeDB = home.objects.get(pk=1)
    infoDB = information.objects.get(pk=1)
    clientDB = clients.objects.all()
    if request.user.is_authenticated and request.user.is_superuser:
        return render(request, 'dashboard_home.html',{
            'homeDB': homeDB,
            'infoDB': infoDB,
            'clientDB': clientDB
        })
    else:
        return HttpResponseRedirect(reverse(dashboard))
def dashboard_about(request):
    if request.user.is_authenticated and request.user.is_superuser:
        aboutsDB = abouts.objects.get(pk=1)
        skillsDB = skills.objects.all()
        infoDB = information.objects.get(pk=1)
        experienceDB = experience.objects.order_by('-sort_date')
        educationDB = education.objects.order_by('-sort_date')
        return render(request, 'dashboard_about.html',{
            'aboutDB': aboutsDB,
            'skillsDB': skillsDB,
            'infoDB': infoDB,
            'experienceDB': experienceDB,
            'educationDB': educationDB,
        })
    else:
        return HttpResponseRedirect(reverse(dashboard))

def client_edit(request, client_id):
    if request.user.is_authenticated and request.user.is_superuser:
        client = clients.objects.get(pk=client_id)
        if request.method == 'POST':
            clientLink = request.POST['client-link-'+str(client_id)]
            client.Logolink = clientLink
            client.save()
        return HttpResponseRedirect(reverse(dashboard_home))
    else:
        return HttpResponseRedirect(reverse(dashboard))

def info_edits(request):
    if request.user.is_authenticated and request.user.is_superuser:
        infoDB = information.objects.get(pk=1)
        if request.method == 'POST':
            emailAddress = request.POST['emailAddress']
            instaAcc = request.POST['instaAcc']
            whatsNumber = request.POST['whatsNumber']
            linkedinAcc = request.POST['linkedinAcc']
            facebookAcc = request.POST['facebookAcc']
            logo = request.POST['logo']
            infoDB.emailAddress = emailAddress
            infoDB.instaAcc = instaAcc
            infoDB.whatsNumber = whatsNumber
            infoDB.linkedinAcc = linkedinAcc
            infoDB.facebookAcc = facebookAcc
            infoDB.logo = logo
            infoDB.save()
        return HttpResponseRedirect(reverse(dashboard_home))
    else:
        return HttpResponseRedirect(reverse(dashboard))
    
def client_add(request):
    if request.user.is_authenticated and request.user.is_superuser:
        Logolink = request.POST.get('client-link')
        clients.objects.create(Logolink=Logolink)
        return HttpResponseRedirect(reverse(dashboard_home))
    else:
        return HttpResponseRedirect(reverse(dashboard))
    
def client_delete(request, client_id):
    if request.user.is_authenticated and request.user.is_superuser:
        client = clients.objects.get(pk=client_id)
        client.delete()
        return HttpResponseRedirect(reverse(dashboard_home))
    else:
        return HttpResponseRedirect(reverse(dashboard))

def education_delete(request, education_id):
    if request.user.is_authenticated and request.user.is_superuser:
        educatio = education.objects.get(pk=education_id)
        educatio.delete()
        return HttpResponseRedirect(reverse(dashboard_about))
    else:
        return HttpResponseRedirect(reverse(dashboard))

def experience_delete(request, experience_id):
    if request.user.is_authenticated and request.user.is_superuser:
        experienc = experience.objects.get(pk=experience_id)
        experienc.delete()
        return HttpResponseRedirect(reverse(dashboard_about))
    else:
        return HttpResponseRedirect(reverse(dashboard))
def new_education(request):
    if request.user.is_authenticated and request.user.is_superuser:
        title = request.POST.get('education-title')
        time = request.POST.get('education-time')
        sort_date = request.POST.get('education-datetime-sort')
        content = request.POST.get('education-content')
        education.objects.create(title=title, time=time, content=content, sort_date=sort_date)
        return HttpResponseRedirect(reverse(dashboard_about))
    else:
        return HttpResponseRedirect(reverse(dashboard))

def new_experience(request):
    if request.user.is_authenticated and request.user.is_superuser:
        title = request.POST.get('experience-title')
        time = request.POST.get('experience-time')
        sort_date = request.POST.get('experience-datetime-sort')
        content = request.POST.get('experience-content')
        experience.objects.create(title=title, time=time, content=content, sort_date=sort_date)
        return HttpResponseRedirect(reverse(dashboard_about))
    else:
        return HttpResponseRedirect(reverse(dashboard))

def skill_edit(request, skill_id):
    if request.user.is_authenticated and request.user.is_superuser:
        skill = skills.objects.get(pk=skill_id)
        if request.method == 'POST':
            skillTitle = request.POST['skill-title-'+str(skill_id)]
            skill.title = skillTitle
            skill.save()
        return HttpResponseRedirect(reverse(dashboard_about))
    else:
        return HttpResponseRedirect(reverse(dashboard))

def education_edit(request, education_id):
    if request.user.is_authenticated and request.user.is_superuser:
        educatio = education.objects.get(pk=education_id)
        if request.method == 'POST':
            title = request.POST['education-title-'+str(education_id)]
            time = request.POST['education-time-'+str(education_id)]
            sort_date = request.POST['education-datetime-'+str(education_id)]
            content = request.POST['education-content-'+str(education_id)]
            educatio.title = title
            educatio.time = time
            educatio.sort_date = sort_date
            educatio.content = content
            educatio.save()
        return HttpResponseRedirect(reverse(dashboard_about))
    else:
        return HttpResponseRedirect(reverse(dashboard))

def experience_edit(request, experience_id):
    if request.user.is_authenticated and request.user.is_superuser:
        experienc = experience.objects.get(pk=experience_id)
        if request.method == 'POST':
            title = request.POST['experience-title-'+str(experience_id)]
            time = request.POST['experience-time-'+str(experience_id)]
            sort_date = request.POST['experience-datetime-'+str(experience_id)]
            content = request.POST['experience-content-'+str(experience_id)]
            experienc.title = title
            experienc.time = time
            experienc.sort_date = sort_date
            experienc.content = content
            experienc.save()
        return HttpResponseRedirect(reverse(dashboard_about))
    else:
        return HttpResponseRedirect(reverse(dashboard))
    
def home_edit(request):
    if request.user.is_authenticated and request.user.is_superuser:
        h = home.objects.get(pk=1)
        if request.method == 'POST':
            title = request.POST['header-input']
            personalImage = request.POST['personal-image']
            smallContent = request.POST['smallContent']
            h.title = title
            h.personalImage = personalImage
            h.smallContent = smallContent
            h.save()
        return HttpResponseRedirect(reverse(dashboard_home))
    else:
        return HttpResponseRedirect(reverse(dashboard))
def about_edit(request):
    if request.user.is_authenticated and request.user.is_superuser:
        aboutsDB = abouts.objects.get(pk=1)
        if request.method == 'POST':
            TitleText = request.POST.get('header-input')
            personalImage = request.POST.get('personal-image')
            aboutme = request.POST.get('aboutme')
            counterOneName = request.POST.get('counterOneName')
            counterTwoName = request.POST.get('counterTwoName')
            counterThreeName = request.POST.get('counterThreeName')
            counterOneNumber = request.POST.get('counterOneNumber')
            counterTwoNumber = request.POST.get('counterTwoNumber')
            counterThreeNumber = request.POST.get('counterThreeNumber')
            aboutsDB.TitleText = TitleText
            aboutsDB.personalImage = personalImage
            aboutsDB.aboutme = aboutme
            aboutsDB.counterOneName = counterOneName
            aboutsDB.counterTwoName = counterTwoName
            aboutsDB.counterThreeName = counterThreeName
            aboutsDB.counterOneNumber = counterOneNumber
            aboutsDB.counterTwoNumber = counterTwoNumber
            aboutsDB.counterThreeNumber = counterThreeNumber
            aboutsDB.save()
        return HttpResponseRedirect(reverse(dashboard_about))
    else:
        return HttpResponseRedirect(reverse(dashboard))

def dashboard_gallery(request):
    if request.user.is_authenticated and request.user.is_superuser:
        infoDB = information.objects.get(pk=1)
        galleryTitle = gallerys.objects.get(pk=1)
        galleryDB = gallerys.objects.all()
        return render(request, 'dashboard_gallery.html',{
            'infoDB': infoDB,
            'galleryTitle': galleryTitle,
            'galleryDB': galleryDB,
        })
    else:
        return HttpResponseRedirect(reverse(dashboard))
    
def gallery_edit(request, gallery_id):
    if request.user.is_authenticated and request.user.is_superuser:
        gallery = gallerys.objects.get(pk=gallery_id)
        if request.method == 'POST':
            title = request.POST['gallery-title-'+str(gallery_id)]
            type = request.POST['gallery-type-'+str(gallery_id)]
            visitLink = request.POST['gallery-link-'+str(gallery_id)]
            content = request.POST['gallery-content-'+str(gallery_id)]
            photo = request.POST['gallery-photo-'+str(gallery_id)]
            fullWidth = 'gallery-checkbox-' + str(gallery_id) in request.POST
            gallery.title=title
            gallery.type=type
            gallery.visitLink=visitLink
            gallery.content=content
            gallery.photo=photo
            gallery.fullWidth=fullWidth
            gallery.save()
        return HttpResponseRedirect(reverse(dashboard_gallery))
    else:
        return HttpResponseRedirect(reverse(dashboard))
    
def gallery_delete(request, gallery_id):
    if request.user.is_authenticated and request.user.is_superuser:
        gallery = gallerys.objects.get(pk=gallery_id)
        gallery.delete()
        return HttpResponseRedirect(reverse(dashboard_gallery))
    else:
        return HttpResponseRedirect(reverse(dashboard))
    
def new_gallery(request):
    if request.user.is_authenticated and request.user.is_superuser:
        if request.method == 'POST':
            title = request.POST['gallery-title']
            type = request.POST['gallery-type']
            visitLink = request.POST['gallery-link']
            content = request.POST['gallery-content']
            photo = request.POST['gallery-photo']
            fullWidth = request.POST.get('gallery-checkbox') == 'on'
            gallerys.objects.create(type=type, title=title, visitLink=visitLink, fullWidth=fullWidth, photo=photo, content=content)
        return HttpResponseRedirect(reverse(dashboard_gallery))
    else:
        return HttpResponseRedirect(reverse(dashboard))
    
def gallery_header_edit(request):
    infoDB = information.objects.get(pk=1)
    if request.user.is_authenticated and request.user.is_superuser:
        gallery = gallerys.objects.get(pk=1)
        if request.method == 'POST':
            HeaderTitle = request.POST['header-input']
            gallery.pageTitle = HeaderTitle
            gallery.save()
        return render(request, 'dashboard_gallery.html',{
            'infoDB': infoDB,
        })
    else:
        return HttpResponseRedirect(reverse(dashboard))
    
def dashboard_bts(request):
    infoDB = information.objects.get(pk=1)
    btsDB = bts.objects.all().order_by('pk')
    firstBTS = bts.objects.get(pk=1)
    if request.user.is_authenticated and request.user.is_superuser:
        if request.method == 'POST':
            header = request.POST['header-input']
            firstBTS.header = header
            firstBTS.save()
        return render(request, 'dashboard_bts.html',{
            'infoDB': infoDB,
            'btsDB': btsDB,
            'firstBTS': firstBTS
        })
    else:
        return HttpResponseRedirect(reverse(dashboard))
def bts_new(request):
    if request.user.is_authenticated and request.user.is_superuser:
        if request.method == 'POST':
            photoLink = request.POST['bts-photo']
            bts.objects.create(photoLink=photoLink)
        return HttpResponseRedirect(reverse(dashboard_bts))
    else:
        return HttpResponseRedirect(reverse(dashboard))
def bts_edit(request, bts_id):
    if request.user.is_authenticated and request.user.is_superuser:
        if request.method == 'POST':
            btsSelected = bts.objects.get(pk=bts_id)
            photoLink = request.POST['bts-link-'+str(bts_id)]
            btsSelected.photoLink = photoLink
            btsSelected.save()
        return HttpResponseRedirect(reverse(dashboard_bts))
    else:
        return HttpResponseRedirect(reverse(dashboard))
    
def bts_delete(request, bts_id):
    if request.user.is_authenticated and request.user.is_superuser:
        if request.method == 'POST':
            btsSelected = bts.objects.get(pk=bts_id)
            btsSelected.delete()
        return HttpResponseRedirect(reverse(dashboard_bts))
    else:
        return HttpResponseRedirect(reverse(dashboard))
def behindthescenes(request):
    infoDB = information.objects.get(pk=1)
    firstBTS = bts.objects.get(pk=1)
    btsDB = bts.objects.all().order_by('pk')
    return render(request, 'bts.html',{
        'infoDB': infoDB,
        'btsDB': btsDB,
        'firstBTS': firstBTS
    })
