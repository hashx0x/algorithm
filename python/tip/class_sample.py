class Person:
    # 생성자
    def __init__(self, name:str): # self : 객체 자기자신 (this)
        print("here")
        self.name = name
        print(self.name)

    def talk(self):
        print(f"안녕하세요 저는 {self.name} 입니다.")
    
person_1 = Person("123")
person_2 = Person("456")