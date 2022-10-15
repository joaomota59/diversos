x=int(input())
horas=int(x/3600)
minutos=int((x%3600)/60)
segundos=(x%3600)%60
print("%d:%d:%d"%(horas,minutos,segundos))