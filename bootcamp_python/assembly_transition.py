
rMat = [[0, 1, 1, 0],
        [1, 0, 1, 0],
        [1, 1, 0, 1],
        [0, 0, 1, 0]]

# 알파벳과 숫자 매칭
cList = []
ntoa = {}
aton = {}

n = len(rMat)
for i in range(n):
    cList.append(chr(65+i))
    ntoa[i] = chr(65+i)
    aton[chr(65+i)] = i


"""   
ntoa = {0: 'A',
        1: 'B',
        2: 'C',
        3: 'D'}

aton = {'A': 0,
        'B': 1,
        'C': 2,
        'D': 3}

cList = ['A', 'B', 'C', 'D']
"""

#print(*rMat, sep='\n')


#step 1

#부품 2개를 합친다
def assemble(a, b):
    # ab + ac -> abc
    result = a

    c = set(a) | set(b)
    c = sorted(list(c))
    c = ''.join(s for s in c)

    return c

# 2개의 부품이 합쳐질 수 있는가?
def isAssemable(mainA, subA):

    #print(mainA, subA)

    #1개 이상의 부품들이 결합가능해야함
    assemable = False
    for c1 in mainA:
        for c2 in subA:
            if rMat[aton[c1]][aton[c2]] == 1:
                assemable = True
                break
    return assemable


def subassemble():
    subassem = []

    lvl = 1

    for i in range(n):

        #각 레벨별 부품모음
        lvlassem = []

        # 1단계라면 하나씩 넣기
        if lvl == 1:
            for j in range(n):
                lvlassem.append(ntoa[j])
            subassem.append(lvlassem)

        # 마지막 단계라면 합쳐진 결과물 넣기
        elif lvl == n:
            assem = ""
            for j in range(n):
                assem += ntoa[j]
            lvlassem.append(assem)
            subassem.append(lvlassem)

        #중간단계
        else:

            # 각 레벨에는 레벨만큼의 부품이 합쳐져있음
            # 이전 레벨의 부품들이 합쳐져있음
            assem = ""

            # 이전 레벨의 부품들을 가져옴
            formerassem = subassem[lvl-2]

            #print("former:", formerassem)

            #메인 부품
            for i in formerassem:
                
                #합쳐보기
                for j in cList:

                    #부품들이 합쳐질 수 있는가 검사
                    if isAssemable(i, j):
                        assem = assemble(i, j)

                    # 합쳐진 부품이 중복이 아니라면 삽입
                        if not assem in lvlassem and len(assem) == lvl:
                            lvlassem.append(assem)
            subassem.append(lvlassem)

        #print(lvlassem)

        lvl += 1

    return subassem

    





#step 2


def makeNodes(subassem):

    nodes = []

    for i in subassem:

        mainAssem = i.copy()

        lvlAssem = []

        # 메인 부품에 없는 부품을 검사해서, 나머지 부품을 /로 표시
        lvl1 = True
        for j in i:
            lvlAssem = []

            # 1 단계라면

            if len(j) == 1:
                if lvl1:
                    temp = cList[0]
                    for k in range(1, len(cList)):
                        temp += ("/" + cList[k])
                    lvl1 = False
                    lvlAssem.append(temp)
                    nodes.append(lvlAssem)


            else:
                temp = []
                temp.append(j)
                differ = set(cList) - set(j)
                differ = list(differ)
                differ.sort()

                for k in differ:
                    temp.append(k)

                tempStr = temp[0]
                for k in range(1, len(temp)):
                    tempStr += ('/' +temp[k])

                lvlAssem.append(tempStr)
                nodes.append(lvlAssem)

    return nodes


#step 3


def isTransition(a, b):
    #b는 a보다 조립된 상태여야함
    aList = a.split('/')
    bList = b.split('/')


    # 각각 메인 부품들만 남긴다
    aList = getLongestString(aList)
    bList = getLongestString(bList)

    isTrans = False
    
    for c1 in aList:
        for c2 in bList:
            # 조립 상태는 한 번에 1레벨만 상승가능
            if len(c2) - len(c1) == 1:
                # 상위부품(b)가 하위부품(a)를 전부 포함해야함
                if containChar(c1, c2):
                    # a에서 b로 조립 가능한가 판별
                    isTrans = isAssemable(c1, c2)

    return isTrans

#a의 모든 문자가 b에 포함되는가
def containChar(a, b):
    for i in a:
        if not i in b:
            return False
    return True


# 문자열 리스트에서 가장 긴 문자열만 추출
# 가장 긴 문자열이 여러 개라면 동시에 추출
def getLongestString(aString):
    longest = 0
    for s in aString:
        if len(s) > longest:
            longest = len(s)

    longList = []

    for s in aString:
        if len(s) == longest:
            longList.append(s)

    return longList


def transitionMatrix(nodes2):
    n2 = len(nodes2)

    tMat = [[0]*n2 for _ in range(n2)]

    for i in range(n2):
        for j in range(n2):
            if i < j:
                if isTransition(nodes2[i], nodes2[j]):
                    tMat[i][j] = 1
                else:
                    tMat[i][j] = 0

            else:
                tMat[i][j] = 0

    return tMat



def doit():
    subassem = subassemble()
    print("Subassemblies for each level")
    print(subassem)

    subassem2 = sum(subassem, [])
    print("Subassemblies for every level")
    print(subassem2, "\n")
    #print(*subassem, sep='\n')



    nodes = makeNodes(subassem)
    print("Nodes for each level")
    print(nodes)

    nodes2 = sum(nodes, [])
    print("Nodes for every level")
    print(nodes2)




    tMat = transitionMatrix(nodes2)
    print("\nAssembly transition matrix")
    print(*tMat, sep='\n')


if __name__ == "__main__":
    doit()

