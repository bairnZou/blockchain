import sys
import random as rd
import ds
import os
#import numpy as np


def main():
    argvs = sys.argv
    if len(argvs) < 6:
        sys.exit(0)

    N = int(sys.argv[1])
    NumofV = int(sys.argv[2])
    m = int(sys.argv[3])
    TPS = int(sys.argv[4])
    T = int(sys.argv[5]) 
    
    nodes_ = ds.Node(N, NumofV)
    #print(nodes.nodes[1][0].owner)
    TXS = []
    #BCOT = 0

    time = 0
    check_point = 0
    trade_index = 0

    if not os.path.exists('./BCOT.txt'):
        os.mknod('./BCOT.txt')
        
    while True:
        for _ in range(TPS):
            trade_num = rd.sample(range(N),2)
            trade_flag = True
            trade_flag = ds.Trade(nodes_.nodes[trade_num[0]],nodes_.nodes[trade_num[1]],trade_index,TXS)
            
            if trade_flag:
                trade_index += 1
            
            time += 1
        
        if time >= T:

            for i in range(len(nodes_.nodes)):
                for value in nodes_.nodes[i]:
                    value.proof.clear()
                    value.proof = value.ownproof[:]
            
            for _ in range(len(TXS)-check_point):
                TXS[_].count += m
                TXS[_].becounted = True
                if TXS[_].proof:
                    for t in TXS[_].proof:
                          

                
    

if __name__ == '__main__':
    main()