class Error_d(Exception):
    def __init__(self,value):
       self.value = value

    def __str__(self):
        return self.value + 'Ошибка!Только числа!'


    
class Expansion_dict(dict):

    empty_dict = {}

    def __init__(self,key = None, value = None):

        if key is None:
            Expansion_dict.empty_dict = {}        

    def __setitem__(self, key, value):
        if not isinstance(value,(int,float)):
            raise Error_d(value)
        return dict.__setitem__(self,key,value)   
    
    def __getitem__(self, value):
        if isinstance(value, int):
            return self.get(list(dict(sorted_tuple))[value])
        else:
            return self.get(value)
  


class Special:
    def __init__(self):
        self.dict = dict()
        self.ploc = Ploc(self.dict)
    
    def __getitem__(self, key):
        return self.dict[key]
    
    def __setitem__(self, key, value):
        self.dict[key] = value
    
    def items(self):
        return self.dict.items()
    
    def __repr__(self):
        return repr(self.dict)



class Ploc:
    def __init__(self,d):
        self.dict = d  
    
    def __getitem__(self, filter_value):
        new_map = Expansion_dict()
       
        
        for key, value in self.dict.items():
            try:
                if filter_value(int(key)):
                    new_map[key] = value
            except ValueError:
                pass  
        
        return new_map

    
       
d = Expansion_dict()
d["value1"] = 1
d["value2"] = 2
d["value3"] = 3
d["1"] = 10
d["2"] = 20
d["3"] = 30
d["1, 5"] = 100
d["5, 5"] = 200
d["10, 5"] = 300

sorted_tuple = sorted(d.items(), key=lambda x: x[0])

print(d[0])
print(d[2])
print(d[5])
print(d[8])

#--------------------#

m = Special()
m["1"] = 10
m["2"] = 20
m["3"] = 30
m["1, 5"] = 100
m["5, 5"] = 200
m["10, 5"] = 300


print(m.ploc[lambda key: key >= 2])



