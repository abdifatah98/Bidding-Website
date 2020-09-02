import os
from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse
from django.template import loader

from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

from .models import Auction

from .forms import CustomUserCreationForm, AuctionForm

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

def home(request):
    return render(request, 'home.html', {})

def health(request):
    return HttpResponse(PageView.objects.count())

def auctionListjson(request):
    return JsonResponse({'auctions': list(Auction.objects.values())})

def auctionList(request):
    return render(request, 'auction/auction_List.html', {})

def createAuction(request):
    if request.method == 'POST':
        form = AuctionForm(request.POST)
        if form.is_valid():
            Name = form.cleaned_data['Name']
            Description = form.cleaned_data['Description']
            AuctionEnd = form.cleaned_data['AuctionEnd']
            Stats = form.cleaned_data['Stats']
            CurrentPrice = form.cleaned_data['CurrentPrice']
            auction = Auction(Name=Name, Description=Description, AuctionEnd=AuctionEnd, Stats=Stats, CurrentPrice=CurrentPrice)
            auction.save()
            return redirect('home')
        else:
            return HttpResponse('Invalid Form')

    form = AuctionForm
    return render(request, 'auction/create_Auction.html', {'form':form})


def search_auctions(request):
    if request.method == "POST":
        search_Auctions = request.POST['search_text']
    else:
        search_Auctions = ""

    auctions = Auction.objects.filter(Name__contains = search_Auctions)
    print(auctions)
    return JsonResponse({'auctions' : list(auctions.values())})

def auctionView(request,AuctionID):
    auct = Auction.objects.get(ID = AuctionID)

    context = {
    'AID' : auct.ID,
    'AName' : auct.Name,
    'ADescription' : auct.Description,
    'AAuctionEnd' : auct.AuctionEnd,
    'ACurrentPrice' : auct.CurrentPrice,
    }

    return render(request, 'auction/bidding_Page.html', context)

def placeBid(request):
    if request.method == "POST":
        bidONAuction = request.POST['Aid']
    else:
        bidONAuction = ""

    bidder = (request.POST['userName'])
    newbid = int(request.POST['amountt'])

    curauc = Auction.objects.get(ID = bidONAuction)
    if(curauc.CurrentPrice < newbid and curauc.HighestBidder != Accounts.objects.get(username = bidder)):
        temp = Auction.objects.filter(ID = bidONAuction).update(CurrentPrice = newbid, HighestBidder = Accounts.objects.get(username = bidder))
        temp.save()

    return HttpResponse("200")
