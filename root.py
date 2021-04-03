
print('\n---------- Welcome to Sarah Travel Agency ----------')

print("\n Our available packages: ")
print(' Package1. 4 days to 3 night \n Package2. 5 days to 4 night \n Package3. 7 days to 6 night \n')

for i in range(1, 4):
    print(" Package{} for #enter: {}".format(i, i))


choose = int(input('\nPlease select your package: '))


class package:
    def package1(self):
        pass
    def package2(self):
        pass
    def package3(self):
        pass
    
    def sort(self):
        self.package1()
        self.package2()
        self.package3()
        

class tourPlace(package):
    if choose==1:
        def package1(self):
            print("\nPlace: Dhaka to Chandpur  Price: 500tk  #Select for enter: 1")
            print("Place: Dhaka To Cox's Bazar  Price: 800tk  #Select for enter: 2")
                        
            cho = int(input('\nPlease select your favorite place: '))
            if cho==1:
                print("\nBooking now for Dhaka to Chandpur")
                book = int(input('\nPlease enter 1 to confirm booking: '))
                if book==1:
                    print('\nThanks, your booking has been successful. Have a nice trip.')
                else:
                    print('You must enter 1 to confirm the booking')
            elif cho==2:
                print("\nBooking now for Dhaka to Cox's bazar")
                book = int(input('\nPlease enter 1 to confirm booking: '))
                if book==1:
                    print('\nThanks, your booking has been successful. Have a nice trip')
                else:
                    print('You must enter 1 to confirm the booking')
            

    elif choose==2:
        def package2(self):
            print("\nPlace: Dhaka To Cox's Bazar  Price: 1000tk  #Select for enter: 1")
            print("Place: Dhaka to Srimongol to Sylhet  Price: 1400tk  #Select for enter: 2")
            
            cho = int(input('\nPlease select your favorite place: '))
            if cho==1:
                print("\nBooking now for Dhaka To Cox's Bazar")
                book = int(input('Please enter 1 to confirm booking: '))
                if book==1:
                    print('\nThanks, your booking has been successful. Have a nice trip.')
                else:
                    print('You must enter 1 to confirm the booking')
            elif cho==2:
                print("\nBooking now for Dhaka to Srimongol to Sylhet")
                book = int(input('\nPlease enter 1 to confirm booking: '))
                if book==1:
                    print('\nThanks, your booking has been successful. Have a nice trip')
                else:
                    print('You must enter 1 to confirm the booking')

    elif choose==3:
        def package3(self):
            print("\nPlace: Dhaka to Srimongol to Sylhet  Price: 1600tk  #Select for enter: 1")
            print("Place: Dhaka to Sundarbon to Cox’s Bazar to Sylhet  Price: 1900tk  #Select for enter: 2")
            
            cho = int(input('\nPlease select your favorite place: '))
            if cho==1:
                print("\nBooking now for Dhaka to Srimongol to Sylhet")
                book = int(input('\nPlease enter 1 to confirm booking: '))
                if book==1:
                    print('\nThanks, your booking has been successful. Have a nice trip.')
                else:
                    print('You must enter 1 to confirm the booking')
            elif cho==2:
                print("\nBooking now for Dhaka to Sundarbon to Cox’s Bazar to Sylhet")
                book = int(input('\nPlease enter 1 to confirm booking: '))
                if book==1:
                    print('\nThanks, your booking has been successful. Have a nice trip')
                else:
                    print('You must enter 1 to confirm the booking')
            


t=tourPlace()
t.sort()