from django.urls import path
from rest_framework import routers
from . import views

router = routers.SimpleRouter()
router.register('registration',views.RegistrationViewSet)
router.register('profile',views.ProfileViewSet,basename="profile")
router.register('',views.UserViewSet)


urlpatterns = router.urls

urlpatterns += [
    # path('verify_otp/',views.UserViewSet.as_view({'post':'verify_otp'}), name='verify-otp')
]