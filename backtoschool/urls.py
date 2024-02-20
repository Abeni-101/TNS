from backtoschool import views
from django.urls import path

urlpatterns = [
path("home/",views.home,name="home"),
path("register/",views.registerpage,name="registerpage"),
path("login/",views.loginpage,name="loginpage"),
path("logout/",views.logoutpage, name="logoutpage"),
path("account_setting/", views.account_settings,name="account_settings"),
path("search/",views.search_student,name="search"),
path("more_info/<int:pk>/",views.more_info,name="more_info"),
path("news/",views.create_news,name="news"),
path("view_news/",views.view_news,name="view_news"),
path("detail_news/<int:pk>/",views.detail_news,name="detail_news"),
path("create_assignment/",views.create_assignment,name="create_assignment"),
path("view_assignment/",views.view_assignment,name="view_assignment"),
path("submit_ass/<int:pk>/",views.submit_assignment,name="submit_ass"),
path("all_assignments/",views.give_res ,name="give_res"),
path("show_result/<int:pk>/",views.show_result,name="show_result"),
path("list/",views.list_result,name="list"),
path("see/<int:pk>/",views.see_result,name="see"),
path("delete/<int:pk>/",views.delete_ass,name="delete_ass")
]