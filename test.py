"""
CREATE objects of classes India and USA and print their capital and language
""" 
class India():
    def capital(self):
        print("New Delhi")
    def language(self):
        print("Hindi and English")
class USA():
    def capital(self):
        print("Washington, D.C.")
    def language(self):
        print("English")
ind=India()
usa=USA()
for country in (ind,usa):
    country.capital()
    country.language()