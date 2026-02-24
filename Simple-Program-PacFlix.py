from tabulate import tabulate 

data = {
    "Shandy": ["Basic Plan", 12, "shandy-2134"],
    "Cahya": ["Standard Plan", 24, "cahya-abcd"],
    "Ana": ["Premium Plan", 5, "ana-2f9g"],
    "Bagus": ["Basic Plan", 11, "bagus-9f92"]
}  # Database PacFlix

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


class User:
    def __init__(self,username):
        username = username.lower()
        self.username = username.capitalize()


    def check_benefit(self):
        print(tabulate(benefit_plan, headers='firstrow', \
                       tablefmt='mixed_grid', maxcolwidths=[20,25,25,25]))
    

    def check_plan(self):
        if self.username not in data.keys():
            raise Exception('Maaf, anda tidak sedang berlangganan.')
        else:
            self.current_plan = data[self.username][0]  # plan yg sdng digunakan
            self.duration_plan = data[self.username][1] # durasi plan yg sdng digunakan
            benefit_current_plan = [[x[0],x[benefit_plan[0].index(self.current_plan)]] 
                                    for x in benefit_plan
                                   ] # tabel benefit plan yang sedang digunakan user
            
            print(f'Kamu sedang berlangganan {self.current_plan} dengan '
                  f'durasi {self.duration_plan} bulan.')
            print(f'Berikut merupakan tabel benefit {self.current_plan}')
            print(tabulate(benefit_current_plan,headers='firstrow',tablefmt='mixed_grid'))


    def upgrade_plan(self,new_plan):
        if self.username not in data.keys():
            raise Exception('Maaf, anda tidak sedang berlangganan.')
        else:
            self.current_plan = data[self.username][0]
            self.duration_plan = data[self.username][1]
            index_current_plan = benefit_plan[0].index(self.current_plan)
            index_new_plan = benefit_plan[0].index(new_plan)
            if index_new_plan >= index_current_plan:
                '''
                pernyataan 'index_new_plan >= index_current_plan' bertujuan untuk
                mengecek apakah user upgrade ke plan lebih di atas atau downgrade. 
                Jika indeksnya lebih dari atau sama dengan maka berarti upgrade 
                dan sebaliknya.
                '''
                if self.duration_plan > 12:
                    new_plan_price = benefit_plan[-1][index_new_plan]
                    discount = 5/100

                    final_price = new_plan_price - new_plan_price * discount

                    print(f'Total biaya langganan ke {new_plan} adalah Rp{int(final_price):_}')
                else:
                    final_price = benefit_plan[-1][index_new_plan]
                    
                    print(f'Total biaya langganan ke {new_plan} adalah Rp{final_price:_}')
            else:
                raise Exception('Maaf, tidak bisa berlangganan downgrade plan.')


class NewUser:
    def __init__(self,username):
        username = username.lower()
        self.username = username.capitalize()


    def check_benefit(self):
        print(tabulate(benefit_plan, headers='firstrow', \
                       tablefmt='mixed_grid', maxcolwidths=[20,25,25,25]))
        
    
    def pick_plan(self,new_plan,referral_code):
        # membuat list referral_code dari database
        referral_code_list = []
        for key in data:
            referral_code_list.append(data[key][-1]) 
        
        # perhitungan biaya plan
        if referral_code in referral_code_list:
            index_new_plan = benefit_plan[0].index(new_plan)
            discount = 4/100
            new_plan_price = benefit_plan[-1][index_new_plan]
            final_price = new_plan_price - new_plan_price * discount
            print(f'Total biaya langganan ke {new_plan} adalah Rp{final_price:_}')
        else:
            index_new_plan = benefit_plan[0].index(new_plan)
            final_price = benefit_plan[-1][index_new_plan]
            print(f'Total biaya langganan ke {new_plan} adalah Rp{final_price:_}')

                