# pip install requests (to be able to get HTML pages and load them into Python)
# pip install bs4 (for beautifulsoup - python tool to parse HTML)


from urllib.request import urlopen, Request
from bs4 import BeautifulSoup


##############FOR MACS THAT HAVE ERRORS LOOK HERE################
## https://timonweb.com/tutorials/fixing-certificate_verify_failed-error-when-trying-requests_html-out-on-mac/

############## ALTERNATIVELY IF PASSWORD IS AN ISSUE FOR MAC USERS ########################
##  > cd "/Applications/Python 3.6/"
##  > sudo "./Install Certificates.command"



url = 'https://www.worldometers.info/coronavirus/country/us'
# Request in case 404 Forbidden error
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}

req = Request(url, headers=headers)

webpage= urlopen(req).read()

soup = BeautifulSoup(webpage, 'html.parser')

print(soup.title.text)




#SOME USEFUL FUNCTIONS IN BEAUTIFULSOUP
#-----------------------------------------------#
# find(tag, attributes, recursive, text, keywords)
# findAll(tag, attributes, recursive, text, limit, keywords)

#Tags: find("h1","h2","h3", etc.)
#Attributes: find("span", {"class":{"green","red"}})
#Text: nameList = Objfind(text="the prince")
#Limit = find with limit of 1
#keyword: allText = Obj.find(id="title",class="text")


table_rows= soup.findAll('tr')
state_death_ratio=''
state_best_testing=''
state_worst_testing=''
highest_death_ratio=0
highest_testing_ratio=0
worste_test_ratio  =100
#print(table_rows[:1])

for row in table_rows[2:52]:
    td = row.findAll('td')
    #print(td)
    state=td[1].text
    Total_Cases=int(td[2].text.replace(",",""))
    Total_deaths=int(td[4].text.replace(",",""))
    Total_tested=int(td[10].text.replace(",",""))
    Population=int(td[12].text.replace(",",""))
    #print(state)
    #print(Total_Cases)
    #print(Total_deaths)
    #print(Total_tested)
    #print(Population)
    death_ratio=Total_deaths/Total_Cases
    test_ratio=Total_tested/Population
    if death_ratio > highest_death_ratio:
        state_death_ratio=state
        highest_death_ratio=death_ratio
    if test_ratio > highest_testing_ratio:
        state_best_testing=state
        highest_testing_ratio=test_ratio
    if test_ratio < worste_test_ratio:
        worste_test_ratio=test_ratio
        state_worst_testing=state
print('State with the highest death ratio is: ',state_death_ratio)
print("Death Ratio: ",format(highest_death_ratio,".2%"))
print()
print()
print("State with the best testing ration is: ",state_best_testing)
print(f"Test Ratio: {highest_testing_ratio:.2%}")
print()
print()
print("State with the worst testing ratio is: ",state_worst_testing)
print(f"Test Ratio: {worste_test_ratio:.2%}")

