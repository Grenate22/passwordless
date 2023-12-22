from django.urls import path
from rest_framework import routers
from . import views

router = routers.SimpleRouter()
router.register('Registration',views.RegistrationViewSet)

urlpatterns = router.urls

urlpatterns += [
    # path('verify_otp/',views.UserViewSet.as_view({'post':'verify_otp'}), name='verify-otp')
]