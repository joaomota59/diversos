for i in range(int(input())):
  a=bin(int(input())).replace("0b","")
  k=[str(x) for x in a.split("0")]
  print(len(str(max(k))))
