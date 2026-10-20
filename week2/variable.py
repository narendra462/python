# Global variable
x = 20

def my_function():
    # Local variable
    y = 10

    print("Global variable:", x)
    print("Local variable:", y)

my_function()

print("Global variable outside function:", x)