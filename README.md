# OMR
OMR 리더기 클라이언트/웹서버

## 사용 라이브러리(클라이언트)
- sveltkit [https://kit.svelte.dev/]
- mongoose [https://mongoosejs.com/]
- picocss [https://picocss.com/]
- amqplib [https://amqp-node.github.io/amqplib/]

## 사용 라이브러리(WORKER)
- pymongo [https://pymongo.readthedocs.io/en/stable/]
- pika [https://pika.readthedocs.io/en/stable/]

## 서버를 띄워 보자
```bash
npm i
npm run dev
```

## 필요 파일
* .env : 환경변수 저장

## 필요한 환경변수
|변수명|용도|예시값|
|-|-|-|
|MONGODB_URL|데이터베이스 주소|mongodb://~~~~~|
|AMQP_HOST|RabbitMQ 주소|x.x.x.x|
|UPLOAD_PATH|파이썬에서 사용하는 uploads 폴더의 위치|

## 파이썬 관련 처리
### Dependency 설치
```
cd worker
python -m pip install -r requirements.txt
```

### Poppler 설치
공식 홈페이지 참조  
https://poppler.freedesktop.org

### python 실행
```
pythom worker.py
```