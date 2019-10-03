class Snake:
    name = "black mamba"

    def change_name(self, new_name):
        self.name = new_name

    #instantiate the class
snake = Snake()
 #prints the current object
print(snake.name)

snake.change_name("Python")
print(snake.name)


#----------------another way of doing it is by defining attributes in init method --------------------------------|

class Snake:

    def __init__(self, name):
        self.name = name

    def change_name(self, new_name):
        self.name = new_name

blackmamba = Snake("black mamba")
python = Snake("python")

print(blackmamba.name)

print(python.name)
        
