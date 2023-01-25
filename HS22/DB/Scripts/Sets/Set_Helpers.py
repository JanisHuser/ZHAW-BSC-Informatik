
def remove_duplicates(rows: list):
    '''
    Removes duplicate rows
    '''
    setified = []
    
    for row in rows:
        if row not in setified:
            setified.append(row)
            
    return setified