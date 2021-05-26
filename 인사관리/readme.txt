__init__.py 파이썬이 디렉토리를 파이썬 패키지로 처리하도록 지시하는 빈 파일입니다.
settings.py 우리가 만든 모든 응용 프로그램 등록, 정적 파일의 위치, 데이터베이스 구성 세부 정보 등을 포함하여 모든 웹 사이트 설정이 포함되어 있습니다.
urls.py 사이트 URL-뷰 매핑을 정의합니다. 여기에는 모든 URL 매핑 코드가 포함될 수 있지만 나중에 볼 수 있듯이 일부 매핑을 특정 응용 프로그램에 위임하는 것이 더 일반적입니다.
wsgi.py 장고 응용 프로그램이 웹 서버와 통신하는 데 사용됩니다. 이를 상용구로 취급할 수 있습니다.
asgi.py 파이썬 비동기 웹 앱 및 서버가 서로 통신하는 표준입니다. ASGI는 WSGI의 비동기 후계자이며 비동기 및 동기 파이썬 앱 모두에 대한 표준을 제공합니다(WSGI는 동기 앱에 대한 표준을 제공한 반면). WSGI와 거꾸로 호환되며 여러 서버 및 응용 프로그램 프레임워크를 지원합니다.
manage.py 스크립트는 응용 프로그램을 만들고, 데이터베이스로 작업하고, 개발 웹 서버를 시작하는 데 사용됩니다.

__init__.py - Django/Python이 폴더를 파이썬 패키지로 인식하고 프로젝트의 다른 부분 내에서 해당 개체를 사용할 수 있도록 여기에 만든 빈 파일입니다.


공부하기위해 참조한 사이트

Django - views.py와 urls.py, url 매핑 규칙, 템플릿, 스태틱 파일(정적 컨텐츠), 장고 템플릿의 블락(block)
https://lar542.github.io/Django/2019-06-17-first_django_ptoject/

[Django] 장고 정리-3 (뷰 view & 장고 url)
https://ychae-leah.tistory.com/140

MS-ACCESS를 이용하여, MySQL에 테이블 업로드하기(Import 하기)
https://m.blog.naver.com/PostView.naver?blogId=rickman2&logNo=221392786855&proxyReferer=https:%2F%2Fwww.google.com%2F

Django와 MySQL 연동하기
https://hae-ong.tistory.com/25