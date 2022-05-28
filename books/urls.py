from django.db import router
from rest_framework.routers import DefaultRouter
from .views import BookViewSet, BookItemViewSet, AuthorViewSet

router = DefaultRouter()
router.register("bookitem", BookItemViewSet)
router.register("book", BookViewSet)
router.register("author", AuthorViewSet)

urlpatterns = router.urls
