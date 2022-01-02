import poplib

mymail = []

host = "pop3.web.de"
mail = poplib.POP3_SSL(host)
print (mail.getwelcome())
print (mail.user("schneeschieben@web.de"))
print (mail.pass_("Winter19&"))
print (mail.stat())
print (mail.list())
print ("")

if mail.stat()[1] > 0:
    print ("You have new mail.")
else:
    print ("No new mail.")

print ("")

numMessages = len(mail.list()[1])
numb=0
for i in range(numMessages):
    for j in mail.retr(i+1)[1]:
        numb+=1
        #print(j)
        if numb == 4 or numb == 5:
            print(j)

mail.quit()
input("Press any key to continue.")