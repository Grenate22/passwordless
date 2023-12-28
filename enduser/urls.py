from django.urls import path
from rest_framework import routers
from . import views

router = routers.SimpleRouter()
router.register('registration',views.RegistrationViewSet)
router.register('profile',views.ProfileViewSet,basename="profile")
router.register('users',views.UserViewSet)


urlpatterns = router.urls

urlpatterns += [
    path('full_verified/',views.CustomView.as_view(), name='fully_verified')
]