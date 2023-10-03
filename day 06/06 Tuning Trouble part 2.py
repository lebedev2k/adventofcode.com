import collections as c
def indexOfMessageStart(s: str) -> int:
    for i in range(len(s)-14):
        a = set(s[i:i+14])
        if len(a) == 14:
            return i+14

with open('input.txt') as f:
    print(indexOfMessageStart(f.read()))
    assert (indexOfMessageStart('mjqjpqmgbljsphdztnvjfqwrcgsmlb') == 19)
    assert (indexOfMessageStart('bvwbjplbgvbhsrlpgdmjqwftvncz') == 23)
    assert (indexOfMessageStart('nppdvjthqldpwncqszvftbrmjlhg') == 23)
    assert (indexOfMessageStart('nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg') == 29)
    assert (indexOfMessageStart('zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw') == 26)
