import unidecode
import chardet
all = []
with open('C:\\Users\\Oliver Morgan\\keywords.txt','r') as f:


     # decodes from utf-8 into unicode

    x = f.read().split('\n')

    for i in x:

        if i=='':
            pass
        else:
            all.append(i)

    print(len(all))
    print(all)

