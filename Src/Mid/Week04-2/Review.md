# 4주차 오프라인 수업 정리

### 파이썬에서의 특이한 기능
- #### [ := ]

- #### [ for else 문 ]

### 파이썬 for문 에서의 in 과 range()
- #### 클래스, 객체, 인스턴스 의 차이
  - 클래스 : 클래스는 객체 또는 인스턴스의 생성하기 위한 <br>
    기본적인 틀로 사용된다
  - 객체 : 클래스의 구조를 넘겨받아 사용할수 있는 상태
  - 인스턴스 : 클래스로 만든 객체를 인스턴스라 한다. 객체와 <br>
    인스턴스는 혼용 하여 사용이 가능하지만, 구분도 가능하다. <br>
    [구분에 관한 자세한 설명(링크)](https://fastsecurity.tistory.com/38)

### 파이썬에서 int() 
- #### c와 다르게 쓰임 주의 해야함
    - str 타입의 데이터를 int 변환을 시켰을때 오류가 아닌 <br>
    사용자가 의도한 숫자형 데이터로 자동 변환해줌

### 파이썬에서 input() 
- #### int(), float(),  complex() 지정 타입
    - 지정 타입으로만 객체를 생성해서 넣어 주기 때문에 <br>
    만약 지정한 타입이 아닌 포괄하지 않는 타입을 넣어주면 <br>
    오류

- #### eval() 자유 타입
    - 자동으로 판단하여 알맞은 타입 객체로 넣어줌

### 비트 연산에서 MSB, LSB
- #### 왼쪽 MSB

- #### 오른쪽 LSB

### Shallow, Deep copy
- #### Shallow
    - 최상위 객체 주소들만 새롭게 복사함
- #### Deep
    - 최상위 뿐만 아니라 하위 객체 주소들도 복사함

## <strong>질문</strong>
1. 예시문 에서 chr 과 ord 함수를 사용해서 문자에 대한 관점으로 <br>
    설명 하셨는데, 파이썬에선 c처럼 char 타입이 따로 존제 하는것 <br>
    으로 아는데 어떻게 생각해야 하나요? <br> 
    (c에서 string또는char[], 그리고 char 타입)

2. 두가지 타입의 덧셈이 진행 되었을때, float() + int() 의 <br>
   형태라고 가정하고 우선순위?

3. 파이썬 에서 정수는 미리 주소를 할당 시켜놓고 그 객체의 주소를 <br>
    넘겨 받아 정수를 처리한다 들었는데, 메모리 관리에 있어 이것이 <br>
    효율적인 방법인가?