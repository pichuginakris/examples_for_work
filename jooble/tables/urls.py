from django.urls import path
from .views import JoobleIndiaView, JooblePhilippinesView, JoobleAustraliaView, JoobleCanadaView, \
    JoobleIrelandView, JoobleMalaysiaView, JoobleNewZealandView, JoobleNigeriaView, JooblePakistanView, \
    JoobleSingaporeView, JoobleUSAView, JoobleUnitedKingdomView, JoobleSouthAfricaView


app_name = "tables"
# app_name will help us do a reverse look-up latter.
urlpatterns = [
    path('india', JoobleIndiaView.as_view()),
    path('india/<int:pk>', JoobleIndiaView.as_view()),
    path('philippines', JooblePhilippinesView.as_view()),
    path('philippines/<int:pk>', JooblePhilippinesView.as_view()),
    path('australia', JoobleAustraliaView.as_view()),
    path('australia/<int:pk>', JoobleAustraliaView.as_view()),
    path('canada', JoobleCanadaView.as_view()),
    path('canada/<int:pk>', JoobleCanadaView.as_view()),
    path('ireland', JoobleIrelandView.as_view()),
    path('ireland/<int:pk>', JoobleIrelandView.as_view()),
    path('malaysia', JoobleMalaysiaView.as_view()),
    path('malaysia/<int:pk>', JoobleMalaysiaView.as_view()),
    path('new_zealand', JoobleNewZealandView.as_view()),
    path('new_zealand/<int:pk>', JoobleNewZealandView.as_view()),
    path('nigeria', JoobleNigeriaView.as_view()),
    path('nigeria/<int:pk>', JoobleNigeriaView.as_view()),
    path('pakistan', JooblePakistanView.as_view()),
    path('pakistan/<int:pk>', JooblePakistanView.as_view()),
    path('singapore', JoobleSingaporeView.as_view()),
    path('singapore/<int:pk>', JoobleSingaporeView.as_view()),
    path('usa', JoobleUSAView.as_view()),
    path('usa/<int:pk>', JoobleUSAView.as_view()),
    path('uk', JoobleUnitedKingdomView.as_view()),
    path('uk/<int:pk>', JoobleUnitedKingdomView.as_view()),
    path('south_africa', JoobleSouthAfricaView.as_view()),
    path('south_africa/<int:pk>', JoobleSouthAfricaView.as_view()),
]
