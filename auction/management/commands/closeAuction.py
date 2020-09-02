from django.core.management.base import BaseCommand, CommandError
#This is the layout of a basic command layout
from auction.models import Auction
from django.utils import timezone
import datetime

def getallOpenAuctions():
    return Auction.objects.filter(Stats = True)

class Command(BaseCommand):
    help = 'Close Open Auctions'

    #if the argument doesnt is optionsal you can add double dash to it e.g. '--name'

    def handle(self, *args, **options):
        self.stdout.write("Closing Opened Auctions....")

        try:
            closeAuctions = ""
            for auc in getallOpenAuctions():

                if(auc.AuctionEnd == None):
                    print(str(auc.ID) + " has no closeTime")

                else:

                    date_time_str = str(auc.AuctionEnd)[0:19]
                    date_time_obj = datetime.datetime.strptime(date_time_str, '%Y-%m-%d %H:%M:%S')
                    if (datetime.datetime.now() > date_time_obj and auc.Stats == True):
                        Auction.objects.filter(ID = auc.ID).update(Stats=False)
                        closeAuctions +=auc.Name + ", "

            self.stdout.write("Cloing Completed")
            if len(closeAuctions) > 1:
                self.stdout.write("Cloing Auctions : %s" %closeAuctions[:-2])

        except:
            print("fail")
