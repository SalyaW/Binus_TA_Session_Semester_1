u = 0
vlimit = 60
s = int(input("input distance:"))
a = float(input("insert acceleration:"))
t = int(input("input time:"))

for i in range(0,t+1):
    s2 = int(0.5 * a * i * i )
    s2 = int(s2/10)
    print("Duration:",i,"Distance:","*"* (s2))

v = t * a
if v <= 60:
    v = t * a
    print("Was not over the speed limit,max speed was",v,"m/s")
else:
    print("Over the speed limit,max speed was",v,"m/s")

s1 = 0.5 * t * t * a

if s1 >= s:
    print("they reached their destination","they reaced",s1)
else:
    print("they didn't reach their destination","they reaced",s1)
