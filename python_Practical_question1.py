def strobogrammatic(n, length=None):
    """
    Generate all strobogrammatic numbers of length n.
    
    A strobogrammatic number looks the same when rotated 180 degrees.
    Valid pairs: (0,0), (1,1), (6,9), (8,8), (9,6)
    """
    if length is None:
        length = n
    
    if n == 0:
        return [""]
    
    if n == 1:
        return ["0", "1", "8"]
    
    # Get strobogrammatic numbers of length n-2
    middles = strobogrammatic(n - 1, length)
    result = []
    
    # Mapping of digits that look the same when rotated 180 degrees
    pairs = [("0", "0"), ("1", "1"), ("6", "9"), ("8", "8"), ("9", "6")]
    
    for middle in middles:
        for pair in pairs:
            # Don't add leading zeros for the full number
            if n != length or pair[0] != "0":
                result.append(pair[0] + middle + pair[1])
    
    return result


# Test cases
if __name__ == "__main__":
    print("n = 2:")
    print(strobogrammatic(2))
    
    print("\nn = 3:")
    print(strobogrammatic(3))
    
    print("\nn = 1:")
    print(strobogrammatic(1))