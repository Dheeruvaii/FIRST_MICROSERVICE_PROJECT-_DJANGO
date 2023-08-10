from django.urls import path,include
from .views import*
from rest_framework import routers


router = routers.DefaultRouter()
# router.register(r'tasks', TaskViewSet, basename='TaskViewSet')
router.register(r'users', UserViewSet, basename='UserViewSet')
# router.register(r'favproducts',FavProductsViewSet , basename='FavProductsViewSet')
router.register(r'favorite-products', FavoriteProductViewSet, basename='favorite-product')

urlpatterns = [
    path('', include(router.urls)),
    path('login/', UserLoginView.as_view()),
    # path('favproducts/', FavoriteProductViewSet.as_view()),
]   
