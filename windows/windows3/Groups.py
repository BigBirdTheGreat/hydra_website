PepsTog = 0
PepsNotApart = 0
NumTogether = int(input())
TogetherList = []
ApartList = []
GroupList = []
Violations = 0

for i in range(NumTogether):
    TogetherList.append(input().split())

NumApart = int(input())


for i in range(NumApart):
    ApartList.append(input().split())

TotalGroups = int(input())

for i in range(TotalGroups):
    GroupList.append(input().split())

for i in range(len(GroupList)):
    for j in range(len(TogetherList)):
        if TogetherList[j][0] in GroupList[i] and TogetherList[j][1] in GroupList[i]:
            PepsTog += 1
    for k in range(len(ApartList)):
        if ApartList[k][0] in GroupList[i] and ApartList[k][1] in GroupList[i]:
            PepsNotApart += 1

Violations = len(TogetherList) - PepsTog + PepsNotApart

print(Violations)

