import io
f =  io.open("result.txt", mode="r", encoding="utf-8")
s= f.read()
whip = eval(s)

t=["الكرم", "المرسى", "باردو", "تونس", "حلق الوادي", "سيدي بوسعيد", "سيدي حسين", "قرطاج"]
key= [ "بناء التجهيزات الجماعية للثقافة والشباب والرياضة والطفولة وتهيئتها","المساحات الخضراء ومداخل المدن","أشغال التهيئة والتهذيب", "التطهير","الإنارة"]
d={}
for k in t:
    d[k]={}
    for i in range(2017,2010,-1):
        s=0
        if (whip[k][str(i)] ):
            for h in whip[k][str(i)]:
               if(whip[k][str(i)][h] ):
                    val =whip[k][str(i)][h]
                    d[k][val]=h
            break
    for i,l in enumerate(d[k]):
        if(i>5):
            break
        else:
            d[k][l]