def minScore(n: int, roads: list[list[int]]) -> int:
        i=0
        pos=1
        res=[]
        print(pos)
        while pos!=n:

            if i>=len(roads):
                for j in range(len(roads)):
                    if(roads[j][1]==pos):
                        pos=roads[j][0]
                        res.append(roads[j][2])
                        roads.pop(j)
                        i=0
            print(roads)
            if(roads[i][0]==pos):
                pos=roads[i][1]
                res.append(roads[i][2])
                i+=1

            else:
                i+=1

            print(pos,i)
        return min(res)
minScore(4,[[1,2,9],[2,3,6],[2,4,5],[1,4,7]])
#minScore(4,[[1,2,2],[1,3,4],[3,4,7]])
#minScore(6,[[4,5,7468],[6,2,7173],[6,3,8365],[2,3,7674],[5,6,7852],[1,2,8547],[2,4,1885],[2,5,5192],[1,3,4065],[1,4,7357]])
#minScore(20,[[18,20,9207],[14,12,1024],[11,9,3056],[8,19,416],[3,18,5898],[17,3,6779],[13,15,3539],[15,11,1451],[19,2,3805],[9,8,2238],[1,16,618],[16,14,55],[17,7,6903],[12,13,1559],[2,17,3693]])
