from tabulate import tabulate 

data = {
    "Shandy": ["Basic Plan", 12, "shandy-2134"],
    "Cahya": ["Standard Plan", 24, "cahya-abcd"],
    "Ana": ["Premium Plan", 5, "ana-2f9g"],
    "Bagus": ["Basic Plan", 11, "bagus-9f92"]
}  # Database PacFlix


class User:
    def __init__(self,username):
        username = username.lower()
        self.username = username.capitalize()
    
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
                    ]  # tabel semua plan dan benefitnya

    def check_benefit(self):
        print(tabulate(self.benefit_plan, headers='firstrow', \
                       tablefmt='mixed_grid', maxcolwidths=[20,25,25,25]))
    

    def check_plan(self):
        if self.username not in data.keys():
            raise Exception('Maaf, anda tidak sedang berlangganan.')
        else:
            self.current_plan = data[self.username][0]
            self.duration_plan = data[self.username][1]
            print(f'Kamu sedang berlangganan {self.current_plan} dengan '
                  f'durasi {self.duration_plan} bulan.')
            print(f'Berikut merupakan tabel benefit {self.current_plan}')
            benefit_current_plan = [[x[0],x[self.benefit_plan[0].index(self.current_plan)]] 
                                    for x in self.benefit_plan
                                   ] # tabel benefit plan yang sedang digunakan user
            print(tabulate(benefit_current_plan,headers='firstrow',tablefmt='mixed_grid'))
        
