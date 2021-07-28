# This function just runs a recursion to as the user the type of volume to be calculated
# The function makes use of recursion to ask for another input for an invalid option
# Isaac D. 05/06/2021
def volumes():
    user_request = input("Please type 1 for sphere,2 for cylinder OR 3 for cone: ")
    user_request = int(user_request)
    
    if user_request == 1:
        def sphere(r):
            import math
            volume_sphere = (4/3)*math.pi*(r**3)
            return volume_sphere
        r = int(input("Enter radius of the sphere: "))
        print(sphere(r))
        
    elif user_request == 2:
        def cylinder(r,l):
            import math
            volume_cylinder = math.pi*(r**2)*l
            return volume_cylinder
        r = int(input("Enter radius of the cylinder: "))
        l = int(input("Enter height of the cylinder: "))
        print(cylinder(r,l))
    
    elif user_request == 3:
        def cone(r,l):
            import math
            volume_cone = math.pi*(r**2)*(l/3)
            return volume_cone
        r = int(input("Enter radius of the cylinder: "))
        l = int(input("Enter height of the cylinder: "))
        print(cone(r,l))

    else:
        volumes()
