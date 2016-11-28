import requests
import string
from bs4 import BeautifulSoup
from imdbpie import Imdb
from operator import itemgetter, attrgetter, methodcaller
#initialisation
imdb = Imdb()
imdb = Imdb(anonymize=True) # to proxy requests
imdb = Imdb(cache=True)




def sort_upon_rating(list):
    temp_list=[]
    for i in list:
        temp_list.append(i.split("###"))

    sorted_list = sorted(temp_list, key=itemgetter(2))
    sorted_list.reverse()
    final_list = []
    temp_list = []
    for i in sorted_list:
        if len(i)>=4:
            if i[2] is not None:
                temp_list.append(i[0] + "###" + i[1] + "###" + i[2] + i[3])
            else:
                final_list.append(i[0] + "###" + i[1] + "###" + i[2] + i[3])


    return final_list+temp_list







def traverse():
    file = open('movie_list2.txt', 'r')
    list = file.readlines()
    file.close()
    final_list = []
    for i in list:
        if(len(i)<2):
            continue


        # print(i)
        name =i.split("###")[0][:len(i.split("###")[0])-1]
        year =i.split("###")[1][:4]
        rating = get_movie_rating(name,year)
        print(name,year,rating)
        final_list.append(name+"###"+year+"###"+str(rating)+"###"+"\n")
        # print(name,year)

    final_list = sort_upon_rating(final_list)
    return final_list


def get_movie_rating(name,year):
    temp_list = imdb.search_for_title(name)
    for i in temp_list:
        if i['title']==name and i['year']==year:
            magic_id = i['imdb_id']
            title = imdb.get_title_by_id(magic_id)
            return title.rating

    return '0'


def write_all():
    file = open('final_movie_list','w')
    file.writelines(traverse())
    file.close()


write_all()
# print(get_movie_rating('A Better Life','2011'))