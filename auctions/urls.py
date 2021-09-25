from django.urls import path

from . import views

urlpatterns = [
    path("time/", views.set_timezone, name="set_timezone"),
    path("", views.index, name="index"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("register/", views.register, name="register"),
    path("profile/", views.profile, name="profile"),
    path("my_listings/", views.my_listings, name="my_listings"),
    path("my_wins/", views.my_wins, name="my_wins"),
    path("dont_won/", views.dont_won, name="dont_won"),
    path("i_am_bidding/", views.i_am_bidding, name="i_am_bidding"),
    path("create_listing/", views.create_listing, name="create_listing"),
    path("listing/<str:id>/", views.listing, name="listing"),
    path("listing/<str:id>/bid/", views.bid, name="bid"),
    path("listing/<int:id>/watchlist/",
         views.watchlist_switch, name="watchlist_add_remove"),
    path("comment/", views.comment, name="comment"),
    path("watchlist/", views.watchlist, name="watchlist"),
    path("categories/", views.categories, name="categories"),
    path("categories/<str:category_name>/", views.category, name="category"),
    path("user/<str:username>/listings",
         views.user_listings, name="user_listings"),
    path("search/", views.search, name="search"),
    path("search/<str:searched>/", views.search_results, name="search_results"),
]
