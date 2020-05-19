# 프로젝트 구조 

```tree
./kafkaBackend/
├── __init__.py
├── db.sqlite3
├── kafkaBackend
│  ├── __pycache__
│  ├── asgi.py
│  ├── settings.py # 파이썬 설정 파일
│  ├── urls.py # 전역 URL 매핑 
│  └── wsgi.py
├── manage.py
├── scripts	# api Test용도 shell
│  ├── createTest.sh
│  └── getTest.sh
└── strimziBackend # kafka Backend용 app
  ├── __init__.py
  ├── __pycache__
  ├── admin.py
  ├── apps.py
  ├── controller.py # controller for kafka class and URL
  ├── kafkaClass.py # kafka class 구현체
  ├── migrations
  ├── models.py
  ├── test_class.py # kafka unit test
  ├── tests.py
  ├── urls.py # kafka app URL 매핑
  └── views.py
```

# 참조

kubernetes python client github: https://github.com/kubernetes-client/python

python client api: https://github.com/kubernetes-client/python/blob/master/kubernetes/README.md