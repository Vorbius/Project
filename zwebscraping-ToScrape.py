from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.request import urlopen, Request
from plotly.graph_objs import Bar
from plotly import offline

Authors={}
Authors_List=[]
Authors_List1=[]
Authors_Length=[]
Authors_Length1=[]
Tags={}
Tags_List=[]
Tags_List1=[]
Tags_Lengths=[]
Tags_Lengths1=[]
Quote_Length=0
Total_Quote_Length=0
Quote_L={}
l_quote=[]
s_quote=[]
s_quote1=[]
p_tag=[]
p_tag1=''
l_tag=''
t_tag=0
m_Auth=''
l_Auth=[]
value=0
x=1
q=1
for i in range(1,11):
    url = f'http://quotes.toscrape.com/page/{i}/'
    
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}
    req = Request(url, headers=headers)

    webpage= urlopen(req).read()

    soup=BeautifulSoup(webpage,'html.parser')
    quotes=soup.find_all('div',class_='quote')
    for quote in quotes:
        text=quote.find('span',class_='text')
        Author=quote.find('small',class_='author')
        Quoted=text.text
        Author=Author.text
        if Author not in Authors:
            Authors[Author]=1
        else:
            Authors[Author]+=1
        tags=quote.find_all('a',class_='tag')
        for t in tags:
            t=t.text
            if t not in Tags:
                Tags[t]=1
            else:
                Tags[t]+=1
        #print(text.text)
        for i in Quoted:
            if i == ' ':
                #print(i)
                Quote_Length+=1
        Quote_Length+=1
        Quote_L[f'Quote {q}']=Quote_Length
        Total_Quote_Length+=Quote_Length
        Quote_Length=0
        q+=1
        #print(Tags)
        #print(Authors)
        #print(text.text)
        #print(input())
    
    #print(quotes)
    text=soup.find('span',class_='text')
    #print(text.text)
    #print(f'End of page {x}')
    x+=1
    #print(input())
for key in Authors:
    Authors_List.append(key)
    Authors_Length.append(Authors[key])
    if value<Authors[key]:
        value=Authors[key]
        m_Auth=key
    if Authors[key]==1:
        l_Auth.append(key)
value5 = 0 
value2=float('inf')
value3=' '
for i in Quote_L:
    if value5<Quote_L[i]:
        value5=Quote_L[i]
        l_quote=i
    if Quote_L[i] <= value2:
        value2=Quote_L[i]
        s_quote.append(Quote_L[i])
        value3=Quote_L[i]
for i in s_quote:
    if i == value3:
        s_quote1.append(i)
value2=float('-inf')
for i in Tags:
    Tags_List.append(i)
    Tags_Lengths.append(Tags[i])
    t_tag+=1
    if Tags[i] >= value2:
        value2=Tags[i]
        p_tag.append(i)
        value4=i
for i in p_tag:
    if i == value4:
        p_tag1=i
for i in Tags:
    t_tag+=1
Authors_List=sorted(Authors.items(), key=lambda item: item[1], reverse=True)
Tags_List=sorted(Tags.items(), key=lambda item: item[1], reverse=True)
Authors_List=dict(Authors_List)
Tags_List=dict(Tags_List)
Tags_List1=list(Tags_List.keys())[:10]
Authors_List1=list(Authors_List.keys())[:10]
Tags_Lengths1=list(Tags_List.values())[:10]
Authors_Length1=list(Authors_List.values())[:10]
'''
for i in Authors_List[:10]:
    Authors_List1.append(i)
    Authors_Length1.append(Authors_List[i])
for i in Tags_List[:10]:
    Tags_List1.append(i)
    Tags_Lengths1.append(Tags_List[i])
'''
print(Authors)
print(f'{m_Auth} has the most quotes at a total of {value}')
print('The Authors with the lowest amount of quotes (1) are as follows:')
for i in l_Auth:
    print(i)
print(Tags)
print(f'The average lenght of a quote is {round(Total_Quote_Length/q,1)} words')
print(f'The longest quote is {l_quote} with a length of {Quote_L[l_quote]}')
print(f'There are {len(s_quote1)} quotes with a length of {value3} words and are as follows:')
for i in Quote_L:
    if Quote_L[i]==value3:
        print(i)
print(f'The most popular tag is {p_tag1} by appearing a total of {Tags[p_tag1]} times')
print(f'Overall, there were {(len(Tags))} unique tags')
#print(Quote_L)
data = [
    {
        "type": "bar",
        "x":Authors_List1,
        "y":Authors_Length1,
        "marker": {
            "color" : "rgb(60,100,150)",
            "line": {"width":1.5,"color":"rgb(25,25,25)"}
        },
        "opacity": 0.6,
    }
]
my_layout={
    "title":'Authors on "Quotes to Scrape" by how much they appear',
    "xaxis":{"title": "Authors"},
    "yaxis":{"title":"Times Quoted"},
}
fig = {"data": data, "layout": my_layout}

offline.plot(fig,filename="python_repos.html")

data = [
    {
        "type": "bar",
        "x":Tags_List1,
        "y":Tags_Lengths1,
        "marker": {
            "color" : "rgb(60,100,150)",
            "line": {"width":1.5,"color":"rgb(25,25,25)"}
        },
        "opacity": 0.6,
    }
]
my_layout={
    "title":'Most common Tags on "Quotes to Scrape"',
    "xaxis":{"title": "Tags"},
    "yaxis":{"title":"Times Tagged"},
}
fig = {"data": data, "layout": my_layout}

offline.plot(fig,filename="Website To Scrape.html")