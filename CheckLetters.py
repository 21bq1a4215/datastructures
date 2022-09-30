class CheckLetters:                                                                                                                                                                              
    def tell(self,l):
      word="akeotpn"
      ans=[]
      flag=0
      for k in l:
          for m in k.lower():
                 if m in word:flag=flag+1
          if flag==len(k):
              ans.append(k)
              flag=0
          else:flag=0
      return ans
l=['arun','varun','kent','peak','pot','eat','net','peacock','zebra','nata','toe','poke','knife','peot','venus','ant']
obj=CheckLetters()
for i in obj.tell(l):print(i)

