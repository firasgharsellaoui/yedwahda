import io
f =  io.open("result.txt", mode="r", encoding="utf-8")
s= f.read()
whip = eval(s)

t=["الكرم", "المرسى", "باردو", "تونس", "حلق الوادي", "سيدي بوسعيد", "سيدي حسين", "قرطاج"]
key= [ "بناء التجهيزات الجماعية للثقافة والشباب والرياضة والطفولة وتهيئتها","المساحات الخضراء ومداخل المدن","أشغال التهيئة والتهذيب", "التطهير","الإنارة"]
d={}

r= {}
for a in whip:
    for k in key:
        for i in range(2017, 2010, -1):
            print(whip[a][str(i)])
            if (k in whip[a][str(i)]):
                if(not(k in r)):
                    r[k]= [0,0]
                r[k][0]+= whip[a][str(i)][k]
                r[k][1]+=1
                break
print (r)
