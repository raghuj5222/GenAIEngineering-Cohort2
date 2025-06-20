import os
import pandas as pd

class JobDataAnalysis:
    
    def __init__(self,filename):
        self.pd = pd.read_csv(filename)  
        #print (self.pd.head())  # Display the first few rows of the DataFrame for verification
    
    def get_company_locations(self):
        #print( self.pd.head())
        #print ( " is it working? " )
        return self.pd["company_location"].sort_values().unique()
    
    def get_salary_range_per_emp_type(self,cntry):
        df = pd.DataFrame(self.pd)
        filtered_df =df['company_location'] == cntry
        return df[filtered_df].groupby('employment_type').agg({'salary_usd': ['mean', 'min', 'max']})
  
    def get_avg_exp_per_level(self, cntry):
        df = pd.DataFrame(self.pd)
        filtered_df =df['company_location'] == cntry
        return  df[filtered_df].groupby('experience_level').agg({'years_experience': ['mean']}).to_dict()
     
    def get_num_industry(self, cntry):
        df = pd.DataFrame(self.pd)
        filtered_df =df['company_location'] == cntry
        return  df[filtered_df].groupby('industry').count().to_dict()

    def get_benefit_score_range(self):
        return self.pd.groupby('company_location').agg({'benefits_score': ['mean', 'min', 'max']})
   
#●	At the initialisation of object, the CSV file name to be provided. The other functions shall work based on this data.
#●	get_company_locations : return the list of company location countries
#●	get_salary_range_per_emp_type : for a country as input, return a data frame 
# containing min, mean, max salary per employee type. Employee type shall be columns
#●	get_avg_exp_per_level : for a country as input, return average number of years experience 
# per experience level as a dict
#●	get_num_industry : return number of industries that are recruiting per country as a dict
#●	get_benefit_score_range : return min, mean, max benefit score per country as a data frame
####################
# Starting the main 

filename = input("Enter file name (including path):")
print("Filename is: " + filename)

## Print the list of company location countries
jda = JobDataAnalysis(filename)
print ( '\n'.join(jda.get_company_locations()))

## list for given country - employee types
cntry = input("Enter Country(full name) to calculate aggregates for:")
print("Country Name is: " + cntry)

print ( '-------------------------- Printing the average salary per level --------------------------' )
print ( jda.get_salary_range_per_emp_type(cntry))

print ( '-------------------------- Printing the average experience per level --------------------------' )
## list avg salary as dic
print ( jda.get_avg_exp_per_level(cntry))

print ( '-------------------------- Printing the industries count --------------------------' )
## list avg salary as dic
print ( jda.get_num_industry(cntry))

print ( '-------------------------- Printing benefits score by country --------------------------' )
## list avg salary as dic
print ( jda.get_benefit_score_range())


