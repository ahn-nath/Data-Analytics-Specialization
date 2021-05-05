import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv('adult.data.csv')
    # remove columns we will not use
    df.drop(columns = ['workclass', 'fnlwgt', 'education-num', 'marital-status', 'relationship', 'capital-gain', 'capital-loss'], 
        inplace = True)

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df.groupby(['race']).size().sort_values(ascending = False)

    # What is the average age of men?
    avg_age = df[df['sex'] == 'Male'].groupby(
        ['sex'])['age'].describe()[['mean']].reset_index('sex').iloc[0, 1]

    average_age_men =  round(avg_age, 1)

    # What is the percentage of people who have a Bachelor's degree?
    s = df.groupby(['education']).size() 
    percentage_bachelors = round(s.Bachelors / s.sum() * 100, 1) 

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    # rows with ''>50K'
    # group by education, get counts per group
    higher = df.salary[df['education'].isin(['Bachelors', 'Doctorate', 'Masters'])]
    lower = df.salary[~df['education'].isin(['Bachelors', 'Doctorate', 'Masters'])]

    # percentage with salary >50K
    higher_education_rich = round((higher[higher == '>50K'].count() / higher.count()) * 100, 1)

    lower_education_rich = round((lower[lower == '>50K'].count() / lower.count()) * 100, 1)

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df.loc[:,'hours-per-week'].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    # rows with ''>50K'
    high_salary = df[df['salary'] == '>50K']

    high_min_hours = high_salary[high_salary['hours-per-week'] == 1].index
    all_min_hours = df[df['hours-per-week'] == 1].index

    rich_percentage = round(len(high_min_hours) / len(all_min_hours), 1) * 100 

    # What country has the highest percentage of people that earn >50K?

    percentages_by_country =  round((high_salary.groupby(['native-country']).size()
               / df.groupby(['native-country']).size()) * 100.0, 1)
    
    highest_earning_country = percentages_by_country.sort_values(ascending = False).index[0]

    highest_earning_country_percentage = percentages_by_country.sort_values(ascending = False)[0]

    # Identify the most popular occupation for those who earn >50K in India.
    top_IN_occupation = high_salary[high_salary['native-country'] == 'India'].groupby(['occupation']).size().sort_values(
    ascending = False).head(1).index[0]

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
