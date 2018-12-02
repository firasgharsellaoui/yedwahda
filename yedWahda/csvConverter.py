import xlrd
#import simplejson
import os
import simplejson
from collections import OrderedDict

def isSheetOkay(sheet):
    if(not(usefulSheet.cell(1, 4).ctype == 2)):
        return (1)
    else:
        if(not(usefulSheet.cell(1, 0).ctype == 1)):
            return (2)
        else:
            if(usefulSheet.cell(1, 4).value == 0):
                return(1)
    return(3)

keywordDict ={}
directoriesPath =r"C:\Users\HP\Desktop\Saisie 2018"
numberOfGoodSheets =0
numberOfEmptySheets =0
numberOfWierdSheets =0
result ={}
for root, dirs, files in os.walk(directoriesPath):
    for dir in dirs:
        filesPath = directoriesPath+ "\\" + dir
        for r,d,fs in os.walk(filesPath):
            for f in fs:
                cityDict={}
                filePath= filesPath + "\\" + f
                pointPos = f.find('.')
                if(not(pointPos == -1)):
                    cityName = f[:pointPos]
                    cityDict["gouvernorat"]= dir
                try:
                    book =xlrd.open_workbook(filePath)
                    for i in range(2011,2018):
                        yearDict ={}
                        sheetName =  "ميزانية" + " " +str(i)
                        try:
                            usefulSheet = book.sheet_by_name(sheetName)
                            if(isSheetOkay(usefulSheet)==3):
                                numberOfGoodSheets+=1
                                # print "Processing sheet no ", sheet_index
                                #firstDepenses = usefulSheet.cell(256,4).value
                                #secondDepenses = usefulSheet.cell(559,4).value
                                #result["total"]= firstDepenses+ secondDepenses
                                #cellName = usefulSheet.cell(562,0)
                                #cellValue = usefulSheet.cell(562,4)
                                #print(cellName.value,cellValue.value)
                                # print attributes
                                for rownum in range(1, usefulSheet.nrows):
                                    currentCell =str(usefulSheet.cell(rownum, 0).value)
                                    if(ord(currentCell[0]) > 1500):
                                        sep =currentCell.find(":")
                                        currentCell = currentCell[sep+1:]
                                        currentValue = usefulSheet.cell(rownum,4).value
                                        yearDict[currentCell] = currentValue
                                        if(not(currentCell in keywordDict)):
                                            keywordDict[currentCell] ={"2011":[0,0,0],"2012":[0,0,0],"2013":[0,0,0],"2014":[0,0,0],"2015":[0,0,0],"2016":[0,0,0],"2017":[0,0,0]}
                                        try:
                                            if (int(currentValue)):
                                                ((keywordDict[currentCell])[str(i)])[1]+=1
                                                ((keywordDict[currentCell])[str(i)])[2] += currentValue
                                            else:
                                                ((keywordDict[currentCell])[str(i)])[0]+=1
                                        except ValueError:
                                            ((keywordDict[currentCell])[str(i)])[0] += 1
                                    else:
                                        currentCell = str(usefulSheet.cell(rownum, 1).value)
                                        if (ord(currentCell[0]) > 1500):
                                            sep = currentCell.find(":")
                                            currentCell = currentCell[sep + 1:]
                                            currentValue = usefulSheet.cell(rownum, 4).value
                                            yearDict[currentCell] = currentValue
                                            if (not (currentCell in keywordDict)):
                                                keywordDict[currentCell] = {"2011": [0, 0, 0], "2012": [0, 0, 0],
                                                                            "2013": [0, 0, 0], "2014": [0, 0, 0],
                                                                            "2015": [0, 0, 0], "2016": [0, 0, 0],
                                                                            "2017": [0, 0, 0]}
                                            try:
                                                if (int(currentValue)):
                                                    ((keywordDict[currentCell])[str(i)])[1] += 1
                                                    ((keywordDict[currentCell])[str(i)])[2] += currentValue
                                                else:
                                                    ((keywordDict[currentCell])[str(i)])[0] += 1
                                            except ValueError:
                                                ((keywordDict[currentCell])[str(i)])[0] += 1
                                    """for key in keyWords:
                                        if(key == currentCell):
                                            currentCell= currentCell[11:]
                                            print(currentCell,usefulSheet.cell(rownum, 4).value)"""
                                    #print(currentCell)
                                cityDict[str(i)]= yearDict
                            else:
                                if (isSheetOkay(usefulSheet) == 2):
                                    numberOfWierdSheets+=1
                                    cityDict[str(i)] = yearDict
                                else:
                                    numberOfEmptySheets+=1
                                    cityDict[str(i)] = yearDict
                        except:
                            numberOfWierdSheets += 1
                            cityDict[str(i)] = yearDict
                        #print(cityDict)
                    result[cityName] = cityDict
                except:
                    print (filesPath,"didnt work :/")
                """rows_list = []
                attr_list = []
                # print attr_list[0]

                for rownum in range(1, usefulSheet.nrows):
                    row_val_list = usefulSheet.row_values(rownum)
                    row_dict = OrderedDict()
                    for index in range(len(attr_list)):
                        row_dict[attr_list[index]] = row_val_list[index]
                    rows_list.append(row_dict)
                    json_data = simplejson.dumps(rows_list)
                    print(json_data)

                print(row_dict)"""
            #print("done")
"""f = open("result.txt", "w" , encoding="utf-8")
f.write(str(result))
f.close()"""
#wb = xlrd.open_workbook(r"")
moyenne={}
for k in keywordDict:
    t= True
    for i in range(2011,2018):
        moyenne[k]={}
        if(keywordDict[k][str(i)][1]):
            moyenne[k][str(i)]= keywordDict[k][str(i)][2]/keywordDict[k][str(i)][1]
        else:
            moyenne[k][str(i)]=0

