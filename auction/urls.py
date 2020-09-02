from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('Auction_List',views.auctionList,name='auction List'),
    path('<int:AuctionID>',views.auctionView,  name='single Auction'),
    path('place_bid',views.placeBid, name ='placeBid'),
    path('Auction_List.json',views.auctionListjson,name='list of auctions'),
    path('create_Auction',views.createAuction, name='create Auction'),
    path('health', lambda request : HttpResonse('okay')),
    path('search.json',views.search_auctions,name="search Bar")
]
