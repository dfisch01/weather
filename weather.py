
# coding: utf-8

# In[4]:


from bs4 import BeautifulSoup as bs

import texttable as tt 

import requests, time

header = ['Time', 'Prediction', 'Temperature', 'Precipitation']
time = []
prediction = []
temp = []
precip = []

zipcode = input('Enter zipcode: ')
url = 'https://weather.com/weather/hourbyhour/l/%s' % (zipcode)

def get_url():
    
    place = requests.get(url)
    soup = bs(place.text, 'html.parser')
    
    return soup


def get_time():

    soup = get_url()
    span = soup.findAll('span', {'class': 'dsx-date'})
    

    for x in span:
        time_real = x.text
        time.append(time_real)
        

def get_prediction():
    
    soup = get_url()
    pred = soup.findAll('td', {'class':'hidden-cell-sm description'})
    
    for x in pred:
        description = x.text
        prediction.append(description)
    
def get_temp():
    
    soup = get_url()
    temperature = soup.findAll('td', {'class': 'temp'})
    
    for x in temperature:
        temp_real = x.text
        temp.append(temp_real)
        
def get_precip():
    
    soup = get_url()
    precipitation = soup.findAll('td', {'class': 'precip'})
    
    for x in precipitation: 
        percent = x.text
        precip.append(percent)
        
def display_data():
    get_time()
    get_prediction()
    get_temp()
    get_precip()
    
    tab = tt.Texttable()
    tab.header(header)
    for row in zip(time,prediction,temp,precip):
        tab.add_row(row)
        
    table = tab.draw()
    print(table)
    
display_data()
              

