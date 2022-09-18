class Solution(object):
    def removeComments(self, source):
       
        result = []
        current_line = ""
        in_block = False
        in_line = False
        skip_next = False
        
        for line in source:
            skip_next = False

            in_line = False
            
            for index, character in enumerate(line):
                
                if skip_next:
                    
                    skip_next = False
                    continue
                
                if in_line:
                    continue
                    
                if in_block:
                    
                    if line[index:index+2] == '*/':
           
                        in_block = False
                        skip_next = True
                        continue
                    else:
                    
                        continue
                
                if line[index:index+2] == '/*':
                    in_block = True
                    skip_next = True
                    continue
                if line[index:index+2] == '//':
                    
                    in_line = True
                    skip_next = True
                    continue
                
    
                current_line += character
            
            
            if not in_block and current_line:
                
                
                result.append(current_line)
                current_line = ""
                
        return result