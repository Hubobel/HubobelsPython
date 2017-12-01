chuck_file= open(pfad + '/api/chuck.txt','r',encoding='UTF-8')
for line in chuck_file:
    fact.append(line.strip('\n'))
chuck_file.close()
ran=random.randint(1,len(fact)-1)
fakt={}
a=0
for i in fact:
    fakt[a]=i
    a  =a +1
with open(pfad+'/api/chuck.json', 'w',encoding='ascii') as fp:
    json.dump(fakt, fp, sort_keys=True, indent=4)