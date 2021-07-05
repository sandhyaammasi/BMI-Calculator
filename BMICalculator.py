#author : Sandhya Ammasi

from pywebio.input import *
from pywebio.output import *

def calculateBMI() :
    #getting the height as an input 
    height = input("Please ENTER your HEIGHT in cm",type = FLOAT)
    weight = input("Please ENTER your WEIGHT in kg",type = FLOAT)

    #calculate the bmi with height and weight
    #formula: [weight (kg) / height (cm) ^2] x 10,000
    bmi = (weight /(height*height)) * 10000

    bmiTuples = [(16,"Severly Underweight"),
    (18.4,"Underweight"),
    (24.9,"Healthy Weight"),
    (29.9,"Over Weight"),
    (34.9,"Obese"),
    (39,"Severly Obese"),
    (40,"Morbidly Obese"),
    ]

    for weightvalue,bmiComment in bmiTuples:
        if bmi <= weightvalue:
            put_text("Your BMI is %.1f and you are %s" %(bmi, bmiComment))
            break
        if bmi >= 40:
            put_text("Your BMI is %.1f and you are %s" %(bmi, bmiComment))
            break 
    
if __name__=='__main__':
    calculateBMI()







