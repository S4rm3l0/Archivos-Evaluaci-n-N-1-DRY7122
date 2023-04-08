acl = int(input("indique número de ACL: "))
if acl >= 1 and acl <= 99:
    print("Este valor corresponde a una ACL estándar")
elif acl >= 100 and acl <= 199:
    print("Este valor correpsonde a una ACL extendida")
else:
    print("Este valor no corresponde a una ACL.")