def water_jug(a,b,s):
    jug_a = 0
    jug_b = 0
    
    print(f"Jug A = {jug_a} liters, Jug B = {jug_b} liters")
    while jug_a != s and jug_b != s:
        if jug_a == 0:
            jug_a = a
            print(f"Jug A = {jug_a}, Jug B = {jug_b}\t->Fill Jug A")
        elif jug_b < b:
            transfer = min(jug_a, b-jug_b)
            jug_a -= transfer
            jug_b += transfer
            print(f"Jug A = {jug_a}, Jug B = {jug_b}\t->Jug A to Jug B")
        else:
            jug_b = 0
            print(f"Jug A = {jug_a}, Jug B = {jug_b}\t->Empty Jug B")
    print(f"Solution found: Jug A = {jug_a}, Jug B = {jug_b}")
    return jug_a,jug_b

a = int(input("Jug A capacity: "))
b = int(input("Jug B capacity: "))
s = int(input("Target in liters: "))
water_jug(a,b,s)