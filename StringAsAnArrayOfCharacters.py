s = 'A Python script'
print(s[0])
print(s[2])
print(s[2:8])
print(s[:8])
print(s[8:])
print(s[222:999])

message = 'Document "cv.doc" was printed on printer: XEROX'
print(message.find(':'))
print(message[message.find(':')+2:])
print(message[message.find('"')+1:])
tmp = message[message.find('"')+1:]
print(tmp[:message.find('"')-3])

# Laboratory

q = 'THE EYES'
print(q[0], q[1], q[2], q[5], q[3], q[7], q[4], q[6])
q = 'a gentleman'
print(q[3], q[6:8], q[2], q[0], q[4:6], q[1], q[8:])
