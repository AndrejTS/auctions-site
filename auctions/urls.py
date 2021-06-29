from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("register/", views.register, name="register"),
    path("profile/", views.profile, name="profile"),
    path("user_listings/", views.user_listings, name="user_listings"),
    path("user_wins/", views.user_wins, name="user_wins"),
    path("create_listing/", views.create_listing, name="create_listing"),
    path("close_listing/", views.close_listing, name="close_listing"),
    path("listing/<str:id>/", views.listing, name="listing"),
    path("bid/", views.bid, name="bid"),
    path("comment/", views.comment, name="comment"),
    path("watchlist/", views.watchlist, name="watchlist"),
    path("categories/", views.categories, name="categories"),
    path("categories/<str:category_name>/", views.category, name="category"),
]
