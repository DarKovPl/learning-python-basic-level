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

q = 'The morse code'
print(q[1:3].upper() + q[6].upper() + q[8].upper(),
      q[10:12].upper() + q[4].upper() + q[13:].upper(),
      q[12].upper() + q[11].upper() + q[0].upper() + q[7].upper())

line = 'Program "Kropka nad i" nadamy o: 22:00'
time = line[line.find(':')+2:]
print(time)
tmp = line[line.find('"'):]
print(tmp)
title = tmp[:14]
print(title)
