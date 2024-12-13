from django.urls import path

from shop import views


urlpatterns = [
    path("register/",views.SignUpView.as_view(),name="signup"),
    path("",views.SignInView.as_view(),name="signin"),
    path("index/",views.IndexView.as_view(),name="index"),
    path('logout',views.LogoutView.as_view(),name="signout"),
    path('profile/change/',views.UserProfileEditView.as_view(),name="profile_edit"),
    path("light/<int:pk>/",views.LightDetailView.as_view(),name='light_detail')
]
