#import the csv module for reading csv files
import csv

# create the path to the data as a variable
csvpath = r'PyBank\Resources\budget_data.csv'

# # reading the csv file using the csv module
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
#    print(csvreader)
    csv_header = next(csvreader)
#    print(f"CSV Header: {csv_header}")
    # for row in csvreader:
    #    print(row)
   
    totalMonths = 0
    totalProfitLosses = 0
    previousProfitLosses = 0
    totalChangingProfitLosses = 0
    greatestIncrease = 0
    greatestDecrease = 0
    for row in csvreader:
        if previousProfitLosses == 0:
            currentProfitLosses = 0
        else:
            currentProfitLosses = int(row[1])
        totalMonths = totalMonths + 1
        totalProfitLosses = totalProfitLosses + int(row[1])
        totalChangingProfitLosses = totalChangingProfitLosses + (currentProfitLosses - previousProfitLosses)
        if (currentProfitLosses - previousProfitLosses) > greatestIncrease:
            greatestIncrease = (currentProfitLosses - previousProfitLosses)
            increaseMonth = row[0]
        if (currentProfitLosses - previousProfitLosses) < greatestDecrease:
            greatestDecrease = (currentProfitLosses - previousProfitLosses)
            decreaseMonth = row[0]
        previousProfitLosses = int(row[1])
    print('Financial Analysis')
    print('------------------------')
    print(f'Total Months: {totalMonths}')
    print(f'Total: ${totalProfitLosses}')
    averageChange = round((totalChangingProfitLosses / (totalMonths-1)),2)
    print(f'Average Change: ${averageChange}')
    print(f'Greatest Increase in Profits: {increaseMonth} (${greatestIncrease})')
    print(f'Greatest Decrease in Profits: {decreaseMonth} (${greatestDecrease})')
    output_path = r'PyBank\Analysis\Financial_Analysis.txt'
    with open(output_path, 'w') as textfile:
        textfile.write('Financial Analysis\n')
        textfile.write('------------------------\n')
        textfile.write(f'Total Months: {totalMonths}\n')
        textfile.write(f'Total: ${totalProfitLosses}\n')
        textfile.write(f'Average Change: ${averageChange}\n')
        textfile.write(f'Greatest Increase in Profits: {increaseMonth} (${greatestIncrease})\n')
        textfile.write(f'Greatest Decrease in Profits: {decreaseMonth} (${greatestDecrease})\n')