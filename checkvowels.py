class allvowels:
    def checkvowels(self,word):
        self.word=word
        vowels="aeiou"
        for k in word:
            if k in vowels:
                vowels=vowels.replace(k,"")
        if vowels =="": return "Yes !!The word consists of all vowels "
        else :return "Noo !!The word does not consists of all vowels "
print("Enter a word or sentence :")
obj= allvowels()
print(obj.checkvowels(input()))

