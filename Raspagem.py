import requests
import re
import xlsxwriter
from bs4 import BeautifulSoup
playerlist=[]
rankplayer=[]
LPList=[]
LVLList=[]
vitoriaList=[]
derrotaList=[]
pctList=[]
z=101
o='#'
cont=0
for a in range(1,1001):
    print("P", a)
    url ="http://br.op.gg/ranking/ladder/page="+str(a)
    req = requests.get(url)
    soup = BeautifulSoup(req.content, "html.parser")
    ############################################################################################
    getstuff = soup.findAll('td',{'class':'ranking-table__cell ranking-table__cell--summoner'})
    for player in getstuff:
        x=str(player.find('span'))
        x=x[6:]
        x=x[:-7]
        playerlist.append(x)


    ############################################################################################
    getstuff = soup.findAll('td',{'class':'ranking-table__cell ranking-table__cell--tier'})
    for rank in getstuff:
        x=str(rank)
        x=re.sub(r'(^[ \t]+|[ \t]+(?=:))', '', x, flags=re.M)
        x=x[59:]
        x=x[:-6]
        rankplayer.append(x)
    
    ###########################################################################################
    getstuff = soup.findAll('td',{'class':'ranking-table__cell ranking-table__cell--lp'})
    for LP in getstuff:
        x=str(LP)
        x=re.sub(r'(^[ \t]+|[ \t]+(?=:))', '', x, flags=re.M)
        x=x[57:]
        x=x[:-9]
        x=int(x.replace(',',''))
        LPList.append(x)
    
    ###########################################################################################
    getstuff = soup.findAll('td',{'class':'ranking-table__cell ranking-table__cell--level'})
    for LVL in getstuff:
        x=str(LVL)
        x=re.sub(r'(^[ \t]+|[ \t]+(?=:))', '', x, flags=re.M)
        x=x[60:]
        x=x[:-6]
        LVLList.append(int(x))
    
    ###########################################################################################
    getstuff = soup.findAll('div',{'class':'winratio-graph__text winratio-graph__text--left'})
    for vitoria in getstuff:
        x=str(vitoria)
        x=x[61:]
        x=x[:-6]
        vitoriaList.append(int(x))
    ##########################################################################################
    getstuff = soup.findAll('span',{'class':'winratio__text'})
    for pct in getstuff:
        x=str(pct)
        x=x[29:]
        x=x[:-7]
        pctList.append(str(x))
    ###########################################################################################
    getstuff = soup.findAll('div',{'class':'winratio-graph__text winratio-graph__text--right'})
    
    for derrota in getstuff:
        x=str(derrota)
        x=x[62:]
        x=x[:-6]
        derrotaList.append(int(x))
        cont=cont+1
    ######################################
    if a == z:
        print('[',o ,']')
        o=o+"#"
        z = (z+z)-1
    
##########################################################################################
print("Players")
print(len(playerlist))
print("Rank")
print(len(rankplayer))
print("LVL")
print(len(LVLList))
print("LP")
print(len(LPList))
for y in range(0,5):
    vitoriaList.pop(0)
print("Vitorias")
print(len(vitoriaList))

for y in range(0,5):
    derrotaList.pop(0)
print("Derrotas")
print(len(derrotaList))

for y in range(0,5):
    pctList.pop(0)
print("Porcentagem de vitorias")
print(len(pctList))
for y in range(0,len(pctList)):
    if pctList[y]=='100%':
        derrotaList.insert(y,0)
print(len(derrotaList))
excel = xlsxwriter.Workbook('Raspagem.xlsx')
worksheet = excel.add_worksheet()
row=0
col=0
for item in playerlist:
    worksheet.write(row, col, item)
    worksheet.write(row, col+1, rankplayer[row])
    worksheet.write(row, col+2, LPList[row])
    worksheet.write(row, col+3, LVLList[row])
    worksheet.write(row, col+4, vitoriaList[row])
    worksheet.write(row, col+5, derrotaList[row])
    worksheet.write(row, col+6, pctList[row])
    row = row + 1
excel.close()
