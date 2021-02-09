########################################################################################################################

# first build - 2nd aug 2020
# Mastery Calculator Application

########################################################################################################################



########################################################################################################################

# get information about mastery type, hours accumulated, years since started etc
mastery_name = input('\n'
                     'What is the subject you want to master?:\n')

subject_years_passed = float(input('Roughly how many years have you\n'
                               'already spent on the subject?:\n'))

past_weekly_hours = float(input('How many hours were you devoting in the past\n(per week):\n'))

weekly_mastery_addition = float(input('How many hours do you spend\n'
                                    'on the subject weekly?:\n'))


########################################################################################################################

# take data on how many past years have been devolved towards the mastery
# take (number of years) x (past weekly hours * weeks in a year) to get the
# past total number of hours devolved towards the mastery subject
past_hours = int((past_weekly_hours * 52.1429) * (subject_years_passed))

# take data on how many hours a week the user devolves towards the task
# and multiply that times the weeks a year (52 weeks in 365 days)
yearly_hours = int(weekly_mastery_addition * 52.1429)
yearly_hours_percentage = int(yearly_hours * 100 / 10000)

# tell the user how the percentage of completion towards 10k hours aka mastery
percentage_to_completion = int((past_hours * 100) / 10000)
percentage_left = int(100 - percentage_to_completion)


########################################################################################################################

# print all results
print(' ')
print('--------------------------------------')
print('--------------------------------------')
print(' ')

# print name of mastery to complete
print('Mastery to complete:\n' + (mastery_name).upper())
print(' ')
print('--------------------------------------')

# accumulated hours
print('Your Total Hours Accumulated:\n' + str(past_hours) + ' hours.')

# yearly hours following weekly hours
print('Your yearly total towards Mastery\n(at ' + str(weekly_mastery_addition) +
      ' hours a week)\nis:', str(yearly_hours) + ' hours a year.')
print(' ')
print('--------------------------------------')

# percentage to mastery and percentage left to master
print('Current Track to Mastery..\n'
      'Percentage of Mastery:', percentage_to_completion, '%')
print('Percentage Left:', percentage_left, '%')
print(' ')
print('--------------------------------------')


########################################################################################################################

# percentage after 1,2,3,4 years
# after 1 year
print('After 1 more year..\n'
      'Percentage of Mastery:',(percentage_to_completion + yearly_hours_percentage), '%\n'
      'Percentage Left:', (100 - (percentage_to_completion + yearly_hours_percentage)), '%')
print(' ')
print('--------------------------------------')
print('--------------------------------------')

########################################################################################################################
