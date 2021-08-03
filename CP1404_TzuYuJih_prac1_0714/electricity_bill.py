# print("Electricity bill estimator")
# cents_per_kWh = float(input("Enter cents per kWh: "))
# daily_use_inkWh = float(input("Enter daily use in kWh: "))
# billing_days = float(input("Enter number of billing days: "))
# estimated_bill = 0.01 * cents_per_kWh * daily_use_inkWh * billing_days
# print("Estimated bill: {0:.2f}".format(estimated_bill))

print("Electricity bill estimator 2.0")
TARIFF_11 = 0.244618
TARIFF_31 = 0.136928
tariff_type = str(input("Which tariff? 11 or 31: "))
daily_use_inkWh = float(input("Enter daily use in kWh: "))
billing_days = float(input("Enter number of billing days: "))
estimated_bill =  daily_use_inkWh * billing_days
if tariff_type == "11":
    estimated_bill *= TARIFF_11
elif tariff_type == "31":
    estimated_bill *= TARIFF_31
print("Estimated bill: {0:.2f}".format(estimated_bill))