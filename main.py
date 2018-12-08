import pyperclip
from CreatePass import CreatePass
from SavePass import SavePass

input_ = input().split()
if len(input_) == 2 and input_[1].isdigit():
    pw = CreatePass()
    pw.set_len_pass(int(input_[1]))
    print(pw.password)
else:
    pw = CreatePass()
    pw.no_set_len_pass()
    print(pw.password)

pyperclip.copy(pw.password)

SavePass(input_[0],pw.password)