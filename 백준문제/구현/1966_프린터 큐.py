# 중요도가 높은 문서가 하나라도 있다면, 문서를 queue의 가장 뒤에 재배치해야하고, 그렇지 않다면
# queue의 가장 앞의 문서를 인쇄(pop)해야 하므로, 리스트의 맨 앞의 원소를 삭제하는데 O(N)의 시간이 걸린다.
#
#
for _ in range(int(input())):
    num_of_documents, target_document = map(int, input().split())
    document_list = list(map(int, input().split()))
