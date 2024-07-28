import matplotlib.pyplot as plt
import pandas as pd

#load the dataframe from the csv file
df_funding_rounds = pd.read_csv('datasets\\funding_rounds.csv')

def __main__():
    choice = 0
    while choice != '5':
        print('Press 1 for histogram')
        print('Press 2 for boxplot')
        print('Press 3 for scatter plot')
        print('Press 4 for average funding by round type')
        print('Press 5 to exit')
        choice = input('Enter your choice: ')
        if choice == '1':
            plt.hist(df_funding_rounds['raised_amount'], bins=30, alpha=0.5)
            plt.title('Distribution of Funding Amounts')
            plt.xlabel('Funding Amount')
            plt.ylabel('Frequency')
            plt.show()
        elif choice == '2':
            plt.boxplot(df_funding_rounds['raised_amount'])
            plt.title('Boxplot of Funding Amounts')
            plt.show()
        elif choice == '3':
            plt.scatter(df_funding_rounds['raised_at'], df_funding_rounds['raised_amount'])
            plt.title('Funding Amount Over Time')
            plt.xlabel('Date')
            plt.ylabel('Funding Amount')
            plt.show()
        elif choice == '4':
            average_funding_by_round = df_funding_rounds.groupby('funding_round_type')['raised_amount'].mean()
            average_funding_by_round.plot(kind='bar')
            plt.title('Average Funding Amount by Round Type')
            plt.xlabel('Round Type')
            plt.ylabel('Average Funding Amount')
            plt.show()

if __name__ == '__main__':
    __main__()
