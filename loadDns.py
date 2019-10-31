with open("hosts.nonencrypted") as f:
  lineList = f.readlines()

with open('c:\windows\System32\drivers\etc\hosts') as fp:
    line = fp.readline()
    cnt = 1
    while line:
        print(line, end = '')
        line = fp.readline()
        cnt += 1
        if line == "## DON'T EDIT AFTER THIS LINE":
            break
print("## DON'T EDIT AFTER THIS LINE")
with open("hosts.nonencrypted") as f:
    line = f.readline()
    print(line, end='')
