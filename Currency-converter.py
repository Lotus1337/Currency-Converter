#Currency converter

#Currency conveter for the top 5 most used currencies in the world (USD, EUR, JPY, CHN, GBP)

#USD converting to others

def USDtoEUR(x):
    return x * 0.84

def USDtoJPY(x):
    return x * 104.07

def USDtoCHN(x):
    return x * 6.58

def USDtoGBP(x):
    return x * 0.75

#EUR converting to others

def EURtoUSD(x):
    return x * 1.2

def EURtoJPY(x):
    return x * 124.50

def EURtoCHN(x):
    return x * 7.87

def EURtoGBP(x):
    return x * 0.9

#JPY converting to others

def JPYtoUSD(x):
    return x * 0.0096

def JPYtoEUR(x):
    return x * 0.0080

def JPYtoCHN(x):
    return x * 0.063

def JPYtoGBP(x):
    return x * 0.0072

#CHN converting to others

def CHNtoUSD(x):
    return x * 0.15

def CHNtoEUR(x):
    return x * 0.13

def CHNtoJPY(x):
    return x * 15.83

def CHNtoGBP(x):
    return x * 0.11

#GBP converting to others

def GBPtoUSD(x):
    return x * 1.33

def GBPtoEUR(x):
    return x * 1.11

def GBPtoJPY(x):
    return x * 138.62

def GBPtoCHN(x):
    return x * 8.76

#Conversion selection

print("Select conversion")
print("1. USD converting to others")
print("2. EUR converting to others")
print("3. JPY converting to others")
print("4. CHN converting to others")
print("5. GBP converting to others")

while True:
    choice = input("Enter choice (1/2/3/4/5): ")

    if choice in ('1', '2', '3', '4', '5'):

        #conversion selection for USD to others

        if choice == '1':
            print("Select Conversion")
            print("1. USD convert to EUR")
            print("2. USD convert to JPY")
            print("3. USD convert to CHN")
            print("4. USD convert to GBP")

            while True:
                choice = input("Enter choice (1/2/3/4): ")

                #outputs for USD converting to others

                if choice in ('1', '2', '3', '4'):
                    amountUSD = float(input("Enter amount of USD: "))
                    if choice == '1':
                        print(amountUSD, "to EUR", "=", USDtoEUR(amountUSD))

                    elif choice == '2':
                        print(amountUSD, "to JPY", "=", USDtoJPY(amountUSD))

                    elif choice == '3':
                        print(amountUSD, "to CHN", "=", USDtoCHN(amountUSD))

                    elif choice == '4':
                        print(amountUSD, "to GBP", "=", USDtoGBP(amountUSD))
                    break

        #conversion selection for EUR to others

        elif choice == '2':
            print("Select Conversion")
            print("1. EUR convert to USD")
            print("2. EUR convert to JPY")
            print("3. EUR convert to CHN")
            print("4. EUR convert to GBP")

            while True:
                choice = input("Enter choice (1/2/3/4): ")

                #outputs for EUR converting to others

                if choice in ('1', '2', '3', '4'):
                    amountEUR = float(input("Enter amount of EUR: "))
                    if choice == '1':
                        print(amountEUR, "to USD", "=", EURtoUSD(amountEUR))

                    elif choice == '2':
                        print(amountEUR, "to JPY", "=", EURtoJPY(amountEUR))

                    elif choice == '3':
                        print(amountEUR, "to CHN", "=", EURtoCHN(amountEUR))

                    elif choice == '4':
                        print(amountEUR, "to GBP", "=", EURtoGBP(amountEUR))
                    break

        #conversion selection for JPY to others

        elif choice == '3':
            print("Select Conversion")
            print("1. JPY convert to USD")
            print("2. JPY convert to EUR")
            print("3. JPY convert to CHN")
            print("4. JPY convert to GBP")

            while True:
                choice = input("Enter choice (1/2/3/4): ")

                #outputs for JPY converting to others

                if choice in ('1', '2', '3', '4'):
                    amountJPY = float(input("Enter amount of JPY: "))
                    if choice == '1':
                        print(amountJPY, "to USD", "=", JPYtoUSD(amountJPY))

                    elif choice == '2':
                        print(amountJPY, "to EUR", "=", JPYtoEUR(amountJPY))

                    elif choice == '3':
                        print(amountJPY, "to CHN", "=", JPYtoCHN(amountJPY))

                    elif choice == '4':
                        print(amountJPY, "to GBP", "=", JPYtoGBP(amountJPY))
                    break

        #conversion selection for CHN to others

        elif choice == '4':
            print("Select Conversion")
            print("1. CHN convert to USD")
            print("2. CHN convert to EUR")
            print("3. CHN convert to JPY")
            print("4. CHN convert to GBP")

            while True:
                choice = input("Enter choice (1/2/3/4): ")

                #outputs for CHN converting to others

                if choice in ('1', '2', '3', '4'):
                    amountCHN = float(input("Enter amount of CHN: "))
                    if choice == '1':
                        print(amountCHN, "to USD", "=", CHNtoUSD(amountCHN))

                    elif choice == '2':
                        print(amountCHN, "to EUR", "=", CHNtoEUR(amountCHN))

                    elif choice == '3':
                        print(amountCHN, "to JPY", "=", CHNtoJPY(amountCHN))

                    elif choice == '4':
                        print(amountCHN, "to GBP", "=", CHNtoGBP(amountCHN))
                    break

        #conversion selection for GBP to others

        elif choice == '5':
            print("Select Conversion")
            print("1. GBP convert to USD")
            print("2. GBP convert to EUR")
            print("3. GBP convert to JPY")
            print("4. GBP convert to CHN")

            while True:
                choice = input("Enter choice (1/2/3/4): ")

                #outputs for GBP converting to others

                if choice in ('1', '2', '3', '4'):
                    amountGBP = float(input("Enter amount of GBP: "))
                    if choice == '1':
                        print(amountGBP, "to USD", "=", GBPtoUSD(amountGBP))

                    elif choice == '2':
                        print(amountGBP, "to EUR", "=", GBPtoEUR(amountGBP))

                    elif choice == '3':
                        print(amountGBP, "to JPY", "=", GBPtoJPY(amountGBP))

                    elif choice == '2':
                        print(amountGBP, "to CHN", "=", GBPtoCHN(amountGBP))
                    break
