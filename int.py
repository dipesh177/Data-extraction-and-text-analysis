import requests
from bs4 import BeautifulSoup
import pandas as pd


def automizer(URL_ID,URL):
    #url='https://insights.blackcoffer.com/ai-in-healthcare-to-improve-patient-outcomes/'

    headers={'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/108.0.5359.112 Mobile/15E148 Safari/604.1'}
    r=requests.get(URL,headers=headers)
    print(r.status_code)
    soup=BeautifulSoup(r.content,features='lxml')
    headers=soup.find_all('header', class_='td-post-title')
    for item in headers:
        title=item.find({'h1':'entry-title'}).text
    #print(title)
    post_elements=soup.find_all('p')
    name=URL_ID+".txt"
    file=open(name,'w')
    try:
        file.write(title+"\n""\n")
    except:
        print("title doesn't exists")
    finally:
        file.write("empty title \n\n")
    
    for post in post_elements:
        print(post.text.strip(), end="\n"*2)
        file.write(post.text.strip()+"\n""\n")
    file.close()

def lil():
        df = pd.read_excel('Input.xlsx')
        df =  df.astype({'URL_ID':'str','URL':'str'})
        for ind in df.index:
            print(df['URL'][ind], df['URL_ID'][ind])
            automizer(df['URL_ID'][ind],df['URL'][ind])

def main():
    lil()

if __name__=="__main__":
    main()                