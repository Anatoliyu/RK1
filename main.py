

from operator import itemgetter


class Operator:
    """"Оператор"""
    def __init__ (self, id ,surname,salary, id_CompLang):
        self.id = id
        self.surname = surname
        self.salary = salary
        self.id_CompLang = id_CompLang

class CompLang:
    """"Язык програмирования"""
    def __init__(self, id, name):
        self.id = id
        self.name = name

class CompLang_Operator:
    """"Операторы языка програмирования"""
    def __init__(self,id_Operator, id_CampLang):
        self.id_Operator = id_Operator
        self.id_CampLang = id_CampLang

Operators=[
    Operator(0,'Иванов',1000,1),
    Operator(1,'Петров',2000,2),
    Operator(2,'Александров',3000,4),
    Operator(3,'Сидоров',4000,1),
    Operator(4,'Абдулов',2500,3),
    Operator(5,'Нурмагомедов',1300,2),
    Operator(6,'Семенов',2000,3),
    Operator(7,'Оппенгеймер',4300,4),
    Operator(8,'Лоуренс',2300,1),
    Operator(9,'Неймер',1700,0),
]

CompLangs=[
    CompLang(0,'язык програмирования C++'),
    CompLang(1,'C'),
    CompLang(2,'язык програмирования Python'),
    CompLang(3,'Pascal'),
    CompLang(4,'Java'),
]

CompLang_Operators=[
    CompLang_Operator(0,0),
    CompLang_Operator(0,2),
    CompLang_Operator(0,4),
    CompLang_Operator(1,2),
    CompLang_Operator(2,4),
    CompLang_Operator(2,1),
    CompLang_Operator(2,0),
    CompLang_Operator(3,1),
    CompLang_Operator(3,2),
    CompLang_Operator(4,3),
    CompLang_Operator(5,2),
    CompLang_Operator(6,3),
    CompLang_Operator(7,4),
    CompLang_Operator(8,1),
    CompLang_Operator(9,0),
]
def main():
    """"Основная функция"""

    one_to_many = [(o.surname, o.salary, c.name)
                   for o in Operators
                   for c in CompLangs
                   if c.id == o.id_CompLang]

    many_to_many_temp = [(c.name, oc.id_CampLang, oc.id_Operator)
                        for c in CompLangs
                        for oc in CompLang_Operators
                        if c.id == oc.id_CampLang]

    many_to_many = [(o.surname, o.salary, CompLang_name)
                    for CompLang_name, CompLang_id, Operator_id in many_to_many_temp
                    for o in Operators
                    if o.id == Operator_id]

    print('Задание E1')
    res = list()
    for surname, salary, nameCompLang in one_to_many:
        if 'язык програмирования' in nameCompLang.lower():
            res.append((surname, salary, nameCompLang))
    print(res)
    print('Задание E2')
    res = []
    res1 = []
    for c in CompLangs:
        c_operators = list(filter(lambda i: i[2] == c.name, one_to_many))
        if len(c_operators)>0:
            c_complangs = [salary for _,salary,_ in c_operators]
            c_sals_midle = round(sum(c_complangs)/len(c_complangs),2)
            res1.append((c.name, c_sals_midle))
    res = sorted(res1, key=itemgetter(1), reverse=True)
    print(res)


    print('Задание E3')
    for surname, salary, name in many_to_many:
        if surname[0] == 'А': print('Язык:',name,'Фамилия:', surname,';')

if __name__ == "__main__":
    main()