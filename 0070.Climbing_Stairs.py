class Solution:
    def climbStairs(self, n: int) -> int:
        count = result = 0
        for i in range(n,(n//2)+(n%2)-1,-1):
            fact_i = fact_count = fact_i_count = 1
            for j in range(1,i+1):
                fact_i = fact_i * j
            for j in range(1,count+1):
                fact_count = fact_count * j
            for j in range(1,i-count+1):
                fact_i_count = fact_i_count * j
            result += int(fact_i/(fact_count*fact_i_count))
            count+=1
        return result
      
      
# 칸 갯수 1개씩 줄어듦. 줄어든 갯수만큼 2 갯수 증가.
# 8C0 -> 7C1 -> 6C2 -> 5C3 -> 4C4 // 4C0 -> 3C1 -> 2C2
# n부터 n2로 나눈 몫+나머지 까지.

# 나는 조합(nCc)로 했는데 disscuss 보니 피보나치로 하면 더 빠르고 메모리 효율 좋음
# 내가 짠 코드는 너무 효율이 안좋다.
