age = 28

sex = 0

bmi = 26.2

num_of_children = 3

smoker = 0


insurance_cost = 250 * age - 128 * sex + 370 * bmi + 425 * num_of_children + 24000 * smoker -12500


print("This person's insurance cost is " + str(insurance_cost) + " dollars.")

age += 4

new_insurance_cost = 250 * age - 128 * sex + 370 * bmi + 425 * num_of_children + 24000 * smoker -12500


change_in_insurance_cost = new_insurance_cost - insurance_cost

print("The change in estimated insurance cost after increasing the age by 4 years is " + str(change_in_insurance_cost) + " dollars")

age = 28

bmi += 3.1

new_insurance_cost = 250 * age - 128 * sex + 370 * bmi + 425 * num_of_children + 24000 * smoker -12500

change_in_insurance_cost = new_insurance_cost - insurance_cost

print("The change in estimated insurance cost after increasing BMI by 3.1 is " + str(change_in_insurance_cost) + " dollars")


bmi -= 3.1

sex += 1

new_insurance_cost = 250 * age - 128 * sex + 370 * bmi + 425 * num_of_children + 24000 * smoker -12500

change_in_insurance_cost = new_insurance_cost - insurance_cost

print("The change in estimated insurance cost after being male is " + str(change_in_insurance_cost) + " dollars")


