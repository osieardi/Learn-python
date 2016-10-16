name = 'ossie'
age = 31
height = 170 #dalam cm
weight = 100 #getting obsess
eyes = 'black'
teeth = 'white'
hair = 'black'

#%s string
#%r repr artinya dia akan recall semua karakter termasuk ''
print("Let's talk about %s." % name)
#%d artinya dia akan manggil dalam number not string
print("He's %d centimeters tall" % height)
print("he's %d kilograms heavy" % weight)
print("Yes he is heavy")
print("He's got %s eyes and %s hair." % (eyes, hair))
print("His teeth are usually %s depending on the coffee." % teeth)

#trickly line
print("If I add %d, %d, and %d I get %d." % (age, height, weight, age + height + weight))
