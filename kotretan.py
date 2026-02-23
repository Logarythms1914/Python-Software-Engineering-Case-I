from tabulate import tabulate 
from database import data  # mengambil data-data yang ada di database

class User:
    def __init__(self,username):
        self.username = username
    

    def check_benefit(self):
        benefit_plan = [['Services', 'Basic Plan', 'Standard Plan', 'Premium Plan'],
                        ['can_stream:', True, True, True],
                        ['can_download:', True, True, True],
                        ['has_SD:', True, True, True],
                        ['has_HD:', False, True, True],
                        ['has_UHD:', False, False, True],
                        ['num_of_devices:', 1, 2, 4],
                        ['content:', '3rd party movie only', 
                         'Basic Plan Content + Sports (F1, Footbal, Basketball)',
                         'Basic Plan + Standard Plan + PacFlix Original Series or Movie'],
                         ['price (Rp):', 120_000, 160_000, 200_000]
                       ]
        print(tabulate(benefit_plan, headers='firstrow', \
                       tablefmt='mixed_grid', maxcolwidths=[20,25,25,25]))
