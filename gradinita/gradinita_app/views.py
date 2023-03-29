from django.shortcuts import render,redirect

from .forms import CustomUserCreationForm ,  ProfileForm ,EditPasswordForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login ,authenticate ,logout 
from .models import Profile ,Kids   , absente_elev , motivari_elev
from django.contrib.auth.hashers import check_password
from django.contrib.auth.hashers import make_password
from django.contrib.auth.forms import UserCreationForm  
from .forms import KidsForm  , absente_elevForm , motivari_elevForm
# Create your views here.
from django.contrib import messages
from django.contrib.admin.views.decorators import staff_member_required
from django.core.mail import send_mail
from django.conf import settings
import random
import string

def navbar(request):
    return render(request,"navbar.html")

def home(request):
    return render(request,"home.html")



def inscrie(request):
     form = CustomUserCreationForm()
     if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            kid2 = request.POST['kid']
            user = form.save(commit=False)
            child=Kids.objects.get(full_name=kid2)
            if child is not None:
                    if child.parent:
                        return render(request,"sorry.html")
                    
                    user.save()
                    profile = Profile.objects.create(
                        owner=user,
                        username=user.username,
                        name=user.first_name,
                        last_name=user.last_name,
                        email=user.email,
                        kid=kid2
                    )
                    profile.save()
                    child.parent=profile
                    child.save()

                    send_mail(
                        profile.username,
                        "Contul tau a fost creat!",
                        settings.EMAIL_HOST_USER,
                        [profile.email],
                        fail_silently=False,
                    )

                    return redirect('home')
     return render(request,"inscriere.html",{"form":form})


def delete(request,pk):
    user = User.objects.get(id=pk)
    user.delete()
    return redirect('inscriere')
def update(request,pk):
    if  request.method == 'POST':
        user = User.objects.get(id=pk)   
        PROFILE = Profile.objects.get(owner=user)
        profile = ProfileForm(request.POST,request.FILES,instance=PROFILE)
        if profile.is_valid():
            profile.save()
            user.first_name=request.POST['name']
            user.last_name=request.POST['last_name']
            user.username = request.POST['username']
            user.email = request.POST['email']
            return redirect("account",pk=user.id)
        return render(request,"sorry.html")
    return redirect('home')
        



def changepassword(request,pk):
    form = EditPasswordForm()
    user = User.objects.get(id=pk)
    profile = Profile.objects.get(owner=user)
    if request.method=='POST':
        form = EditPasswordForm(request.POST)

        if form.is_valid():
            password1 = request.POST['password1']  
            old_password=request.POST['oldpassword'] 
            current_password=user.password    
            equality=check_password(old_password,current_password)
            if equality  :    
                messages.success(request, "Un cod pentru parola a fost trimis pe gmail!" )  
                return redirect('gmail',pk=pk,newpassword=password1)      
                    

            messages.success(request, "Old password must match with the current one!" )  
        else:
            messages.success(request,"Passwords must match")
    return redirect('account',pk=pk)
    


def verification_gmail(request,pk,newpassword):
    user = User.objects.get(id=pk)
    profile = Profile.objects.get(owner=user)
    hash =random()
    send_mail(
            profile.username,
              hash,
             settings.EMAIL_HOST_USER,
            [profile.email],
             fail_silently=False,
    )
   
    if request.method=='POST':
        form = request.POST['email_verification']
        
        if hash == form:
               user.set_password(newpassword)
               user.save()
               messages.success(request,"You password is changed!")
               return redirect('account',pk)

        else:
               messages.success(request,"Gmail verification code is wrong!")
               return redirect('account',pk)

    return render(request,"verificare.html")


def catalog(request):
    
    pag = int(0)

    if 'catalog_form' in request.POST:
        form = request.POST['kids']
        kids = Kids.objects.filter(group=form)[:3]
       



        context={'kid':kids,'group':form,'pag':pag}
        return render(request,"catalog.html",context)
    
    if request.method == 'POST':
        grupa = request.POST['group']
        pag  = int(request.POST['page'])
        if pag<0:
            pag=int(0)
        kids = Kids.objects.filter(group=grupa)[pag*3:pag*3+3]
        context={'kid':kids,'group':grupa,'pag':pag}
        return render(request,"catalog.html",context)


def account(request,pk):
    user = User.objects.get(id=pk)
    profile = Profile.objects.get(owner=user)
    kid = Kids.objects.filter(parent=profile)
    edit_password = EditPasswordForm()
    formprofile = ProfileForm(instance=profile)
    context = {"profile" : profile,"password":edit_password,"formprofile":formprofile,"kid":kid}
    return render(request,"account.html",context)

def kid_account(request,pk):
    kid = Kids.objects.get(id=pk)
    motivari = motivari_elev.objects.filter(owner=kid)
    absente=absente_elev.objects.filter(owner=kid)
    context={'profile':kid,'abs':absente,'motv':motivari}
    return render(request,"profile_kid.html",context)

def logoutUser(request):
        logout(request)
        return redirect('home')
def kid_register(request):
    form = KidsForm()
    if request.method=='POST':
        form = KidsForm(request.POST)
        if form.is_valid():
            kid = form.save(commit=False)
            kid.absente=0
            kid.motivari=0
            kid.save()
            absente = absente_elev.objects.create(
                owner = kid,
                numar=0,
                
            )
            motivari = motivari_elev.objects.create(
                owner=kid,
                numar=0
            )
            return redirect("home")  
        return render(request,"sorry.html")
    return render(request,"register_kid.html",{"form":form})


def kid_account(request,pk):
    chield = Kids.objects.get(id=pk)
    
    return render(request,"account_kid.html",{"kid":chield})

def request_kid(request,pk):
        parent = User.objects.get(id=pk)
        profile = Profile.objects.get(owner=parent)
        kid = Kids.objects.get(parent=profile)
        return render(request,"account_kid.html",kid.id,{"kid":kid})

def absente_motivari(request,pk):
    kid =Kids.objects.get(id=pk)
    absente=absente_elev.objects.filter(owner=kid)
    motivari=motivari_elev.objects.filter(owner=kid)
    
    
    form_abs = absente_elevForm()
    form_mot= motivari_elevForm()
    form_kid = KidsForm(instance=kid)

    context ={'absente':absente,'motivari':motivari,'kid':kid,'form':form_kid,'form_absente':form_abs,'form_motivare':form_mot}
    return render(request,"absente_motivari.html",context)

def update_kid(request,pk):
    kid=Kids.objects.get(id=pk)
    if request.method=='POST':
       form = KidsForm(request.POST,request.FILES,instance=kid)
       if form.is_valid():
            form.save()
            return redirect('absente_motivari',pk=pk)

def adauga_copil_PARINTE(request,pk):
    user = User.objects.get(id=pk)
    parent=Profile.objects.get(owner=user)
    if request.method=='POST':
        fullname=request.POST['fullname']
        try:
            kid = Kids.objects.get(full_name=fullname)
        except:
            kid=None
            messages.success(request,"KID NAME INCORRECT")
            return redirect("account",pk=pk)

        if kid is not None:
            kid.parent=parent
            kid.save()
            messages.success(request,"KID ADDED ")
            return redirect("account",pk=pk)

def delete_absenta(request,pk,pk2):
    absenta = absente_elev.objects.get(id=pk)
    kid=Kids.objects.get(id=pk2)
    kid.absente=kid.absente-absenta.numar
    if kid.absente<0:
        kid.absente=0
    kid.save()
    absenta.delete()
    return redirect("absente_motivari",pk=pk2)
def delete_motivare(request,pk,pk2):
    kid = Kids.objects.get(id=pk2)
    motivare = motivari_elev.objects.get(id=pk)
    kid.motivari=kid.motivari-motivare.numar
    if kid.motivari<0:
        kid.motivari=0
    kid.save()
    motivare.delete()
    return redirect("absente_motivari",pk=pk2)

def adauga_motivare(request,pk):
    kid = Kids.objects.get(id=pk)
    form = motivari_elevForm()
    if request.method=='POST':
        form = motivari_elevForm(request.POST)
        if form.is_valid():
            motivare = motivari_elev.objects.create(
                owner=kid,
                data=request.POST['data'],
                numar=request.POST['numar']
            )
            motivare.save()
            kid.motivari=int(motivare.numar)+int(kid.motivari)
            kid.save()
            return redirect("absente_motivari",pk=pk)

    return redirect("home")
           
def about_us(request):
    return render(request,"aboutus.html")




def adauga_absenta(request,pk):
    kid = Kids.objects.get(id=pk)
    form = absente_elevForm()
    if request.method=='POST':
        form = absente_elevForm(request.POST)
        if form.is_valid():
            absenta = absente_elev.objects.create(
                owner=kid,
                data=request.POST['data'],
                numar=request.POST['numar']
            )
            absenta.save()
            kid.absente=int(absenta.numar)+int(kid.absente)
            kid.save()
            return redirect("absente_motivari",pk=pk)

    return redirect("home")



def page_kids(request):
    return render(request,"page1.html")







####PASSWORD FIELDS
def loginUser(request):
    password = EditPasswordForm()
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        try:
            user = User.objects.get(email=email)
        except:
            pass
        user = authenticate(request,username=username,password=password,email=email)
        if user is not None:
            login(request,user)
            profile = Profile.objects.get(owner=user)
            return redirect("home")
        else:
            pass
    return render(request,'login.html',{'password':password})
    

def password_lost(request):
    if request.method=='POST':
        password_form=EditPasswordForm(request.POST)

        if password_form.is_valid():
            password1 = request.POST['password1']
            email = request.POST['email']
            messages.success(request, "Un cod pentru parola a fost trimis pe gmail!" )  
            length = 10
            characters = string.ascii_letters + string.digits
            code = ''.join(random.choice(characters) for i in range(length))
            send_mail(
                        "Password verification",
                        code,
                        settings.EMAIL_HOST_USER,
                        [email],
                        fail_silently=False,
             )
            return redirect('password_lostGmail',password=password1,email=email,code=code)
        messages.success(request,"Passwords must match!")
        return redirect('login')

def password_lost_EmailVerif(request,password,email,code):
    if request.method=='POST':
        gmail_code = request.POST['code']
        if code == gmail_code:
            user = User.objects.get(email=email)
            messages.success(request,"PASSWORD WAS SUCCESFULLY CHANGED!")
            user.set_password(password)
            user.save()
            login(request,user)
            return redirect("account",user.id)
        messages.success(request,"Gmail code is wrong")
        return redirect('login')
    return render(request,"verificare_passwordCode.html")