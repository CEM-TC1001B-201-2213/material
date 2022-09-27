
edad = int(input("Indica tu edad: "))

# if edad >= 3 and edad <= 5:
#     print("Kinder")
# 
# if edad >= 6 and edad <= 11:
#     print("Primaria")
#     
# if edad >= 12 and edad <= 14:
#     print("Secundaria")
# 
# if edad >= 15 and edad <= 17:
#     print("Preparatoria")
# 
# if edad >= 18:
#     print("Profesional")

# ---------------------------------------
    
# if edad >= 3 and edad <= 5:
#     print("Kinder")
# else:
#     if edad <= 11:
#         print("Primaria")
#     else:
#         if edad <= 14:
#             print("Secundaria")
#         else:
#             if edad <= 17:
#                 print("Preparatoria")
#             else:
#                 if edad >= 18:
#                     print("Profesional")

# -------------------------------------

if edad < 3:
    print("No está en edad para ir a la escuela.")
elif edad <= 5:
    print("Kinder")
elif edad <= 11:
    print("Primaria")
elif edad <= 14:
    print("Secundaria")
elif edad <= 17:
    print("Preparatoria")
else:
    print("Profesional")