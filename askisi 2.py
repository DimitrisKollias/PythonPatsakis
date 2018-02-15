import requests
import json
from datetime import datetime, timedelta
from pprint import pprint

#req = requests.get('http://applications.opap.gr/DrawsRestServices/kino/last.json')


inputs = [] #the array the 10 inputs wil be stored

for i in range(10):
    inputs.append(int(input("Enter #" + str(i+1) +" KINO number: ")))
    #inputs.append(i)


#since we need to find the best matches of the month, we search
#in the opap database for the last 30 days


now = datetime.now();

max_day = ""
max_count = 0

for i in range(30):
    
    past_date = now - timedelta(i)
    date_final = past_date.strftime('%d-%m-%Y')
    url = 'http://applications.opap.gr/DrawsRestServices/kino/drawDate/'+date_final+'.json' #we get the data using http request from the opap server
    req = requests.get(url)
    data = req.json()
    draw = data['draws']['draw'][0:] #here we open the json file and pass through the "array" elements
    day_successes_counter = 0
    for j in range(len(draw)):
        final_draw_array = data['draws']['draw'][j]['results'] #here we parse the params to a temp array

        #here we check if the 10 given numbers are in the temp array and store the equal nums to a counter
        counter = 0
        for k in range(10):
            if inputs[k] in final_draw_array:
                counter = counter + 1
        #print(counter)
        if (counter>=4):
            #print("Possible win in" + date_final)
            day_successes_counter = day_successes_counter + 1
        if (day_successes_counter > max_count):
            max_count = day_successes_counter
            max_day = date_final
        
print(max_day)
