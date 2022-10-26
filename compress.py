


class Compress:
    
    def compress(self,text):
        compressed = []
        values = {}
        n = 1
        text_list = text.split(" ")
        for z in text_list:
            if not z in values:
                values[z] = n
                n = n + 1

        for x in text_list:
            if x in values:
                y = values[x]
                compressed.append(y)
        return compressed,values

    def uncompress(self,compre,value):
        text = ""
        lista = value.keys()
        lista = list(lista)
        for x in compre:
            x-=1
            z = lista[x]
            text = text + ' ' +z
        return text[1:]