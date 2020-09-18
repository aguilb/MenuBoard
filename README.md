https://docs.djangoproject.com/en/dev/topics/db/models

https://www.skysilk.com/blog/2017/how-to-make-a-blog-with-django/

https://openclassrooms.com/fr/courses/1871271-developpez-votre-site-web-avec-le-framework-django/1872229-les-modeles

-> django-admin startproject web_project (ou python -m django ...)
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

==========
-> python manage.py inspectdb > models.py

-> python manage.py runserver 0.0.0.0:8000

git pull
git commit -m ""
git push

HTML :
<div class="row row-cols-1 row-cols-sm-2 row-cols-md-3 row-cols-lg-4">
    <div class="col mb-4">
        <div class="card booking-card h-100">
            <div class="view overlay">
                <img class="card-img-top" src="https://mdbootstrap.com/img/Photos/Horizontal/Food/8-col/img (5).jpg" alt="Card image cap">
                <a href="#!">
                    <div class="mask rgba-white-slight"></div>
                </a>
            </div>
            <div class="card-body">
                <h4 class="card-title font-weight-bold"><a>{title}</a></h4>
                <ul class="list-unstyled list-inline rating dark-grey-text mb-0">
                    <li class="list-inline-item"><p class="text-muted">Alcool</p></li>
                    <li class="list-inline-item mr-0"><i class="fas fa-square"> </i></li>
                    <li class="list-inline-item mr-0"><i class="fas fa-square"></i></li>
                    <li class="list-inline-item mr-0"><i class="fas fa-square"></i></li>
                    <li class="list-inline-item mr-0"><i class="fas fa-square"></i></li>
                    <li class="list-inline-item"><i class="fal fa-square"></i>{alcohol}</li>
                </ul>
                <ul class="list-unstyled list-inline rating dark-grey-text mb-0">
                    <li class="list-inline-item"><p class="text-muted">Sucré</p></li>
                    <li class="list-inline-item mr-0"><i class="fas fa-square"> </i></li>
                    <li class="list-inline-item mr-0"><i class="fas fa-square"></i></li>
                    <li class="list-inline-item mr-0"><i class="fal fa-square"></i></li>
                    <li class="list-inline-item mr-0"><i class="fal fa-square"></i></li>
                    <li class="list-inline-item"><i class="fal fa-square"></i>{sweetness}</li>
                </ul>
                <ul class="list-unstyled list-inline rating dark-grey-text mb-0">
                    <li class="list-inline-item"><p class="text-muted">Amer</p></li>
                    <li class="list-inline-item mr-0"><i class="fas fa-square"> </i></li>
                    <li class="list-inline-item mr-0"><i class="fal fa-square"></i></li>
                    <li class="list-inline-item mr-0"><i class="fal fa-square"></i></li>
                    <li class="list-inline-item mr-0"><i class="fal fa-square"></i></li>
                    <li class="list-inline-item"><i class="fal fa-square"></i>{bitterness}</li>
                </ul>
                <p class="mb-2">{glass}</p>
                <p class="card-text">{description}Some quick example text to build on the card title and make up the bulk of the card's content.</p>
                <hr class="my-3">
                <ul class="list-unstyled list-inline d-flex my-0">
                    <li class="list-inline-item">
                        <div class="chip secondary-color white-text mb-0 mr-0">{taste}</div>
                    </li>
                    <li class="list-inline-item">
                        <div class="chip secondary-color white-text mb-0 mr-0">{taste}</div>
                    </li>
                    <li class="list-inline-item">
                        <div class="chip secondary-color white-text mb-0 mr-0">{taste}</div>
                    </li>
                </ul>
                <ul class="list-unstyled list-inline d-flex my-0">
                    <li class="list-inline-item">
                        <div class="chip {class_color} mb-0 mr-0">{alcohol}</div>
                    </li>
                    <li class="list-inline-item">
                        <div class="chip {class_color} mb-0 mr-0">{alcohol}</div>
                    </li>
                    <li class="list-inline-item">
                        <div class="chip {class_color} mb-0 mr-0">{alcohol}</div>
                    </li>
                </ul>
                <hr class="my-3">
                <div class="d-flex justify-content-between">
                    <a href="#" class="btn btn-flat deep-purple-text p-1 mx-0 mb-0">Commander</a>
                    <a href="#" class="btn btn-flat deep-purple-text p-1 mx-0 mb-0" data-toggle="modal" data-target="#ModalIngredients" data-id="{idcocktail}">Ingrédients</a>
                </div>
            </div>
        </div>
    </div>
</div>
<div class="modal fade" id="ModalIngredients" tabindex="-1" role="dialog" aria-labelledby="ModalLabel" aria-hidden="true">
    <div class="modal-dialog" role="document">
        <div class="modal-content">
            <div class="modal-header">
                <h4 class="modal-title" id="ModalLabel">Ingrédients</h4>
                <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                    <span aria-hidden="true">&times;</span>
                </button>
            </div>
            <div class="modal-body">
                <ul class="list-unstyled dark-grey-text mb-0">
                    <li><p class="text-muted"><i class="fad fa-caret-right mr-1"></i>{ingredient}</p></li>
                    <li><p class="text-muted"><i class="fad fa-caret-right mr-1"></i>{ingredient}</p></li>
                    <li><p class="text-muted"><i class="fad fa-caret-right mr-1"></i>{ingredient}</p></li>
                </ul>
                <hr class="my-3">
                <ul class="list-unstyled dark-grey-text mb-0">
                    <li><p class="text-muted"><i class="fad fa-terminal mr-1"></i>{instruction}</p></li>
                    <li><p class="text-muted"><i class="fad fa-terminal mr-1"></i>{instruction}</p></li>
                    <li><p class="text-muted"><i class="fad fa-terminal mr-1"></i>{instruction}</p></li>
                </ul>
            </div>
            <div class="modal-footer">
                <button type="button" class="btn btn-secondary" data-dismiss="modal">Fermer</button>
            </div>
        </div>
    </div>
</div>
