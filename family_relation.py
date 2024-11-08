from collections import defaultdict

class Solution:
    def __init__(self,head):
        self.family = defaultdict(list)
        self.head = head
        self.dead = set()
        self.fam_mem = [head]
        
    def birth(self,parent,child):
        self.family[parent].append(child)
        self.fam_mem.append(parent)
        self.fam_mem.append(child)
        
    def death(self,name):
        self.dead.add(name)
    
    def inheritance(self):
        self.ans = []
        self.dfs(self.head)
        return self.ans
    
    def dfs(self,head):
        if (head not in self.dead):
            self.ans.append(head)
        for i in self.family[head]:
            self.dfs(i)
    
    def relation(self,name1,name2):
        h = self.family[self.head]
        p1 = self.family[self.head][0]
        p2 = self.family[self.head][1]
        p = self.family.keys()
        c = self.family.values()
        if (name1 not in self.fam_mem) or (name2 not in self.fam_mem):
            return f"{name1} and {name2} are not related"
        if (name1 in h) and (name2 in h):
            return f"{name1} and {name2} are brothers"
        elif ((name1 in self.family[p1]) and (name2 in self.family[p1])) or ((name1 in self.family[p2]) and (name2 in self.family[p2])):
            return f"{name1} and {name2} are siblings"
        elif ((name1 in self.family[p1]) and (name2 in self.family[p2])) or ((name1 in self.family[p2]) and (name2 in self.family[p1])):
            return f"{name1} and {name2} are cousins"
        elif (name1 in self.family[name2]):
            return f"{name1} is child of {name2}"
        elif (name2 in self.family[name1]):
            return f"{name1} is parent of {name2}"
        elif len(self.family[name1]) < len(self.family[name2]):
            if (name1 not in p1) and (name2 in p2):
                return f"{name1} is {name2}'s brother's child"
            elif (name2 not in p1) and (name2 in p2):
                return f"{name1} is {name2}'s brother's child"
            else:
                return f"{name1} is grandchild of {name2}"
        elif len(self.family[name1]) > len(self.family[name2]):
            if (name2 in self.family[p2]) and (name2 in self.family[p1]):
                return f"{name1} is {name2}'s parent's brother"
            elif (name2 not in self.family[p1]) and (name2 in self.family[p2]):
                return f"{name1} is {name2}'s parent's brother"
            else:
                return f"{name1} is grandparent of {name2}"
        elif ((name1=='1') and (name2=='2')) or ((name1=='2') and (name2=='1')):
            return f"{name1} and {name2} are siblings"
        else:
            return f"{name1} and {name2} are long related"
            
ob = Solution('Ramaswamy')
ob.birth('Ramaswamy','Murali')
ob.birth('Ramaswamy','Siva')
ob.birth('Murali','Sabareesh')
ob.birth('Murali','Valli')
ob.birth('Siva','Himaja')
ob.birth('Siva','Sreenija')
ob.birth('Sabareesh','1')
ob.birth('Sabareesh','2')
#print(ob.family)
print(ob.inheritance())
ob.death('Ramaswamy')
print(ob.inheritance())
ob.death('Murali')
print(ob.inheritance())
#print(ob.relation('Ramaswamy','Murali'))
#print(ob.relation('Sabareesh','Murali'))
#print(ob.relation('Siva','Murali'))
#print(ob.relation('Ramaswamy','Valli'))
#print(ob.relation('Himaja','Sabareesh'))
#print(ob.relation('1','Murali'))
#print(ob.relation('Siva','2'))
#print(ob.relation('Sabareesh','Valli'))
#print(ob.relation('Siva','Umesh'))
name1,name2 = input("Enter 2 names: ").split()
print(f"Relation b/w {name1} and {name2} is: ")
print(ob.relation(name1,name2),end='\n')