import pandas as pd
import matplotlib.pyplot as py

df = pd.read_csv("petrolbrands.csv")
print(df)
no_of_brands = int(input("Enter number of brands you want to analyze (Choose number from 1 to 5): "))
if no_of_brands < 1 or no_of_brands > 5:
    print("Invalid option. Please enter a number from 1 to 5.")
else:
    print('\nEnter 1 for revenue analysis\nEnter 2 for profit/loss analysis\nEnter 3 for equity analysis\n')
    analyse_no_brandmulti = int(input("\nEnter your choice: "))
    if analyse_no_brandmulti < 1 or analyse_no_brandmulti > 3:
        print("Invalid option. Please enter a number from 1 to 3.")
    else:
        no_of_yrs_brandmulti = int(input("Enter number of years you would like to analyse (Choose number from 1 to 20): "))
        if no_of_yrs_brandmulti > 20 or no_of_yrs_brandmulti < 1:
            print("Invalid option. Please enter a number from 1 to 20.")
        elif no_of_yrs_brandmulti == 1:
            year_brandmulti = int(input("Enter year that you want to analyse data for (Choose a year from 2004 and 2023): "))
            if year_brandmulti < 2004 or year_brandmulti > 2023:
                print("Invalid option. Please enter a year from 2004 to 2023.")
            else:
                print("Which brands would you like to analyse?\n Select 1 for Indian Oil\n Select 2 for Bharat Petroleum\n Select 3 for Hindustan Petroleum\n Select 4 for ONGC\n Select 5 for GAIL\n")
                for i in range(1, no_of_brands + 1):
                    name_of_brandmulti = int(input("Enter your choice: "))
                    name_index = name_of_brandmulti - 1
                    year_index = 2023 - year_brandmulti
                    ind = name_index + (year_index * 5)

                    if analyse_no_brandmulti == 1:
                        x = df.columns[2:6]
                        p = df.iloc[ind, 2:6].str.replace(',', '', regex=True).astype(float)
                        y = p.sort_values()
                        labels = ['Indian Oil', 'Bharat Petroleum', 'Hindustan Petroleum', 'ONGC', 'GAIL']
                        py.plot(x, y, label=labels[name_index])
                        py.xlabel('Revenue')
                        py.ylabel('Revenue in US Dollars')
                        py.grid(True)
                        py.legend(loc=1)
                        py.title('Revenue Analysis')
                        py.xticks(x, rotation=90)
                    elif analyse_no_brandmulti == 2:
                        x = df.columns[7:9]
                        p = df.iloc[ind, 7:9].str.replace(',', '', regex=True).astype(float)
                        y = p.sort_values()
                        labels = ['Indian Oil', 'Bharat Petroleum', 'Hindustan Petroleum', 'ONGC', 'GAIL']
                        py.plot(x, y, label=labels[name_index])
                        py.xlabel('Profit/Loss')
                        py.ylabel('Profit/Loss in US Dollars')
                        py.grid(True)
                        py.legend(loc=1)
                        py.title('Profit/Loss Analysis')
                        py.xticks(x, rotation=90)
                    else:
                        x = df.columns[9:12]
                        p = df.iloc[ind, 9:12].str.replace(',', '', regex=True).astype(float)
                        y = p.sort_values()
                        labels = ['Indian Oil', 'Bharat Petroleum', 'Hindustan Petroleum', 'ONGC', 'GAIL']
                        py.plot(x, y, label=labels[name_index])
                        py.xlabel('Equity Dividend')
                        py.ylabel('Equity')
                        py.grid(True)
                        py.legend(loc=1)
                        py.title('Equity Analysis')
                        py.xticks(x, rotation=90)
                py.show()
                print("Your graph has been plotted")



        else:
            multi_year = []
            brand_indices = []
            ind = []
            print("Which brand would you like to analyze?")
            print("Select 1 for Indian Oil\nSelect 2 for Bharat Petroleum\nSelect 3 for Hindustan Petroleum\nSelect 4 for ONGC\nSelect 5 for GAIL")

            for brand_index in range(1, no_of_brands + 1):
                name_of_brandmulti = int(input("Enter choice: "))
                if name_of_brandmulti < 1 or name_of_brandmulti > 5:
                    print("Invalid choice. Please enter a valid choice between 1 and 5.")
                else:
                    brand_indices.append(name_of_brandmulti - 1)

            for i in range(1, no_of_yrs_brandmulti + 1):
                year = int(input("Enter year that you want to analyze data for (Choose a year from 2004 and 2023): "))
                if year < 2004 or year > 2023:
                    print("Invalid option. Please enter a year between 2004 and 2023.")
                else:
                    multi_year.append(year)

            for brand_index in brand_indices:
                for year in multi_year:
                    year_index = 2023 - year
                    ind.append(brand_index + (year_index * 5))


            if analyse_no_brandmulti == 1:
                print("What would you like to analyse?\nSelect 1 for Net Revenue\nSelect 2 for Gross Revenue\nSelect 3 for Total Revenue\nSelect 4 for Operating Revenue")
                analyse_no1_revenue = int(input("Enter choice:"))
                if analyse_no1_revenue < 1 or analyse_no1_revenue > 4:
                    print("Invalid option. Please enter number between 1 to 4.")
                elif analyse_no1_revenue == 1:
                    if no_of_yrs_brandmulti == 1:
                        x = [int(year) for year in multi_year]
                        p = df.iloc[ind, 7].str.replace(',', '', regex=True).astype(float)
                        y = p.sort_values()
                        labels = ['Indian Oil', 'Bharat Petroleum', 'Hindustan Petroleum', 'ONGC', 'GAIL']
                        for brand_index in brand_indices:
                            py.plot(x, y, label=labels[brand_index])
                        py.xlabel('Years')
                        py.ylabel('Net Revenue in US Dollars')
                        py.title('Net Revenue')
                        py.grid(True)
                        py.legend(loc=1)
                        py.xticks(x, rotation=90)
                    else:
                        labels = ['Indian Oil', 'Bharat Petroleum', 'Hindustan Petroleum', 'ONGC', 'GAIL']
                        for year in multi_year:
                            x = [int(year) for year in multi_year]
                        for brand_index in brand_indices:
                            p = []
                            ind1 = []
                            for year in multi_year:
                                year_index = 2023 - year
                                ind1.append(brand_index + (year_index * 5))
                            p = df.iloc[ind1, 2].str.replace(',', '', regex=True).astype(float)
                            y = p.sort_values().tolist()
                            py.plot(x, y, label=labels[brand_index])
                            py.xlabel('Years')
                            py.ylabel('Net Revenue in US Dollars')
                            py.title('Net Revenue Over Years')
                            py.grid(True)
                            py.legend(loc=1)
                            py.xticks(x, rotation=90)

                elif analyse_no1_revenue == 2:
                    if no_of_yrs_brandmulti == 1:
                        x = [int(year) for year in multi_year]
                        p = df.iloc[ind, 7].str.replace(',', '', regex=True).astype(float)
                        y = p.sort_values()
                        labels = ['Indian Oil', 'Bharat Petroleum', 'Hindustan Petroleum', 'ONGC', 'GAIL']

                        for brand_index in brand_indices:
                            py.plot(x, y, label=labels[brand_index])
                        py.xlabel('Years')
                        py.ylabel('Gross Revenue in US Dollars')
                        py.title('Gross Revenue')
                        py.grid(True)
                        py.legend(loc=1)
                        py.xticks(x, rotation=90)
                    else:
                        labels = ['Indian Oil', 'Bharat Petroleum', 'Hindustan Petroleum', 'ONGC', 'GAIL']
                        for year in multi_year:
                            x = [int(year) for year in multi_year]
                        for brand_index in brand_indices:
                            p = []
                            ind1 = []
                            for year in multi_year:
                                year_index = 2023 - year
                                ind1.append(brand_index + (year_index * 5))
                            p = df.iloc[ind1, 2].str.replace(',', '', regex=True).astype(float)
                            y = p.sort_values().tolist()
                            py.plot(x, y, label=labels[brand_index])
                            py.xlabel('Years')
                            py.ylabel('Gross Revenue in US Dollars')
                            py.title('Gross Revenue Over Years')
                            py.grid(True)
                            py.legend(loc=1)
                            py.xticks(x, rotation=90)

                elif analyse_no1_revenue == 3:
                    if no_of_yrs_brandmulti == 1:
                        x = [int(year) for year in multi_year]
                        p = df.iloc[ind, 7].str.replace(',', '', regex=True).astype(float)
                        y = p.sort_values()
                        labels = ['Indian Oil', 'Bharat Petroleum', 'Hindustan Petroleum', 'ONGC', 'GAIL']

                        for brand_index in brand_indices:
                            py.plot(x, y, label=labels[brand_index])
                        py.xlabel('Years')
                        py.ylabel('Total Revenue in US Dollars')
                        py.title('Total Revenue')
                        py.grid(True)
                        py.legend(loc=1)
                        py.xticks(x, rotation=90)
                    else:
                        labels = ['Indian Oil', 'Bharat Petroleum', 'Hindustan Petroleum', 'ONGC', 'GAIL']
                        for year in multi_year:
                            x = [int(year) for year in multi_year]
                        for brand_index in brand_indices:
                            p = []
                            ind1 = []
                            for year in multi_year:
                                year_index = 2023 - year
                                ind1.append(brand_index + (year_index * 5))
                            p = df.iloc[ind1, 2].str.replace(',', '', regex=True).astype(float)
                            y = p.sort_values().tolist()
                            py.plot(x, y, label=labels[brand_index])
                            py.xlabel('Years')
                            py.ylabel('Total Revenue in US Dollars')
                            py.title('Total Revenue Over Years')
                            py.grid(True)
                            py.legend(loc=1)
                            py.xticks(x, rotation=90)

                elif analyse_no1_revenue == 4:
                    if no_of_yrs_brandmulti == 1:
                        x = [int(year) for year in multi_year]
                        p = df.iloc[ind, 7].str.replace(',', '', regex=True).astype(float)
                        y = p.sort_values()
                        labels = ['Indian Oil', 'Bharat Petroleum', 'Hindustan Petroleum', 'ONGC', 'GAIL']

                        for brand_index in brand_indices:
                            py.plot(x, y, label=labels[brand_index])
                        py.xlabel('Years')
                        py.ylabel('Operating Revenue in US Dollars')
                        py.title('Operating Revenue')
                        py.grid(True)
                        py.legend(loc=1)
                        py.xticks(x, rotation=90)
                    else:
                        labels = ['Indian Oil', 'Bharat Petroleum', 'Hindustan Petroleum', 'ONGC', 'GAIL']
                        for year in multi_year:
                            x = [int(year) for year in multi_year]

                        for brand_index in brand_indices:
                            p = []
                            ind1 = []
                            for year in multi_year:
                                year_index = 2023 - year
                                ind1.append(brand_index + (year_index * 5))
                            p = df.iloc[ind1, 2].str.replace(',', '', regex=True).astype(float)
                            y = p.sort_values().tolist()
                            py.plot(x, y, label=labels[brand_index])
                            py.xlabel('Years')
                            py.ylabel('Operating Revenue in US Dollars')
                            py.title('Operating Revenue Over Years')
                            py.grid(True)
                            py.legend(loc=1)
                            py.xticks(x, rotation=90)



            elif analyse_no_brandmulti == 2:
                print("What would you like to analyse?\nSelect 1 for profit/loss before tax \nSelect 2 for profit/loss after tax\n")
                analyse_no2_tax = int(input("Enter choice: "))
                if analyse_no2_tax < 1 or analyse_no2_tax > 2:
                    print("Invalid option. Please enter 1 or 2.")
                elif analyse_no2_tax == 1:
                    if no_of_yrs_brandmulti == 1:
                        x = [int(year) for year in multi_year]
                        p = df.iloc[ind, 7].str.replace(',', '', regex=True).astype(float)
                        y = p.sort_values()
                        labels = ['Indian Oil', 'Bharat Petroleum', 'Hindustan Petroleum', 'ONGC', 'GAIL']

                        for brand_index in brand_indices:
                            py.plot(x, y, label=labels[brand_index])
                        py.xlabel('Years')
                        py.ylabel('Profit/Loss before tax in US Dollars')
                        py.title('Profit/Loss before tax')
                        py.grid(True)
                        py.legend(loc=1)
                        py.xticks(x, rotation=90)
                    else:
                        labels = ['Indian Oil', 'Bharat Petroleum', 'Hindustan Petroleum', 'ONGC', 'GAIL']
                        for year in multi_year:
                            x = [int(year) for year in multi_year]
                        for brand_index in brand_indices:
                            p = []
                            ind1 = []
                            for year in multi_year:
                                year_index = 2023 - year
                                ind1.append(brand_index + (year_index * 5))
                            p = df.iloc[ind1, 6].str.replace(',', '', regex=True).astype(float)
                            y = p.sort_values().tolist()
                            py.plot(x, y, label=labels[brand_index])
                            py.xlabel('Years')
                            py.ylabel('Profit/Loss before tax in US Dollars')
                            py.title('Profit/Loss before tax over the years')
                            py.grid(True)
                            py.legend(loc=1)
                            py.xticks(x, rotation=90)

                elif analyse_no2_tax == 2:
                    if no_of_yrs_brandmulti == 1:
                        x = [int(year) for year in multi_year]
                        p = df.iloc[ind, 7].str.replace(',', '', regex=True).astype(float)
                        y = p.sort_values()
                        labels = ['Indian Oil', 'Bharat Petroleum', 'Hindustan Petroleum', 'ONGC', 'GAIL']

                        for brand_index in brand_indices:
                            py.plot(x, y, label=labels[brand_index])
                        py.xlabel('Years')
                        py.ylabel('Profit/Loss before tax in US Dollars')
                        py.title('Profit/Loss before tax')
                        py.grid(True)
                        py.legend(loc=1)
                        py.xticks(x, rotation=90)
                    else:
                        labels = ['Indian Oil', 'Bharat Petroleum', 'Hindustan Petroleum', 'ONGC', 'GAIL']
                        for year in multi_year:
                            x = [int(year) for year in multi_year]
                        for brand_index in brand_indices:
                            p = []
                            ind1 = []
                            for year in multi_year:
                                year_index = 2023 - year
                                ind1.append(brand_index + (year_index * 5))
                            p = df.iloc[ind1, 6].str.replace(',', '', regex=True).astype(float)
                            y = p.sort_values().tolist()
                            py.plot(x, y, label=labels[brand_index])
                            py.xlabel('Years')
                            py.ylabel('Profit/Loss before tax in US Dollars')
                            py.title('Profit/Loss before tax over Years')
                            py.grid(True)
                            py.legend(loc=1)
                            py.xticks(x, rotation=90)


            else:
                print("What would you like to analyse?\nSelect 1 for Equity Share Dividend\nSelect 2 for Tax On Dividend\nSelect 3 for Equity Dividend Rate (%)\n")
                analyse_no3_equity = int(input("Enter choice:"))
                if analyse_no3_equity < 1 or analyse_no3_equity > 3:
                    print("Invalid option. Please enter a number from 1 to 3.")
                elif analyse_no3_equity == 1:
                    if no_of_yrs_brandmulti == 1:
                        x = [int(year) for year in multi_year]
                        p = df.iloc[ind, 7].str.replace(',', '', regex=True).astype(float)
                        y = p.sort_values()
                        labels = ['Indian Oil', 'Bharat Petroleum', 'Hindustan Petroleum', 'ONGC', 'GAIL']

                        for brand_index in brand_indices:
                            py.plot(x, y, label=labels[brand_index])
                        py.xlabel('Years')
                        py.ylabel('Equity Share Dividend in US Dollars')
                        py.title('Equity Share Dividend')
                        py.grid(True)
                        py.legend(loc=1)
                        py.xticks(x, rotation=90)
                    else:
                        labels = ['Indian Oil', 'Bharat Petroleum', 'Hindustan Petroleum', 'ONGC', 'GAIL']
                        for year in multi_year:
                            x = [int(year) for year in multi_year]
                        for brand_index in brand_indices:
                            p = []
                            ind1 = []
                            for year in multi_year:
                                year_index = 2023 - year
                                ind1.append(brand_index + (year_index * 5))
                            p = df.iloc[ind1, 6].str.replace(',', '', regex=True).astype(float)
                            y = p.sort_values().tolist()
                            py.plot(x, y, label=labels[brand_index])
                            py.xlabel('Years')
                            py.ylabel('Equity Share Dividend in US Dollars')
                            py.title('Equity Share Dividend Over Years')
                            py.grid(True)
                            py.legend(loc=1)
                            py.xticks(x, rotation=90)

                elif analyse_no3_equity == 2:
                    if no_of_yrs_brandmulti == 1:
                        x = [int(year) for year in multi_year]
                        p = df.iloc[ind, 7].str.replace(',', '', regex=True).astype(float)
                        y = p.sort_values()
                        labels = ['Indian Oil', 'Bharat Petroleum', 'Hindustan Petroleum', 'ONGC', 'GAIL']

                        for brand_index in brand_indices:
                            py.plot(x, y, label=labels[brand_index])
                        py.xlabel('Years')
                        py.ylabel('Tax On Dividend in US Dollars')
                        py.title('Tax On Dividend')
                        py.grid(True)
                        py.legend(loc=1)
                        py.xticks(x, rotation=90)
                    else:
                        labels = ['Indian Oil', 'Bharat Petroleum', 'Hindustan Petroleum', 'ONGC', 'GAIL']
                        for year in multi_year:
                            x = [int(year) for year in multi_year]
                        for brand_index in brand_indices:
                            p = []
                            ind1 = []
                            for year in multi_year:
                                year_index = 2023 - year
                                ind1.append(brand_index + (year_index * 5))
                            p = df.iloc[ind1, 6].str.replace(',', '', regex=True).astype(float)
                            y = p.sort_values().tolist()
                            py.plot(x, y, label=labels[brand_index])
                            py.xlabel('Years')
                            py.ylabel('Tax On Dividend in US Dollars')
                            py.title('Tax On Dividend Over Years')
                            py.grid(True)
                            py.legend(loc=1)
                            py.xticks(x, rotation=90)

                elif analyse_no3_equity == 3:
                    if no_of_yrs_brandmulti == 1:
                        x = [int(year) for year in multi_year]
                        p = df.iloc[ind, 7].str.replace(',', '', regex=True).astype(float)
                        y = p.sort_values()
                        labels = ['Indian Oil', 'Bharat Petroleum', 'Hindustan Petroleum', 'ONGC', 'GAIL']

                        for brand_index in brand_indices:
                            py.plot(x, y, label=labels[brand_index])
                        py.xlabel('Years')
                        py.ylabel('Equity Dividend Rate (%) in US Dollars')
                        py.title('Equity Dividend Rate (%)')
                        py.grid(True)
                        py.legend(loc=1)
                        py.xticks(x, rotation=90)
                    else:
                        labels = ['Indian Oil', 'Bharat Petroleum', 'Hindustan Petroleum', 'ONGC', 'GAIL']
                        for year in multi_year:
                            x = [int(year) for year in multi_year]
                        for brand_index in brand_indices:
                            p = []
                            ind1 = []
                            for year in multi_year:
                                year_index = 2023 - year
                                ind1.append(brand_index + (year_index * 5))
                            p = df.iloc[ind1, 6].str.replace(',', '', regex=True).astype(float)
                            y = p.sort_values().tolist()
                            py.plot(x, y, label=labels[brand_index])
                            py.xlabel('Years')
                            py.ylabel('Equity Dividend Rate (%) in US Dollars')
                            py.title('Equity Dividend Rate (%) Over Years')
                            py.grid(True)
                            py.legend(loc=1)
                            py.xticks(x, rotation=90)


            py.show()
            print("Your graph has been plotted")