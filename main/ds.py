import random as rd

class txn:
        
        proof = []
        proof_value = 0
        count = 0
        becounted = False

        def __init__(self, index):
            self.proof_value = index
            self.proof = []
            self.count = 0
            self.becounted = False


#class TXN:

#    def __init__(slef, N):
#       slef.txn = 


class value:

        owner = []
        proof = []
        ownproof = []
        def __init__(self, ori_node):
            self.owner = ori_node
            self.proof = []
            self.ownproof = []
        
        def change_own(self, new_node):
            self.owner = new_node

        def add_proof(self, newproof):
            self.proof.append(newproof)
    
        def add_ownproof(self,newproof):
            self.ownproof.append(newproof)
        
        #def change_ownproof(self,newproof):
         #   self.ownproof.


class Node:

    nodes = []
    S = []
    N = 0

    def __init__(self, N, M):
        self.N = N
        self.nodes = [[] for _ in range(N)]
        for i in range(N):
            #for j in range(M):
            #    self.nodes[i].append(value())
            self.nodes[i] = [value([i,j]) for j in range(M)]
        self.S = []
        
    def changeS(self, S_):
        self.S = [S_] * self.N
    #def trade(self, i, j, k):
     #   for _ in self.nodes[i]:


def Trade(node_a, node_b, trade_index, TXS, BCOT_):

    if len(node_a) == 0:
        return False

    tx_this = txn(trade_index)
    max_temp = 0
    temp_index = []
    #print(id(node_b))
    #print(id(node_b[1]))
    for _ in range(len(node_a)):
        if len(node_a[_].proof) == max_temp:
            temp_index.append(_)
        elif len(node_a[_].proof) > max_temp:
            max_temp = len(node_a[_].proof)
            temp_index.clear()
            temp_index.append(_)

    choice = rd.choice(temp_index)
    node_b.append(node_a[choice])
    node_b[-1].add_proof(trade_index)
    #print(node_b[-1].proof,'x')
    node_b[-1].ownproof.clear()
    node_b[-1].add_ownproof(trade_index)

    if len(node_a[choice].proof) == len(node_a[choice].ownproof):
        tx_this.proof = node_a[choice].proof[:]
        #print('eee')

    TXS.append(tx_this)
    #print(len(node_b))
    BCOT = 0
    print(node_b[-1].proof)
    
    for _ in node_b[-1].proof:
        TXS[_].count += 2
        BCOT += 2
    #print(BCOT)
    #print(len(TXS))
    BCOT_.append(BCOT)
    #with open('./BCOT.txt','w') as f:
    #    f.write(str(BCOT)+'\t')

    del node_a[choice]
    def update(value):
        value.proof.append(trade_index)
        value.ownproof.append(trade_index)
    map(update,node_a)
    return True



