if __name__ == "__main__":
    N, M = map(int, input().split())

def size(N,M):
    block = ".|."
    max_block = 0
    
    #top triangle
    for row_block in range(1,M//3,2):
        print((block*row_block).center(M,"-"))
        max_block = row_block
    
    #welcome
    print("WELCOME".center(M,"-"))
    
    #bottom triangle
    for row_block in range(max_block,-1,-2):
        print((block*row_block).center(M,"-")) 
          
size(N,M)
