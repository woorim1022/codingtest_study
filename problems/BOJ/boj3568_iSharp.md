# boj3568 iSharp

주어진 입력에서 공백과 ',', ';'를 제거하고 리스트에 담는다

변수명과 붙어있는 추가적인 변수형은 뒤집어서 따로 저장해 놓는다

이때, '[' 나 ']' 가 나올 경우에는 순서를 바꿔서 저장해준다

​	처음엔 stack을 사용하려했는데 원소가 두개 뿐이라 굳이 사용할 필요 없는것같음

주어진 조건에 맞게 출력한다

##### 실수한것

변수명이 꼭 한글자가 아니라는 것을 간과했다. 'abc' 와 같이 길이가 1 이상인 변수명을 처리할 수 있게 코드를 수정했다.

짧은 코드로 구현할 수 있을것 같은데 코드가 불필요하게 긴 느낌이다. 길이 줄여서 다시 구현해봐야겠다