# display trouser measurement
from typing import Dict, Any

# print("Men Trouser Measurement Details ")
#
# # Declare empty list
#
trouser_container: Dict[Any, Any] = {}

# # TODO
# # I want to take user first name and last name and store it with their correspondent measurement
# # input trouser lenght

while True:
    try:
        name = input("Customer name: ").strip().capitalize()
        trouser_length = input("Trouser Length:").strip()
        new_trouser = float(trouser_length)
        if new_trouser > 0:
            trouser_container.update({"trouser": {"trouser length": new_trouser}})

        else:
            print("Enter a valid measurement")

        # input trouser waist
        trouser_waist = input("Trouser Waist:").strip()
        new_waist = float(trouser_waist)
        if new_waist > 0:
            trouser_container.update({"waist": {"Trouser Waist is": new_waist}})
        else:
            print("Enter a valid trouser waist")

        # input trouser outseam
        trouser_outseam = input("Trouser Outseam:").strip()
        new_outseam = float(trouser_outseam)
        if new_outseam > 0:
            trouser_container.update({"outseams": {"Trouser OutSeams is": new_outseam}})
        else:
            print("Enter a valid out-seam measurement")

        # input trouser inseam
        trouser_inseam = input("Trouser Inseam:").strip()
        new_inseam = float(trouser_inseam)
        if new_inseam > 0:
            trouser_container.update({"inseams": {"Trouser InSeams is": new_inseam}})
        else:
            print("Enter a valid in-seam measurement")

        # input trouser crotch
        trouser_crotch = input("Trouser Crotch:").strip()
        new_crotch = float(trouser_crotch)
        if new_crotch > 0:
            trouser_container.update({"crotch": {"Trouser Crouch is": new_crotch}})
        else:
            print("Enter a valid crotch measurement")

        # input trouser thigh
        trouser_thigh = input("Trouser Thigh:").strip()
        new_thigh = float(trouser_thigh)
        if new_thigh > 0:
            trouser_container.update({"thigh": {"Trouser Thigh is": new_thigh}})
        else:
            print("Enter a valid Thigh measurement")

        # input trouser knee

        trouser_knee = input("Trouser Knee:").strip()
        new_knee = float(trouser_knee)
        if new_knee > 0:
            trouser_container.update({"knee": {"Trouser Knee is": trouser_knee}})
        else:
            print("Enter a valid knee measurement")
    except:
        print('Enter valid measurement')

    print(trouser_container)

    #def trouser(t_length):