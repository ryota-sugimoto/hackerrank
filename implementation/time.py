import sys
H = int(sys.stdin.next())
M = int(sys.stdin.next())

hours = { 1: "one",
          2: "two",
          3: "three",
          4: "four",
          5: "five",
          6: "six",
          7: "seven",
          8: "eight",
          9: "nine",
         10: "ten",
         11: "eleven",
         12: "twelve",
         13: "one"}
minutes = { 1: "one",
            2: "two",
            3: "three",
            4: "four",
            5: "five",
            6: "six",
            7: "seven",
            8: "eight",
            9: "nine",
           10: "ten",
           11: "eleven",
           12: "twelve",
           13: "thirteen",
           14: "fourteen",
           16: "sixteen",
           17: "seventeen",
           18: "eighteen",
           19: "nineteen",
           20: "twenty"}
if M == 0:
  print "%s o' clock" % (hours[H],)
elif M == 1:
  print "one minute past %s" % (hours[H],)
elif M == 15:
  print "quarter past %s" % (hours[H],)
elif M == 45:
  print "quarter to %s" % (hours[H+1],)
elif M == 59:
  print "one minute to %s" % (hours[H+1],)
elif M == 30:
  print "half past %s" % (hours[H],)
elif M <= 30:
  if M > 20:
    i = M%10
    minute = minutes[20] + " " + minutes[i] 
  else:
    minute = minutes[M]
  print "%s minutes past %s" % (minute, hours[H])
else:
  m = 60 - M
  if m > 20:
    i = M%10
    minute = minutes[20] + " " + minutes[i]
  else:
    minute = minutes[m]
  print "%s minutes to %s" % (minute, hours[H+1])
