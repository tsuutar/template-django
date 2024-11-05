# Django テンプレート

## 環境の作成

```
$ python -m venv .venv
$ .venv/Scripts/Activate.ps1
$ python.exe -m pip install --upgrade pip
$ pip install -r requirements.txt
```

## superuser 設定

```
$ python manage.py createsuperuser
```

## migrate

```
$ python manage.py migrate
```

# Django

## プロジェクト・アプリ作成

```
$ python -m django startproject config .
$ django-admin startapp app
$ django-admin startapp accounts
```

# Other

## 環境情報の保存

```
$ pip freeze > requirements.txt
```
