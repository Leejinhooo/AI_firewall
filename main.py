def main():
    print("Hello from py-practice!")


if __name__ == "__main__":
    main()

data = [1,2,3,]
a,b,c = data
print(a,b,c)

data = [10,20,30,]
x,y,z = data
print(x,y,z)

def add(x,y,z):
    return x+y+z
args = [1,2,3]
print(add(*args))
kargs = {'x':4, 'y':5, 'z':6}
print(add(**kargs)) #출력 : 15

info = { 'name': 'Alice', 'age':30}
a,b = info
print(a,b)

for key, value in info.items():
    print(key,value)

#다중 대입 / 값 교환
a, b = 1,2
print(a,b)
a, b = b, a
print(a, b) #출력: 2 1


# *을 이용한 가변 언패킹
numbers = [1,2,3,4,5]
a, *b = numbers
print(a)   #출력 : 1
print(b)   #출력 : [2,3,4,5]
*a, b = numbers
print(a)   #출력 : [1,2,3,4]
print(b)   #출력 : 5

a, *b, c = numbers
print(a) #출력 : 1
print(b) #출력 : [2,3,4]
print(c) #출력 : 5

#기존 방식 ( 딕셔너리 병합)
d1 = { 'a': 1, 'b': 2 }
d2 = { 'c': 3, 'd': 4 }

n = len(data)
if 10 < n:
    print(f"데이터가 너므 큽니다 ({n}개)")

if (n:= len(data))>10:
    print(f"데이터가 너무 큽니다 ({n}개)")

class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def greet(self):
        print(f"안녕하세요. 저는 {self.name}이고, 나이는 {self.age}살입니다.")
person1 = person("철수", 30)
person1.greet()

class Stack[T]:
    def __init__(self) -> None:
        self.items =list[T]  = []
    def push(self, item: T) -> None:
        self.items.append(item)
    def pop(self) -> T:
        return self.items.pop()

#데코레이터
import time
def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__}실행시간 : {end - start:.4f}초")
        return result
    return wrapper
@timer
def compute():
    return sum(range(1000000))
compute()

#이터레이터
py_list = [1,2,3,4,5]
list_iter = iter(py_list)
for item in py_list:
    print(item)

#제너레이터
def fiv():
    a, b = 0,1
    while True:
        yield a
        a, b = b, a+b
fibonaci = fiv()
for i in range(10):
    print(next(fibonaci), end = " ")
    
#제너레이터 표현식 : 0부터 9까지 제곱수 출력
squares =( x**2 for x in range(10))
for square in squares:
    print(square, end=" ")

def describe(shape):
    match shape:
        case ("circle", r):
            return f"원: 반지름 {r}"
        case ("square", s):
            return f"정사각형: 한 변의 길이 {s}"
        case ("rectangle", w, h):
            return f"직사각형: 넓이 {w}, 높이 {h}"
        case _:
            return "알 수 없는 형태"
print(describe(("rectangle", 3, 8)))