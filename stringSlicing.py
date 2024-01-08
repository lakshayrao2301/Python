#slicing creating a substring by extracting elements from another string

    #we can either user indexing[] operator or slice() function

            #[start:stop:step] first(start) index is inclusive & stop index is exclusive
            #step is mainly use for creating substring it increment 1 by default

# 1. Slicing By indexing operator
name= "Lakshay Yadav"

first_name= name[0:7]
first_name= name[:7] # both are same
#python will assume start index 0 if we leave start index empty
print(first_name)

last_name= name[8:13]
last_name= name[8:]
#in python if we leave stop index empty it will print to the last element
print(last_name)

nick_name=name[0:13:2] # it will display every 2nd character
nick_name=name[::2]
# it will assume start from 0 and stop at last with increment of 2
print(nick_name)


reversed_name= name[::-1]#it will reverse my name & use from reverse the string
print(reversed_name)

# 2.By using slice function

website1="http://google.com"
website2="http://yahoo.com"

# slice(start,stop,step)
slice = slice(7,-4) #it will give only website name
# stop index in negative because in the last all website has same domains so we use negative indexing

print(website1[slice])
print(website2[slice])


