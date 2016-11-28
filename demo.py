from operator import itemgetter, attrgetter, methodcaller


def to_str(list):
    a=''
    for i in list:
        a+=i+' '

    return a[:len(a)-1]




def sort_upon_rating():
    temp_list=return_data_list()

    sorted_list = sorted(temp_list, key=itemgetter(2))
    sorted_list.reverse()
    final_list = []
    temp_list = []
    for i in sorted_list:
        if len(i)>=4:
            if i[2] is not None:
                temp_list.append(i[0] + "   " + i[1] + "   " + i[2] + i[3])
            else:
                final_list.append(i[0] + "   " + i[1] + "   " + i[2] + i[3])


    a= final_list+temp_list
    file = open('bal','w')
    file.writelines(a)
    file.close()





def return_data_list():
    file = open('temp_movie_list', 'r')
    a = file.readlines()
    file.close()
    final_list=[]
    for i in a:
        list = i.split(' ')
        # print(list)
        if len(list) > 2:
            name = to_str(list[:len(list) - 2])
            year = list[len(list) - 2]
            rating = list[len(list) - 1]
            temp_list = []
            temp_list.append(name)
            temp_list.append(year)
            temp_list.append(rating)
            temp_list.append("\n")
            final_list.append(temp_list)
            # print(name, year, rating)
        else:
            print(i)

    return final_list


sort_upon_rating()