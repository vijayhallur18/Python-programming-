class parents1():
    def assign_string_one(self,str1):
        self.str1=str1
    def show_string_one(self):
        return self.str1
    
class parents2():
    def assign_string_two(self,str2):
        self.str2=str2
    def show_string_two(self):
        return self.str2
    
class child(parents1,parents2):
    def assign_string_three(self,str3):
        self.str3=str3
    def show_string_three(self):
        return self.str3
    
p1=child()
p1.assign_string_one("one")
p1.assign_string_two("two")
p1.assign_string_three("three")
p1.show_string_one()
p1.show_string_two()
p1.show_string_three()
