# -*- coding:utf-8 -*-



class TextOperate():
    
    def edit_distance(self,s1,s2):
        '''
        求取s1与s2的编辑距离
        
        '''
        m,n = len(s1),len(s2)
        dp = [[0 for j in range(n+1)] for i in range(m+1)]
        for i in range(m+1):
            for j in range(n+1):
                if i == 0:
                    dp[i][j] = j
                elif j == 0:
                    dp[i][j] = i
                elif s1[i-1] ==s2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i][j-1],dp[i-1][j],dp[i-1][j-1]) + 1
        return dp[-1][-1]
    def edit_distance_v1(self,s1,s2):
        '''
        求取s1与s2的编辑距离，优化内存版
        '''
        m=len(s1)
        n=len(s2)
        dp=list(range(n+1))
        for i in range(m):
            lu=dp[0]
            dp[0]=i+1
            for j in range(n):
                dp[j+1],lu=min(dp[j]+1,dp[j+1]+1,lu+int(s1[i]!=s2[j])),dp[j+1]
        return dp[-1]
    
    def lower(self,words_str):
        '''
        将字符串小写化
        '''
        if isinstance(words_str,str):
            return words_str.lower()
        else:
            raise ValueError('输入的类型不是字符串，请查看原因')
