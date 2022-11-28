"""
    야매로 구현하는 Linked List
"""

MX = 1000005
dat = [-1] * MX
pre = [-1] * MX
nxt = [-1] * MX
unused = 1


def insert(addr, num):
    dat[unused] = num
    pre[unused] = addr
    nxt[unused] = nxt[addr]

    if nxt[addr] != -1:
        pre[nxt[unused]] = unused
    nxt[addr] = unused

    unused += 1


def erase(addr):
    if nxt[unused] != -1:
        pre[nxt[unused]] = pre[unused]
    if pre[unused] != -1:
        nxt[pre[unused]] = nxt[unused]
    dat[unused] = None
    pre[unused] = None
    nxt[unused] = None


def traverse():

    return


def insert_test():

    return


def erase_test():

    return
