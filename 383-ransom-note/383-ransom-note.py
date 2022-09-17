class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        #iterate the unqiue letter in ransom note
        for i in set(ransomNote):

            #check if the letter count in magazine is less than ransom note
            if magazine.count(i) < ransomNote.count(i):
                return(False)
        
        return(True)