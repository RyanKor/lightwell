## How to deploy
기술 stack: Python django

```shell
# install django
$ pip3 install django

# deploy at the root path of the project (with manage.py)
$ pm2 start "python3 manage.py runserver 서브도메인포트" --name "서브도메인"
```

## html 파일 변경 방법
* homepage > templates 폴더에서 해당 경로에 해당하는 html파일 변경
* lightwell > urls.py 에서 html의 경로 설정

## static
css, fonts, imgs, pdf 파일 보관