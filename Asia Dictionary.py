from typing import NewType


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