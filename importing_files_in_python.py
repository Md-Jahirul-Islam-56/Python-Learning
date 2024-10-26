# import KBC_challenge
# importing a file will automatically run the imported file. To stop that we can use if __name__ == "__main__":

#print(dir(KBC_challenge)) #dir shows what is there in the imported file

#-------------------------------------------------------------------------------------------------------------------

# import math as m #by using as we can shorted the name of the imported file
# print(m.sqrt(9))

# from math import sqrt as s #to bring a specific variable or function we can use (from imported_file_name import required_function)
# print(s(9))


#-------------------------------------------------------------------------------------------------------------------

# from math import * #if we want to import everything from the file but not recommended

# result = sqrt(9)
# print(result)  # Output: 3.0

# print(pi)  # Output: 3.141592653589793

#-------------------------------------------------------------------------------------------------------------------

import Zen_Of_Python_Poem as z #Go to Zen_Of_Python_Poem for more information
z.main()

