"""
Create a function with classes and objects to implement polymorphism with inheritance, using the following content

Country, Language spoken and capital for India and USA as 2 functions with inheritance

""" 
class Country:
    def __init__(self, capital):
        self.capital = capital

    def display_capital(self):
        print("Capital:", self.capital)

class Language:
    def __init__(self, language):
        self.language = language

    def display_language(self):
        print("Language:", self.language)

class India(Country, Language):
    def __init__(self, capital, language):
        Country.__init__(self, capital)
        Language.__init__(self, language)

class USA(Country, Language):
    def __init__(self, capital, language):
        Country.__init__(self, capital)
        Language.__init__(self, language)

india = India("New Delhi", "Hindi")
usa = USA("Washington, D.C.", "English")

india.display_capital()
india.display_language()

usa.display_capital()
usa.display_language()
