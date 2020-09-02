from django_cron import CronJobBase, Schedule
import os


class closeAuction(CronJobBase):
    RUN_EVERY_MINS = 1 # every 1 minute

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'auction.cron.MyCronJob.closeAuction'    # a unique code

    def do(self):
        os.system('python manage.py closeAuction')
        pass    # do your thing here
