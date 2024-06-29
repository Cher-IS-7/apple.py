print ("Enter number of slices of pie")

Int1 = int(input(""))
try:
    print(Int1)
except ValueError:
    print('Enter a Int')

print("If you where to cut an apple pie in", Int1, "slices...")
print("You would have")
print(100 / Int1, "% per slice")
print("👍")

input("Press ENTER to exit")
