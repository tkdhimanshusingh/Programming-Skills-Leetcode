class Solution:
    def interpret(self, command: str) -> str:
        d = {"(al)":"al", "()":"o","G":"G"}
        temp= ""
        ans=""
        for i in range(len(command)):
            temp+=command[i]
            if(temp in d):
                ans+=d[temp]
                temp=""
        return ans