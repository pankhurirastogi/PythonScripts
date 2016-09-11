from textblob import TextBlob
blob = TextBlob (u'Happy birthday Krity!!!.')
list1= ['de' , 'zh-CN' , 'fr', 'gu' , 'hi' ,'ja' , 'pa']
for n in list1 : 
  print(blob.translate(to= n))
