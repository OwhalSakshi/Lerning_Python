# class car:
#     windows=4
#     doors=4
#     color='red'
#     def horn(self):
#         print('horn')
#         print(self.doors)

# obj=car()
# print(obj.color)
# obj.horn()

# using self keyword
class Car:
    def __init__(self, w, d, c):
        self.w = w  # Assign values to the attributes
        self.d = d
        self.c = c

# Create instances of the Car class
obj = Car(4, 4, 'red')
obj_1 = Car(5, 5, 'black')

# Print the 'd' attribute of obj_1
print(obj_1.d)
