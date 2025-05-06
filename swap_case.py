def swap_case(s):
    ans =""
    for char in s:
        if char.islower():
            ans = ans + char.upper()
        else:    
            ans = ans + char.lower()
    return ans