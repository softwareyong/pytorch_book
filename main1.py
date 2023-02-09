# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


import torch

def print_tensor(tensor):
    print("size:", tensor.size())
    print("shape:", tensor.shape)
    print("랭크(차원):", tensor.ndimension())

x = torch.tensor([[1,2,3], [4,5,6], [7,8,9]])
print_tensor(x)
# print(x)

# print("size:", x.size())
# print("shape:", x.shape)
# print("랭크(차원):", x.ndimension())

#### 랭크 늘리기 ####
# unsqueeze(), squeeze(), view() ==> 텐서의 랭크와 shape를 인위적으로 바꿀 수 있습니다.
x = torch.unsqueeze(x, 0) # ==> 이 코드는 랭크 2 텐서의 첫번째(0번째) 자리에 1이라는 차원값을 추가해 [1,3,3]모양의 랭크 3텐서로 변경 ==> 랭크는 늘어나도 텐서속 원소의 수는 유지됩니다.
print(x)
print("size:", x.size())
print("shape:", x.shape)
print("랭크(차원):", x.ndimension())

#### 랭크 줄이기 ####
# squeeze() 함수를 이용하면 텐서의 랭크 중 크기가 1인 랭크를 삭제하여 다시 랭크 2텐서로 되돌릴 수 있다.
x = torch.squeeze(x) # x tenser의 랭크를 1줄인다.
print(x)
print("size:", x.size())
print("shape:", x.shape)
print("랭크(차원):", x.ndimension())

#### view ####
# 뷰 함수를 이용하면 이와 같은 작업을 더쉽게 가능
# 직접 텐서으 모양을 바꿀 수 있다.
# 랭크 2의 [3,3]모양인 x를 랭크 1의 [9]모양으로 바꾸기 가능
x = x.view(9)
print(x)
print("size:", x.size())
print("shape:", x.shape)
print("랭크(차원):", x.ndimension())

try:
    x = x.view(2, 4)
except Exception as e:
    print(e) # 에러 출력


# Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
