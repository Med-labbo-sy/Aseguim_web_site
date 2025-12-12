from django.urls import path
from .import views

urlpatterns = [
    path('', views.accueil, name='accueil'),
    path('Apropos/', views.Apropos, name='Apropos'),
    path('Contact/', views.Contact, name='Contact'),
    path('autres/', views.autres, name='autres'),
    path('Bureau/Bureau', views.Membres_du_Bureau, name='Membres_du_Bureau'),
    path('Bureau/Ancien', views.AncienSG, name='AncienSG'),
    path('Bureau/Elites', views.Nos_Elites, name='Nos_Elites'),
    path('Commissions/Com', views.Cellule_de_Com, name='Cellule_de_Com'),
    path('Commissions/Recolte', views.Cellule_de_Recolte, name='Cellule_de_Recolte'),
    path('Commissions/Scientifique', views.Commission_Scientifique, name='Commission_Scientifique'),
    path('Commissions/Culturelle', views.Commission_Culturelle, name='Commission_Culturelle'),
    path('Commissions/Sociales', views.Commission_Sociale, name='Commission_Sociale'),
    path('Commissions/Sportive', views.Commission_Sportive, name='Commission_Sportive'),
    path('evenements/Futur', views.Evenement_Futur, name='Evenement_Futur'),
    path('evenements/ev', views.liste_ev, name='liste_ev'),
    path('evenements/Scientifique', views.Evenement_Scientifique, name='Evenement_Scientifique'),
    path('evenements/Culturelle', views.Evenement_Culturelle, name='Evenement_Culturelle'),
    path('evenements/Social', views.Evenement_Social, name='Evenement_Social'),
    path('evenements/Sportif', views.Evenement_Sportif, name='Evenement_Sportif'),
    path('journal/', views.journal_list, name='journal_list'),
    path('journal/<int:id>/', views.journal_detail, name='journal_detail'),
    path('Guide/', views.Guide_maroc, name='Guide_maroc'),
    path('Etude/', views.Etude_maroc, name='Etude_maroc'),
    path('Sejour/', views.Sejour_maroc, name='Sejour_maroc'),

]
