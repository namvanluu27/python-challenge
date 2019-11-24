# Dependencies
import os
import pandas as pd
# Name of the CSV file
csv_file = "../Resources/budget_data.csv"
budget_df = pd.read_csv(csv_file)
budget_df.head()
# The total number of months included in the dataset
months_count = budget_df["Date"].count()
months_count
# The net total amount of "Profit/Losses" over the entire period
net_total = budget_df["Profit/Losses"].sum()
net_total
# The average of the changes in "Profit/Losses" over the entire period
budget_df["Profit/Loss Diff"] = budget_df["Profit/Losses"].diff()
profit_loss_average = budget_df["Profit/Loss Diff"].mean()
profit_loss_average
# The greatest increase in profits (date and amount) over the entire period
greatest_increase = budget_df["Profit/Loss Diff"].max()
greatest_increase_row = budget_df.loc[budget_df["Profit/Loss Diff"] == greatest_increase, "Date"]
greatest_increase_date = greatest_increase_row.iloc[0]
print(greatest_increase_date, greatest_increase_row)
# The greatest decrease in losses (date and amount) over the entire period
greatest_decrease = budget_df["Profit/Loss Diff"].min()
greatest_decrease_row = budget_df.loc[budget_df["Profit/Loss Diff"] == greatest_decrease, "Date"]
greatest_decrease_date = greatest_decrease_row.iloc[0]
print(greatest_decrease_date, greatest_decrease_row)
print("Financial Analysis")
print("-------------------")
print(f"Total Months: {months_count}")
print(f"Total Revenue: ${net_total}")
print(f"Average Change: ${profit_loss_average}")
print(f"Greatest Increase in Profits: {greatest_increase_date}({greatest_increase})")
print(f"Greatest Decrease in Profits: {greatest_decrease_date}({greatest_decrease})")
# Export Script to Local
output_path = os.path.join("budget_report.txt")