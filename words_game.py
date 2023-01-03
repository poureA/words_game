class Filter(object):
    '''class docstring'''
    def __init__(self,text)->None:
        self.__t = text
    def write_message(self)->str:
        '''function docstring'''
        text_list = self.__t.split()
        temp = ''
        res = []
        bad = 0
        for i in text_list :
            for j in i :
                if j not in [chr(i) for i in range(ord('a'),ord('z')+1)] and j not in [chr(i) for i in range(ord('A'),ord('Z')+1)]:
                    bad+=1
            if len(i)/2 > bad :
                bad = 0
                for j in i :
                    if j in [chr(i) for i in range(ord('a'),ord('z')+1)] or j in [chr(i) for i in range(ord('A'),ord('Z')+1)]:
                        temp+=j
                res.append(temp)
                temp = ''
            bad = 0
        temp = ''
        finall = []
        for i in res :
            temp += i[0].upper()
            temp+=i[1:].lower()
            finall.append(temp)
            temp = ''
        res_dict = dict()
        for i in finall :
            res_dict[i] = finall.count(i)
        return res_dict
sample = Filter(input('enter a text :'))
print(sample.write_message())
exit = input('enter any key to exit :')
