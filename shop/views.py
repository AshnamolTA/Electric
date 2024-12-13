from django.shortcuts import render,redirect

# from django.forms import BaseModelForm

# from django.http import HttpResponse

from django.urls import reverse_lazy

from django.views.generic import View,FormView,TemplateView,DetailView

from django.contrib.auth import authenticate,login,logout

from shop.forms import SignUpForm,SignInForm,UserProfileForm


from shop import views

from shop.models import Light,UserProfile,Category


class SignUpView(View):

    template_name="signup.html"

    form_class=SignUpForm

    def get(self,request,*args,**kwargs):

        form_instance=self.form_class

        return render(request,self.template_name,{"form":form_instance})
    
    def post(self,request,*args,**kwargs):

        form_instance=self.form_class(request.POST)

        if form_instance.is_valid():

            form_instance.save()

            print("Account Created")

            return redirect("signin")
        
        else:

            print("Failed To Create Account")
            
            
            return render(request,"login.html",{"form":form_instance})
        
class IndexView(TemplateView):

    template_name="index.html"

    def get(self,request,*args,**kwargs):

        qs=Category.objects.all()

        return render(request,self.template_name,{"data":qs})
        

class SignInView(FormView):

    template_name="login.html"

    form_class=SignInForm

    def post(self,request,*args,**kwargs):
        
        form_instance=self.form_class(request.POST)

        if form_instance.is_valid():

            uname=form_instance.cleaned_data.get("username")

            pwd=form_instance.cleaned_data.get("password")

            user_object=authenticate(username=uname,password=pwd)

            if user_object:

                login(request,user_object)

                return redirect("index")
            
        return render(request,self.template_name,{"form":form_instance})
    
class LogoutView(View):

    def get(self,request,*arga,**kwargs):
         
         logout(request)

         return redirect("signin")
    


class UserProfileEditView(View):

    template_name="profile_edit.html"

    form_class=UserProfileForm

    def get(self,request,*args,**kwargs):

        user_profile_instance=request.user.profile

        form_instance=self.form_class(instance=user_profile_instance)

        return render(request,self.template_name,{"form":form_instance})
    
    def post(self,request,*args,**kwargs):

        user_profile_instance=request.user.profile

        form_instance=self.form_class(request.POST,instance=user_profile_instance,files=request.FILES)

        if form_instance.is_valid():

            form_instance.save()

            return redirect("index")

        return render(request,self.template_name,{"form":form_instance})
    
class LightDetailView(DetailView):

    template_name="light_detail.html"
    
    context_object_name="light"

    model=Light


    

        
    
