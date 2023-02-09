import torch

# 오차랑 기울기 알려줌 , x=10부터 , ,반복적으로 값찾기

# 값이 10.0인 스칼라 초기값 정의
w =  torch.tensor(10.0, requires_grad=True)

# 수식정의
a  = w*w - (2*w) + 3 # x^2 - 2x + 3
print(a)
