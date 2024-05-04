# SAMPLE SIZE CALCULATOR SYSTEM PROGRAM BY GROUP 4
#Members
#Aproda, Rizalyn W. 
#Baquiran, Joshua E. 
#Dacillo, Nicole Caroline D. 
#Gadiano, Jezreel M. 
#Militante, Dariel M. 
#Victoriano, Nicole S. 

import pandas as pd
import math

sample_size = 0
population_size = None
margin_of_error = None
z_score = None
p_proportion = None
s_deviation = None

print ("\nSAMPLE SIZE CALCULATOR\n")
print ("\nHi, researchers! \n\n    Instructions: ")
print ("       \u2713 Determine the sample size based on the data availability.")
print ("       \u2713 Follow the recommended data and Excel file format to calculate the sample size without encountering any errors.")
print ("       \u2713 After obtaining the sample size, type 'Y' to try again, otherwise type any other key(s).")
print ("       \u2713 Another way to terminate the program is to type 'exit' on 'Enter the code:'.\n\n")

while True:
    print("\nCODE \t\t FORMULA TYPE \t\t\t\t\t\tREQUIRED DATA\n")
    print("SS1 \t Slovin's Formula \t\t\t\t Population Size, Margin of Error\n")
    print ("SS2 \t Known Population Formula \t\t Population Size, Margin of Error, Z-score, Population Proportion \n")
    print("SS3 \t Cochran's Formula \t\t\t\t Margin of Error, Z-score, Standard Deviation \n")
    print("SS4 \t Unknown Population Formula \t Margin of Error, Z-score, Population Proportion")
    
    code = input ("\nEnter the code: ")
    
    # SLOVIN'S CALCULATION (SS1)
    if code.lower () == "ss1":
        recommended_data = """\n\tRecommended Values for Starters:
        • Population Size - Non-negative value (e.g. 1500, 2000, 5000)
        • Margin of Error - Between 0.04 (4%) and 0.08 (8%)"""
        print(recommended_data)
       
        while True:
            try:
                choice = int (input ("Do you want to (1) input the data or (2) import data from Excel?: "))
                if choice < 1 or choice > 2:
                    print ("Invalid choice. Please try again.")
                    continue
                break
            
            except ValueError:
                print ("Invalid input. Please try again.")
       
        # SS1.Using the USER'S INPUT DATA to calculate the sample size.                  
        if choice == 1:
            while True:
                try:
                    population_size = float (input ("Enter the population size: "))
                    if population_size < 0:
                        print("Invalid input. Population size must be an integer greater than 0. Please try again.")
                        continue
                    elif (population_size).is_integer() and population_size > 0:
                        pass
                        break
                    else:
                        print("Invalid input. Please try again.")
                        continue
                    
                except ValueError:
                    print ("Invalid input. Please try again.")
                    
            while True:
                try:
                    margin_of_error = float (input ("Enter the margin of error: "))
                    if margin_of_error >= 1:
                        print("Margin of Error must be greater than 0 and less than 1. Please try again.")
                        continue
                    elif margin_of_error < 0:
                        print("Margin of Error must be greater than 0 and less than 1. Please try again.")
                        continue
                    elif margin_of_error == 0:
                        print("Margin of Error must be greater than 0 and less than 1. Please try again.")
                        continue
                    else:
                        pass
                        break
                    
                except ValueError:
                    print ("Invalid input. Please try again.")
               
            sample_size = math.ceil(population_size / (1 + population_size*(margin_of_error**2)))
            print (f"\nThe recommended sample size is {sample_size}.")
           
            Continue = input("\nDo you wish to continue using the sample size calculator? [Type 'Y' to continue, otherwise type any other key(s)]: ")
            if Continue.lower () == "y":
                continue
            else:
                print ("\nThank you for using our Sample Size Calculator!")
            break
           
        # SS1.Using the USER'S EXCEL FILE to calculate the sample size.
        elif choice == 2:
            recommended_format = """\n\tRecommended Excel Format:
        • Column 1 - Population Size
        • Column 2 - Margin of Error
        (The data must be on the second row or above.)"""
            print(recommended_format)
           
            while True:
                try:        
                    excel_file = input('Enter the path of the Excel file: ')
                    file = pd.read_excel(excel_file)
                    print()
                    column_names = ["Population","Margin of Error"]
                    file.columns = column_names
                    margin_of_error = (file['Margin of Error']*file['Margin of Error'])
                    denominator = (1 + file['Population']*(margin_of_error))              
               
                    sample_size = ((file['Population'])/denominator)
                    file['Sample Size'] = sample_size.apply(math.ceil)
                    print()
                    print(file.to_string(index=False))
                    break
               
                except FileNotFoundError:
                    print(f"Error: File '{excel_file}' not found. Please enter a valid path and try again.\n")
                    continue
                except ValueError:
                    print("Error: The Excel file format is not compatible. Please make sure the file has 2 columns for the Population Size and Margin of Error and try again.\n")
                    continue
                except Exception as e:
                    print(f"Error: {e}\nPlease enter a valid Excel file and try again.\n")
                    continue
        
            Continue = input("\nDo you wish to continue using the sample size calculator? [Type 'Y' to continue, otherwise type any other key(s)]: ")
            if Continue.lower () == "y":
                continue
            else:
                print ("\nThank you for using our Sample Size Calculator!")
            break
                                  
    # KNOWN POPULATION CALCULATION (SS2)                                  
    elif code.lower () == "ss2":
        recommended_data = """\n\tRecommended Values for Starters:
        • Population Size - Non-negative value (e.g. 1500, 2000, 5000)
        • Margin of Error - Between 0.04 (4%) and 0.08 (8%)
        • Z-score - 1.96 value at the 95% confidence level
        • Population Proportion - If not available, use 0.5 (50%)"""
        print(recommended_data)
       
        while True:
            try:
                choice = int (input ("Do you want to (1) input the data or (2) import data from Excel?: "))
                if choice < 1 or choice > 2:
                    print ("Invalid choice. Please try again.")
                    continue
                break  
            
            except ValueError:
                print ("Invalid input. Please try again.")
       
        # SS2.Using the USER'S INPUT DATA to calculate the sample size.
        if choice == 1:
            while True:
                try:
                    population_size = float (input ("Enter the population size: "))
                    if population_size < 0:
                        print("Invalid input. Population size must be an integer greater than 0. Please try again.")
                        continue
                    elif (population_size).is_integer() and population_size > 0:
                        pass
                        break
                    else:
                        print("Invalid input. Please try again.")
                        continue
                    
                except ValueError:
                    print ("Invalid input. Please try again.")
                    
            while True:
                try:
                    margin_of_error = float (input ("Enter the margin of error: "))
                    if margin_of_error >= 1:
                        print("Margin of Error must be greater than 0 and less than 1. Please try again.")
                        continue
                    elif margin_of_error < 0:
                        print("Margin of Error must be greater than 0 and less than 1. Please try again.")
                        continue
                    elif margin_of_error == 0:
                        print("Margin of Error must be greater than 0 and less than 1. Please try again.")
                        continue
                    else:
                        pass
                        break
                    
                except ValueError:
                    print ("Invalid input. Please try again.")
                    
            while True:
                try:
                    z_score = float (input ("Enter the z-score: "))
                    if z_score < 0:
                        print("Try z-scores from 0 to 3. Please try again.")
                        continue
                    elif z_score > 3:
                        print("Try z-scores from 0 to 3. Please try again.")
                        continue
                    elif z_score <= 3:
                        pass
                        break
                    
                except ValueError:
                    print ("Invalid input. Please try again.")
                    
            while True:
                try:
                    p_proportion = float (input ("Enter the population proportion: "))
                    if p_proportion <= 0:
                        print("Population proportion must be greater than 0 and less than or equal 1. Please try again.")
                        continue
                    elif p_proportion > 1:
                        print("Population proportion must be greater than 0 and less than or equal 1. Please try again.")
                        continue
                    else:
                        pass
                        break
                    
                except ValueError:
                    print ("Invalid input. Please try again.")
           
            numerator = ((z_score**2)*p_proportion*(1-p_proportion))/(margin_of_error**2)
            denominator = 1 + ((z_score**2)*p_proportion*(1-p_proportion))/((margin_of_error**2)*population_size)
            sample_size = math.ceil(numerator/denominator)
            print()
            print (f"The recommended sample size is {sample_size}.")
           
            Continue = input("\nDo you wish to continue using the sample size calculator? [Type 'Y' to continue, otherwise type any other key(s)]: ")
            if Continue.lower () == "y":
                continue
            else:
                print ("\nThank you for using our Sample Size Calculator!")
            break
           
        # SS2.Using the USER'S EXCEL FILE to calculate the sample size.    
        elif choice == 2:
            recommended_format = """\n\tRecommended Excel Format:
        • Column 1 - Population Size
        • Column 2 - Margin of Error
        • Column 3 - Z-score
        • Column 4 - Population Proportion
        (The data must be on the second row or above.)"""
            print(recommended_format)
           
            while True:
                try:  
                    excel_file = input('Enter the path of the Excel file: ')
                    file = pd.read_excel(excel_file)
                    column_names = ["Population", "Margin of Error","Z-score","Population Proportion"]
                    file.columns = column_names
                    z_score = (file['Z-score']**2)
                    p_proportion = file["Population Proportion"]*(1-file["Population Proportion"])
                    margin_of_error = file['Margin of Error']**2
                    numerator = (z_score*p_proportion)/margin_of_error
                    Ne = file["Population"]*margin_of_error
                    denominator = 1+(z_score*p_proportion/Ne)
               
                    sample_size = (numerator/denominator)
                    file['Sample Size'] = sample_size.apply(math.ceil)
                    print()
                    print(file.to_string(index=False))
                    break
               
                except FileNotFoundError:
                    print(f"Error: File '{excel_file}' not found. Please enter a valid path and try again.\n")
                    continue
                except ValueError:
                    print("Error: The Excel file format is not compatible. Please make sure the file has 4 columns for the required data and try again.\n")
                    continue
                except Exception as e:
                    print(f"Error: {e}\nPlease enter a valid Excel file and try again.\n")
                    continue
               
            Continue = input("\nDo you wish to continue using the sample size calculator? [Type 'Y' to continue, otherwise type any other key(s)]: ")
            if Continue.lower () == "y":
                continue
            else:
                print ("\nThank you for using our Sample Size Calculator!")
            break
               
    # COCHRAN'S CALCULATION (SS3)    
    elif code.lower () == "ss3":
        recommended_data = """\n\tRecommended Values for Starters:
        • Margin of Error - Between 0.04 (4%) and 0.08 (8%)
        • Z-score - 1.96 value at the 95% confidence level
        • Standard Deviation - If not available, use 0.5 """
        print(recommended_data)
       
        while True:
            try:
                choice = int (input ("Do you want to (1) input the data or (2) import data from Excel?: "))
                if choice < 1 or choice > 2:
                    print ("Invalid choice. Please try again.")
                    continue
                break
           
            except ValueError:
                print ("Invalid input. Please try again.")
       
        # SS3.Using the USER'S INPUT DATA to calculate the sample size.
        if choice == 1:
            while True:
                try:
                    margin_of_error = float (input ("Enter the margin of error: "))
                    if margin_of_error >= 1:
                        print("Margin of Error must be greater than 0 and less than 1. Please try again.")
                        continue
                    elif margin_of_error < 0:
                        print("Margin of Error must be greater than 0 and less than 1. Please try again.")
                        continue
                    elif margin_of_error == 0:
                        print("Margin of Error must be greater than 0 and less than 1. Please try again.")
                        continue
                    else:
                        pass
                        break
                    
                except ValueError:
                    print ("Invalid input. Please try again.")
                    
            while True:
                try:
                    z_score = float (input ("Enter the z-score: "))
                    if z_score < 0:
                        print("Try z-scores from 0 to 3. Please try again.")
                        continue
                    elif z_score > 3:
                        print("Try z-scores from 0 to 3. Please try again.")
                        continue
                    elif z_score <= 3:
                        pass
                        break
                    
                except ValueError:
                    print ("Invalid input. Please try again.")
                    
            while True:
                try:
                    s_deviation = float (input ("Enter the standard deviation: "))
                    if s_deviation <= 0:
                        print("Standard deviation must be greater than 0 and less than or equal 1. Please try again.")
                        continue
                    elif s_deviation > 1:
                        print("Standard deviation must be greater than 0 and less than or equal 1. Please try again.")
                        continue
                    else:
                        pass
                        break
                    
                except ValueError:
                    print ("Invalid input. Please try again.")
           
            sample_size = math.ceil(((z_score**2)*(s_deviation**2))/margin_of_error**2)
            print()
            print (f"The recommended sample size is {sample_size}.")
           
            Continue = input("\nDo you wish to continue using the sample size calculator? [Type 'Y' to continue, otherwise type any other key(s)]: ")
            if Continue.lower () == "y":
                continue
            else:
                print ("\nThank you for using our Sample Size Calculator!")
            break
   
        # SS3.Using the USER'S EXCEL FILE to calculate the sample size.
        elif choice == 2:
            recommended_format = """\n\tRecommended Excel Format:
        • Column 1 - Margin of Error
        • Column 2 - Z-score
        • Column 3 - Standard Deviation
        (The data must be on the second row or above.)"""
            print(recommended_format)
           
            while True:
                try:  
                    excel_file = input('Enter the path of the Excel file: ')
                    file = pd.read_excel(excel_file)
                    column_names = ["Margin of Error","Z-score","Standard Deviation"]
                    file.columns = column_names
                    z_score = (file['Z-score']**2)
                    s_deviation = file["Standard Deviation"]**2
                    numerator = z_score*s_deviation
                    denominator = file['Margin of Error']**2
               
                    sample_size = (numerator/denominator)
                    file['Sample Size'] = sample_size.apply(math.ceil)
                    print()
                    print(file.to_string(index=False))
                    break
               
                except FileNotFoundError:
                    print(f"Error: File '{excel_file}' not found. Please enter a valid path and try again.\n")
                    continue
                except ValueError:
                    print("Error: The Excel file format is not compatible. Please make sure the file has 3 columns for the required data and try again.\n")
                    continue
                except Exception as e:
                    print(f"Error: {e}\nPlease enter a valid Excel file and try again.\n")
                    continue
               
            Continue = input("\nDo you wish to continue using the sample size calculator? [Type 'Y' to continue, otherwise type any other key(s)]: ")
            if Continue.lower () == "y":
                continue
            else:
                print ("\nThank you for using our Sample Size Calculator!")
            break
               
    # UNKNOWN POPULATION CALCULATION (SS4)  
    elif code.lower () == "ss4":
        recommended_data = """\n\tRecommended Values for Starters:
        • Margin of Error - Between 0.04 (4%) and 0.08 (8%)
        • Z-score - 1.96 value at the 95% confidence level
        • Population Proportion - If not available, use 0.5 (50%)"""
        print(recommended_data)
       
        while True:
            try:
                choice = int (input ("Do you want to (1) input the data or (2) import data from Excel?: "))
                if choice < 1 or choice > 2:
                    print ("Invalid choice. Please try again.")
                    continue
                break
           
            except ValueError:
                print ("Invalid input. Please try again.")
       
        # SS4.Using the USER'S INPUT DATA to calculate the sample size.
        if choice == 1:
            while True:
                try:
                    margin_of_error = float (input ("Enter the margin of error: "))
                    if margin_of_error >= 1:
                        print("Margin of Error must be greater than 0 and less than 1. Please try again.")
                        continue
                    elif margin_of_error < 0:
                        print("Margin of Error must be greater than 0 and less than 1. Please try again.")
                        continue
                    elif margin_of_error == 0:
                        print("Margin of Error must be greater than 0 and less than 1. Please try again.")
                        continue
                    else:
                        pass
                        break
                    
                except ValueError:
                    print ("Invalid input. Please try again.")
                    
            while True:
                try:
                    z_score = float (input ("Enter the z-score: "))
                    if z_score < 0:
                        print("Try z-scores from 0 to 3. Please try again.")
                        continue
                    elif z_score > 3:
                        print("Try z-scores from 0 to 3. Please try again.")
                        continue
                    elif z_score <= 3:
                        pass
                        break
                    
                except ValueError:
                    print ("Invalid input. Please try again.")
                    
            while True:
                try:
                    p_proportion = float (input ("Enter the population proportion: "))
                    if p_proportion <= 0:
                        print("Population proportion must be greater than 0 and less than or equal 1. Please try again.")
                        continue
                    elif p_proportion > 1:
                        print("Population proportion must be greater than 0 and less than or equal 1. Please try again.")
                        continue
                    else:
                        pass
                        break
                    
                except ValueError:
                    print ("Invalid input. Please try again.")
           
            sample_size = math.ceil(((z_score**2)*p_proportion*(1-p_proportion))/(margin_of_error**2))
            print()
            print (f"The recommended sample size is {sample_size}.")
           
            Continue = input("Do you wish to continue using the sample size calculator? [Type 'Y' to continue, otherwise type any other key(s)]: ")
            if Continue.lower () == "y":
                continue
            else:
                print ("\nThank you for using our Sample Size Calculator!")
            break
       
        # SS4.Using the USER'S EXCEL FILE to calculate the sample size.
        elif choice == 2:
            recommended_format = """\n\tRecommended Excel Format:
        • Column 1 - Margin of Error
        • Column 2 - Z-score
        • Column 3 - Population Proportion
        (The data must be on the second row or above.)"""
            print(recommended_format)
           
            while True:
                try:    
                    excel_file = input('Enter the path of the Excel file: ')
                    file = pd.read_excel(excel_file)
                    column_names = ["Margin of Error","Z-score","Population Proportion"]
                    file.columns = column_names
                    z_score = (file['Z-score']**2)
                    p_proportion = file["Population Proportion"]*(1-file["Population Proportion"])
                    numerator = z_score*p_proportion
                    denominator = file["Margin of Error"]**2
               
                    sample_size = (numerator/denominator)
                    file['Sample Size'] = sample_size.apply(math.ceil)
                    print()
                    print(file.to_string(index=False))
                    break
               
                except FileNotFoundError:
                    print(f"Error: File '{excel_file}' not found. Please enter a valid path and try again.\n")
                    continue
                except ValueError:
                    print("Error: The Excel file format is not compatible. Please make sure the file has 3 columns for the required data and try again.\n")
                    continue
                except Exception as e:
                    print(f"Error: {e}\nPlease enter a valid Excel file and try again.\n")
                    continue
               
            Continue = input("\nDo you wish to continue using the sample size calculator? [Type 'Y' to continue, otherwise type any other key(s)]: ")
            if Continue.lower () == "y":
                continue
            else:
                print ("\nThank you for using our Sample Size Calculator!")
            break                            
   
    elif code.lower () == "exit" :
        print ("\nThank you for using our Sample Size Calculator!")
        break
 
    else:
        print ("Invalid input. Please try again.")





