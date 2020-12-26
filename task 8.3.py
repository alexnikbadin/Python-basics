class MyErrors(Exception):

    my_list = []

    def __init__(self):
        pass

    def put_in_mylist(self):
        while True:
            try:
                MyErrors.my_list.append(int(input("Enter something : ")))
            except ValueError:
                print('You entered the string!')
                break #не могу придумать как добавить условие с остановкой цикла "stop"
        return MyErrors.my_list


w = MyErrors()
w.put_in_mylist()
print(MyErrors.my_list)
