from dataset import users, countries



from pprint import pprint
#Point1
users_wrong_password = []

for user in users:
    if user['password'].isdigit():
        users_wrong_password.append({'name':user['name'], 'mail':user['mail']})



#point2
drivers_girls = []

for friend in user.get('friends'):
    if friend['sex'] == 'F' and friend.get('cars'):
        drivers_girls.append({friend['name']})

#point3
best_occupation = []
salary_comparison = 0

for money in user.get('friends'):
    if money['job']['salary'] > salary_comparison:
        salary_comparison = money['job']['salary']
        best_occupation = {'occupation':money['job']['occupation'],'salary':money['job']['salary']}
        
#point4
vip_user = []
max_salary = 0
for money in user.get('friends'):
    if money['job']['salary'] > max_salary:
        max_salary = money['job']['salary']
        vip_user = money['name']


#point5
flight_user = 0
flight_check = 0
cars = 0
cars_check = 0

for flight in user.get('friends'):
    if 'flights' in flight:
        flight_check = len(flight['flights'])
        flight_user += flight_check
        if flight.get('cars'):
            cars_check = len(flight['cars'])
            cars += cars_check
avg_flights = flight_user / cars
#Не догнал как сделать 5 знаков после точки и как сделать так чтоб не было делении на ноль при отсутвии машин у пользователя

#point6 вообще сильно затупил нужна помощь
check = []
for del_user in user.get('friends'):
    if del_user.get('flights'):
        check = del_user['flights']

i = 0


while i < len(check):
    for j in check:
        if j['country'] in countries:
            del users[i]



    
    


            









# print(friend['job']['salary']) #залезли в фриендс-> джоб