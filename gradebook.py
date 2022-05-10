# last semester gradebook::
last_semester_gradebook = [["politics", "latin", "dance", "architecture"], [80, 96, 97, 65]]
print("\nLast semester gradebook: \n" + str(last_semester_gradebook) + "\n")

# beginning of new gradebook creation:
# choosing subjects::
subjects = ["physics", "calculus", "poetry", "history"]

# adding grades to them:
grades = [98, 97, 85, 88]

#combining both lists to make one whole gradebook:
gradebook = [subjects] + [grades]

# adding computer science and visual arts + their grades:
gradebook[0].append("computer science")
gradebook[1].append(100)
gradebook[0].append("visual arts")
gradebook[1].append(93)

# changing visual arts' grade:
gradebook[-1][-1] = 98

# removing visual arts grade:
gradebook[1].remove(gradebook[1][2])

# inserting a new grade to visual arts in the shape of "Pass":
gradebook[1].insert(2, "pass")
print("The actual semester gradebook: \n" + str(gradebook) + "\n")

# joining the two gradebooks together to make one whole:
full_gradebook = last_semester_gradebook + gradebook
print("Full gradebook: \n" + str(full_gradebook) + "\n")
