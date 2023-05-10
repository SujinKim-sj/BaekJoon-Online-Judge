# String
# 5052번. 전화번호 목록
# 트라이(Trie) 자료구조
# PyPy3 으로 제출해야 시간초과 안남

# 트라이에 글자를 저장하는 노드 부분
class NODE:
    def __init__(self):
        self.value = False  # 문자열의 끝 표시
        self.childs = {}    # 문자열이 연결된 트리를 만들기 위해 사용


class Trie:
    # 루트노드 생성
    def __init__(self):
        self.root = NODE()

    # 트라이 자료구조의 문자열 삽입
    def insert(self, phone_num):
        curNode = self.root     # 현재노드를 트라이의 루트노드로 설정

        # 현재 노드의 자식 중 전화번호의 글자가 없다면 현재 노드의 자식에 새로운 노드 생성
        for num in phone_num:
            if num not in curNode.childs:
                curNode.childs[num] = NODE()

            # 현재노드를 현재 노드의 자식 중 num으로 위치 시킨다
            curNode = curNode.childs[num]

            # 현재 노드가 문자열의 끝이라면 접두어와 만난 것이므로 False 반환
            if curNode.value is True:
                return False

        # 문자열의 끝 노드는 True로 표시
        curNode.value = True

        # 접두어를 만나지 못했다면 True
        return True

# 테스트 케이스의 수 입력
for _ in range(int(input().rstrip())):
    n = int(input().rstrip())       # 공백 제거를 위해 사용
    phone_List = [input().rstrip() for _ in range(n)]

    # 전화번호 목록을 길이가 짧은 것이 앞에 오도록 정렬
    phone_List.sort()
    trie = Trie()
    tof = True      # 접두어와 겹치는지 확인용
    for num in phone_List:
        tof = trie.insert(num)
        # 한 전화번호와 다른 전화번호의 접두어가 겹친다면 False
        if not tof:
            break
    if tof:
        print("YES")
    else:
        print("NO")