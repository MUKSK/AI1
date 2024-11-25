class FamilyTree:
    def _init_(self):
        self.tree = {}
    def add_parent(self, parent, child):
        self.tree.setdefault(parent, {'children': [], 'parents': []})['children'].append(child)
        self.tree.setdefault(child, {'children': [], 'parents': []})['parents'].append(parent)
    def add_spouse(self, person1, person2):
        self.tree.setdefault(person1, {'children': [], 'parents': [], 'spouse': None})['spouse'] = person2
        self.tree.setdefault(person2, {'children': [], 'parents': [], 'spouse': None})['spouse'] = person1
    def get_parents(self, person):
        return self.tree.get(person, {}).get('parents', None)
    def get_children(self, person):
        return self.tree.get(person, {}).get('children', None)
    def get_spouse(self, person):
        return self.tree.get(person, {}).get('spouse', None)
    def get_siblings(self, person):
        parents = self.get_parents(person)
        if parents:
            siblings = [sibling for parent in parents for sibling in self.get_children(parent) if sibling != person]
            return siblings
        return None
    
obj = FamilyTree()
obj.add_parent('John', 'Alice')
obj.add_parent('John', 'Bob')
obj.add_parent('Mary', 'Alice')
obj.add_parent('Mary', 'Bob')
obj.add_spouse('John', 'Mary')
obj.add_parent('Alice', 'Charlie')
obj.add_parent('Bob', 'David')

print("Alice's parents:", obj.get_parents('Alice'))
print("John's children:", obj.get_children('John'))
print("John's spouse:", obj.get_spouse('John'))
print("Alice's siblings:", obj.get_siblings('Alice'))
