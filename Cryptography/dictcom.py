def dict_comp(stop, step):
    #floor division of step// stopto determine the range of the dictionery keys
    floor_division = stop//step
    #Multiplying the bove result by step to know the range of dictionery values
    floor_division = floor_division*step
    appender = []
    #Looping through the perfect range of values without any remainder
    for i in range(1, (stop//step)+1):
        appender.append('item-'+str(i))
    value_list = list(range(1, floor_division+1))

    list_range = range(1, len((value_list))+1)
    #Getting the chunk of data that will make individual dictionery values
    data_chunk = [list_range[step*i:step*(i+1)] for i in range(len(list_range)//step+1)]
    data_chunk = data_chunk[:len(data_chunk)-1]
    dict_values = []
    #Arranging the data in a single list
    for q in data_chunk:
        dict_values.append(list(q))
    #performing a dict comprehension to put it all together.
    dict_result = {key:value for (key,value) in zip(appender, dict_values)}
   
    return dict_result

#dict_comp(20, 2)

