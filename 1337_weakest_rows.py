def kWeakestRows(mat, k):
    soldiers = []
    
    for idx, platoon in enumerate(mat):
        soldiers.append((sum(platoon), idx))
    
    soldiers.sort()
    
    return [idx[1] for idx in soldiers[:k]]