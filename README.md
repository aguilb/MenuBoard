https://docs.djangoproject.com/en/dev/topics/db/models

https://www.skysilk.com/blog/2017/how-to-make-a-blog-with-django/

https://openclassrooms.com/fr/courses/1871271-developpez-votre-site-web-avec-le-framework-django/1872229-les-modeles

-> django-admin startproject web_project (ou python -m django ...)

-> python manage.py runserver 0.0.0.0:8000

-> Fichier settings.py :
	- Configuration MYSQL :
		DATABASES = {
			'default': {
				'ENGINE': 'django.db.backends.mysql',   # Backends disponibles : 'postgresql', 'mysql', 'sqlite3' et 'oracle'.
				'NAME': 'web_project',             # Nom de la base de données
				'USER': '<nom d\'utilisateur>',
				'PASSWORD': '<mot de passe MySQL>',        
				'HOST': '127.0.0.1',                    # Utile si votre base de données est sur une autre machine
				'PORT': '3306',                         # ... et si elle utilise un autre port que celui par défaut
			}
		}
	- Modification à faire :
		LANGUAGE_CODE = 'fr-FR'
		TIME_ZONE = 'UTC'

-> python manage.py startapp menuboard

-> Fichier settings.py : ajouter 'menuboard'

sudo mysql -u root -p
root -> pwd "th***"
menuboard -> admin / "sat***1***"

-> python manage.py inspectdb > models.py

git pull
git commit -m ""
git push
