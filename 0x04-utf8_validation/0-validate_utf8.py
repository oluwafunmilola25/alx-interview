def validUTF8(data):
    n_bytes == 0
    
    check1 = 1 << 7
    check2 = 1 << 6
    for num in data:
        byte = num & 0xFF
        
        if n-bytes == 0:
            
            check = 1 << 7
            while check & byte:
                n_bytes += 1
                check >>= 1
                
                if n_bytes == 0: #check 1bytes character
                    continue
                
                if n_bytes == 1 or n_bytes > 4:
                    return False
                else:
                    if not (byte & check1 and not (byte & chec2)):
                        return False
                    
                    n_bytes -= 1
                    
                    return n_bytes == 0