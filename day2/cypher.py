import sys

if (sys.argv[1] == "cypher"):
    mode = "cypher"
elif (sys.argv[1] == "decypher"):
    mode = "decypher"
else:
    print(f"commande non supportee: {sys.argv[1]}")
    sys.exit(0)
key = sys.argv[2]
msg = sys.argv[3]

first_char = msg[0]


i = 0
msg_ord = []
for i in range(len(msg)):
    if (mode == "cypher")
        msg_ord.append(ord(msg[i]) + key)
    i = i+1
print(ord(first_char))
print(msg_ord)