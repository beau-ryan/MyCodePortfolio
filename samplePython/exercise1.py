# for all to contribute to the project, and to learn from it, and to have fun with it, and to create amazing things with it, and to share it with the world, and to make a difference in the world with it, and to make a positive impact on the world with it, and to make a better world with it, and to make a better future with it, and to make a better life with it, and to make a better you with it, and to make a better me with it, and to make a better us with it, and to make a better them with it, and to make a better everything with it.
import psutil
def mem_free():

    mem_free = psutil.virtual_memory()
    return mem_free.free

print(mem_free())