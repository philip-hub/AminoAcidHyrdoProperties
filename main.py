sequenceList = ["ACD","ACDACD"]
aminoAcid= ["N","L","W","W","L","W","N","L","W",]
aminoDict ={"A":"N" ,"C":"L" ,"D":"W" ,"E":"W" ,"F":"L" ,"G":"W" ,
            "H":"N" ,"I":"L" ,"L":"W" ,"K":"W" ,"M":"L" ,"N":"W" ,
            "P":"W","Q":"W","R":"W","S":"W","T":"W","V":"L","W":"L",
            "Y":"N", "X":"N"} #X as a padding charector

def sequenceHandler(sequence, aminoDict, index, newString):
    aminoAcid = sequence[index]
    hydroChar = aminoDict.get(aminoAcid)
    if hydroChar == "L":
        hydroChar = "H"
    elif hydroChar == "W":
        hydroChar = "P"
    newString = newString + hydroChar
    if index == len(sequence) - 1:
        return newString
    else:
        return sequenceHandler(sequence, aminoDict, index + 1, newString)

def sequenceCoverter(sequenceList, aminoDict, index, newList):
    sequence = sequenceList[index]
    newList.append(sequenceHandler(sequence, aminoDict, 0, ""))
    if index == len(sequenceList) - 1:
        return newList
    else:
        return sequenceCoverter(sequenceList, aminoDict, index + 1, newList)

resultList = []
newList = sequenceCoverter(sequenceList, aminoDict, 0, resultList)
print(newList)
