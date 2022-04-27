#List of All Asian Countries & Capitals
NE_Asia = {
    "Japan": "Tokyo", 
    "South Korea":"Seoul",
    "North Korea":"Pyongyang",
    "Taiwan" : "Taipei",
    "China":"Beijing",
    "Mongolia":"Ulaan Bataar"
    }

SE_Asia = {
    "Indonesia":"Jakarta",
    "East Timor":"Dili",
    "Philippines":"Manila",
    "Malaysia":"Kuala Lumpur",
    "Brunei":"Bandar Seri Begawan",
    "Singapore":"Singapore",
    "Vietnam" : "Hanoi",
    "Laos":"Vientiane",
    "Cambodia":"Phom Phen",
    "Thailand":"Bangkok",
    "Myannmar":"Rangoon",
    }

S_Asia = {
    "India":"New Delhi",
    "Nepal":"Kathmandu",
    "Bhutan":"Thimphu",
    "Pakistan":"Islamabad",
    "Sri Lanka":"Colombo",
    "Bangladesh":"Dhaka",
    "Maldives":"Male"
}

C_Asia = {
    "Kazahkstan":"Astana",
    "Kyrgyzstan":"Bishkek",
    "Tajikistan":"Dushanbe",
    "Turkmenistan":"Ashgabat",
    "Uzbekistan":"Tashkent",
    "Georgia":"T'bilisi",
    "Armenia":"Yerevan",
    "Azerbaijan":"Baku",
}

W_Asia = {
    "Afghanistan":"Kabul",
    "Iran":"Tehran",
    "Oman":"Muscat",
    "Yemen":"Sana'a",
    "Saudi Arabia":"Rihyad",
    "United Arab Emirates":"Abu Dhabi",
    "Quatar":"Doha",
    "Bahrain":"Manama",
    "Kuwait":"Kuwait City",
    "Iraq":"Bahgdad",
    "Syria":"Damascus",
    "Jordan":"Amman",
    "Israel":"West Jerusalem",
    "Palestine":"East Jerusalem",
    "Lebanon":"Beiruit",
    "Turkey":"Ankara",
    "Cyprus":"Nicosia"
}

from collections import OrderedDict
import os 
clear = lambda: os.system('cls')

country_count_in_NE_Asia = (len(NE_Asia))
country_count_in_SE_Asia = (len(SE_Asia))
country_count_in_S_Asia = (len(S_Asia))
country_count_in_C_Asia = (len(C_Asia))
country_count_in_W_Asia = (len(W_Asia))
country_count_in_Asia = country_count_in_C_Asia + country_count_in_NE_Asia + country_count_in_S_Asia + country_count_in_SE_Asia + country_count_in_W_Asia

NE_Asia_ordered = OrderedDict(sorted(NE_Asia.items()))
SE_Asia_ordered = OrderedDict(sorted(SE_Asia.items()))
S_Asia_ordered = OrderedDict(sorted(S_Asia.items()))
C_Asia_ordered = OrderedDict(sorted(C_Asia.items()))
W_Asia_ordered = OrderedDict(sorted(W_Asia.items()))

def country_count():
    count = len(chosen_region)
    print(count)

def exit_program():
    program =+1

for key, value in NE_Asia_ordered.items():
    print(key, ' : ', value)


program = 0
while program == 0:
    print("Welcome to Asia")
    region = input(str("Which region of Asia would you like to check, NE, SE, S, C or W?"))
    if region == "NE":
        chosen_region = NE_Asia
        print(f"You have chosen to see the {country_count_in_NE_Asia} countries in North East Asia: {chosen_region}")
        NE_choice = input("Would you like to see all the countries of North East Asia in Alphabetical Order? Y/N: ")
        if NE_choice == "Y":
            print(f"These are all the countries in North-East Asia in Alphabetical order: {NE_Asia_ordered}")
    elif region == "SE":
        chosen_region = SE_Asia
        print(f"You have chosen to see the {country_count_in_SE_Asia}  countries in South East Asia: {chosen_region}")
        SE_choice = input("Would you like to see all the countries of South East Asia in Alphabetical Order? Y/N: ")
        if SE_choice == "Y":
            print(f"These are all the countries in South-East Asia in Alphabetical order: {SE_Asia_ordered}")
    elif region == "S":
        chosen_region = S_Asia
        print(f"You have chosen to see the {country_count_in_S_Asia} countries in South Asia: {chosen_region}")
        S_choice = input("Would you like to see all the countries of South Asia in Alphabetical Order? Y/N: ")
        if S_choice == "Y":
            print(f"These are all the countries in South Asia in Alphabetical order: {S_Asia_ordered}")
    elif region == "C":
        chosen_region = C_Asia
        print(f"You have chosen to see the {country_count_in_C_Asia}  countries in Central Asia: {chosen_region}")
        C_choice = input("Would you like to see all the countries of Central Asia in Alphabetical Order? Y/N: ")
        if C_choice == "Y":
            print(f"These are all the countries in Central Asia in Alphabetical order: {C_Asia_ordered}")
    elif region == "W":
        chosen_region = W_Asia
        print(f"You have chosen to see the {country_count_in_W_Asia}  countries in West Asia: {chosen_region}")
        W_choice = input("Would you like to see all the countries of West Asia in Alphabetical Order? Y/N: ")
        if W_choice == "Y":
            print(f"These are all the countries in West Asia in Alphabetical order: {NE_Asia_ordered}")
    else:
        print("Error")

    print(f"There are a total of {country_count_in_Asia} countries in Asia")

    def merge():
        Asia = W_Asia | C_Asia | S_Asia | SE_Asia | NE_Asia
        return Asia

    Asia = merge()
    Asia_ordered = OrderedDict(sorted(Asia.items()))
    all_choice = input("Would you like to see all the countries of Asia in Order? Y/N: ")
    if all_choice == "Y":
        print(f"These are all the countries in Asia in Alphabetical order: {Asia_ordered}")
        print("Thank you for using the program tiny one hehehehe, you're the best")

    ending = input("Would you like to exit the program since there's nothing to do anymore? Y/N")
    if ending == "Y":
        print("Thanks baby, I love you so much")
        exit()
    else:
        clear()