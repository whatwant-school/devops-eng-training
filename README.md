[![Deploy and Test](https://github.com/whatwant-school/devops-eng-training/actions/workflows/github-actions.yml/badge.svg)](https://github.com/whatwant-school/devops-eng-training/actions/workflows/github-actions.yml)

# devops-eng-training
해당 프로젝트는 모두의연구소 풀잎스쿨 MLOps 스터디에서 진행한 DevOps 실습입니다.
Flask를 사용하여 웹서버를 구현하였으며, GET Method를 통해 사칙 연산 및 기타 연산을 할 수 있습니다.
unittest/functions_test.py에서는 사칙연산 함수를 테스트 해볼 수 있고, integration/app_test.pt에서는 웹서버의 상태를 확인할 수 있습니다.

## Install

- git clone
```shell
git clone https://github.com/scy6500/devops-eng-training.git
```
- 패키지 설치
```shell
pip install -r requirements.txt
```
- 웹서버 실행  
```shell
python app.py
```

## Usage

- 덧셈
```shell
curl -X GET 'http://localhost:5000/add?num1=10&num2=2'
```
- 뺄셈
```shell
curl -X GET 'http://localhost:5000/subtract?num1=10&num2=2'
```
- 곱셈
```shell
curl -X GET 'http://localhost:5000/multiply?num1=10&num2=2'
```
- 나누셈
```shell
curl -X GET 'http://localhost:5000/division?num1=10&num2=2'
```
- 제곱근
```shell
curl -X GET 'http://localhost:5000/sqrt?num1=9'
```

## Test

- 사칙연산 함수 테스트
```shell
cd devops-eng-training/unittest
pytest
```
- 서버 상태 테스트
```shell
cd devops-eng-training/integration
pytest
```
