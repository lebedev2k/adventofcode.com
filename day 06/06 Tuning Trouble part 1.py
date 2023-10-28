import collections as c
def indexOfPacketStart(s: str) -> int:
    for i in range(len(s)-4):
        a = set(s[i:i+4])
        if len(a) == 4:
            return i+4

with open('input.txt') as f:
    print(indexOfPacketStart(f.read()))
    assert (indexOfPacketStart('bvwbjplbgvbhsrlpgdmjqwftvncz') == 5)
    assert (indexOfPacketStart('nppdvjthqldpwncqszvftbrmjlhg') == 6)
    assert (indexOfPacketStart('nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg') == 10)
    assert (indexOfPacketStart('zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw') == 11)
