# defining all the Richter Scale values

RS_10 = 1.0
RS_50 = 5.0
RS_78 = 7.8
RS_91 = 9.1
RS_92 = 9.2
RS_95 = 9.5

# computing Joules released for each value

Joules_RS_10 = 10**((1.5 * RS_10) + 4.8)
Joules_RS_50 = 10**((1.5 * RS_50) + 4.8)
Joules_RS_78 = 10**((1.5 * RS_78) + 4.8)
Joules_RS_91 = 10**((1.5 * RS_91) + 4.8)
Joules_RS_92 = 10**((1.5 * RS_92) + 4.8)
Joules_RS_95 = 10**((1.5 * RS_95) + 4.8)

# computing tons of TNT released for each value

TNT_RS_10 = Joules_RS_10 / (4.184 * (10**9))
TNT_RS_50 = Joules_RS_50 / (4.184 * (10**9))
TNT_RS_78 = Joules_RS_78 / (4.184 * (10**9))
TNT_RS_91 = Joules_RS_91 / (4.184 * (10**9))
TNT_RS_92 = Joules_RS_92 / (4.184 * (10**9))
TNT_RS_95 = Joules_RS_95 / (4.184 * (10**9))

# printing the table of values

print("Richter           Joules                     TNT")
print(RS_10, "       ", Joules_RS_10, "              ", TNT_RS_10)
print(RS_50, "       ", Joules_RS_50, "            ", TNT_RS_50)
print(RS_78, "       ", Joules_RS_78, "     ", TNT_RS_78)
print(RS_91, "       ", Joules_RS_91, "   ", TNT_RS_91)
print(RS_92, "       ", Joules_RS_92, "   ", TNT_RS_92)
print(RS_95, "       ", Joules_RS_95, " ", TNT_RS_95)

# ask the user for their own Richter Scale value and define it

User_RS = float(input("Please enter a Richter scale value: "))

# calculate Joules and TNT for the user value

Joules_User_RS = 10**((1.5 * User_RS) + 4.8)
TNT_User_RS = Joules_User_RS / (4.184 * (10**9))

# print the user values

print("Richter scale value: ", User_RS)
print("Equivalent in joules: ", Joules_User_RS)
print("Equivalent in tons of TNT: ", TNT_User_RS)