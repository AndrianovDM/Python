def log(string):
    with open('C:\\Users\\Dmitry\\Downloads\\Postgraduate studies\\Homework program\\Python\\Seminar7\\history_log.txt','a', encoding = 'utf-8') as file:
        file.write(string + "\n")
    file.close()