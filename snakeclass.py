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
