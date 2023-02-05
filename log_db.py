
def save_data(result, message):
    file = open('db.csv', 'a')
    file.write(f' Result {str(result)} : {message.from_user.id} : {message.from_user.first_name}\n')
    print(message)
    file.close()