from django.urls import path
from myapp import views
app_name="myapp"

urlpatterns = [
    path('trail/',views.trail,name="Trail"),
    path('profile/',views.profile,name="profile"),
    path('get_demo/',views.get_demo,name="get_demo"),
    path('post_demo/',views.post_demo,name="post_demo"),
    path('register/',views.register,name="register"),
    path('multiselect/',views.multiselect,name="multiselect"),
    path('img/',views.img_upld,name="img"),
    path('img_display/',views.img_display,name="img_display"),
    path('builtin/',views.builtinforms,name="builtinforms"),
]
