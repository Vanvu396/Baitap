import random

questions = {
"strong": "Do ye like yer drinks strong?",
"salty": "Do ye like it with a salty tang?",
"bitter": "Are ye a lubber who likes it bitter?",
"sweet": "Would ye like a bit of sweetness with yer poison?",
"fruity": "Are ye one for a fruity finish?",
}
ingredients = {
"strong": ["glug of rum", "slug of whisky", "splash of gin"],
"salty": ["olive on a stick", "salt-dusted rim", "rasher of bacon"],
"bitter": ["shake of bitters", "splash of tonic", "twist of lemon peel"],
"sweet": ["sugar cube", "spoonful of honey", "spash of cola"],
"fruity": ["slice of orange", "dash of cassis", "cherry on top"],
}



def nhap(cau_hoi):
    listValue = list(questions.values())
    try:
        return listValue.index(cau_hoi)
    except:
        return


def xuat(cau_hoi):
    listKey = list(questions.keys())
    try:
        listAns = ingredients[listKey[cau_hoi]]
        print("Câu trả lời: ")
        print(listAns[random.randint(0,2)])
    except:
        print("Câu hỏi không hợp lệ, bạn vui lòng hỏi lại!!!")



a = input("Bạn muốn hỏi gì? ")

xuat(nhap(a))