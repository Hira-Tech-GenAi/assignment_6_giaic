#2. Using cls
#Assignment:
#Create a class Counter that keeps track of how many objects have been created. Use a class variable #and a class method with cls to manage and display the count.

class Counter():
    count = 0
    
    def __init__(self):
        Counter.count += 1
        
    #cls matlab "class" ka reference (jaise self object ka hota hai).    
    @classmethod
    def get_obj_count(cls):
        print(f"Count of Object: {cls.count}")

obj1 = Counter()
obj1 = Counter()
obj1 = Counter()

Counter.get_obj_count()