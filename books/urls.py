from django.urls import path

from .views import my_homepage,history,history1, \
history2,history3,history4,history5, \
articles, article1, article2, article3, dict,prose,prose1, \
mail, forum, discussion, UserRegister, UserLogin, UserLogout, myprofile

urlpatterns=[
    path('', my_homepage),
	path('history/', history),
	path('history/history1/', history1),
	path('history/history2/', history2),
	path('history/history3/', history3),
	path('history/history4/', history4),
	path('history/history5/', history5),
	path('articles/', articles),
	path('articles/article1/', article1),
	path('articles/article2/', article2),
	path('articles/article3/', article3),
	path('dict/', dict),
	path('prose/', prose),
	path('prose/prose1/', prose1),
	path('mail/', mail),
	path("forum/",forum, name="Forum"),
    path("discussion/<int:myid>/",discussion, name="Discussions"),
    path("register/",UserRegister, name="Register"),
    path("login/",UserLogin, name="Login"),
    path("logout/",UserLogout, name="Logout"),
    path("myprofile/",myprofile, name="Myprofile"),
]