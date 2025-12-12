from django.shortcuts import render,redirect
from django.core.paginator import Paginator
from datetime import datetime
from .models import Bureau
from .models import SecretaireGeneraux
from .models import Elites
from .models import Ev_Scientifique
from .models import Ev_Culturelle
from .models import Ev_Social
from .models import Ev_Sportif
from .models import Ev_Futur
from .models import CommissionScientifique,CommissionCulturelle,CommissionSociale,CommissionSportive,Celluledecom,Cellulederecolte,SecretaireGeneraux
from django.shortcuts import render
from django.contrib import messages
from .forms import ContactForm
#from django.core.mail import send_mail
from django.core.mail import EmailMessage

from django.shortcuts import get_object_or_404
from Babalee.models import journal,Guide,Etude,Sejour


# Accueil
def accueil(request):
    context = {
        'year': datetime.now().year,
    }
    return render(request, 'Babalee/accueil.html', context)


    # Apropos

def Apropos(request):
        return render(request, 'Babalee/Apropos.html')




def autres(request):
        return render(request, 'Babalee/autres.html')




def liste_ev(request):
        return render(request, 'evenements/ev.html')



def Membres_du_Bureau(request):
        membres_Bureau = Bureau.objects.all()[:12]  # limite à 12
        return render(request, 'Bureau/membres_du_bureau.html', {
        'membres_Bureau':  membres_Bureau
    })      

def AncienSG (request):
        membres = SecretaireGeneraux.objects.all()[:12]  # limite à 12
        return render(request, 'Bureau/Ancien.html', {
        'membres': membres
    })




def Nos_Elites(request):
        membres = Elites.objects.all()[:12]  # limite à 12
        return render(request, 'Bureau/talent.html', {
        'membres':  membres
    })  

    # Commissions

def Commission_Scientifique(request):
        membres = CommissionScientifique.objects.all()[:12]  # limite à 12
        return render(request, 'Commissions/Commission_Scientifique.html', {
        'membres':  membres
    })




def Commission_Culturelle(request):
        membres = CommissionCulturelle.objects.all()[:12]  # limite à 12
        return render(request, 'Commissions/Commission_Culturelle.html', {
        'membres': membres
    })



def Cellule_de_Com(request):
        membres = Celluledecom.objects.all()[:12]  # limite à 12
        return render(request, 'Commissions/cellule_com.html', {
        'membres': membres
    })


def Cellule_de_Recolte(request):
        membres = Cellulederecolte.objects.all()[:12]  # limite à 12
        return render(request, 'Commissions/Commission_Recolte.html', {
        'membres': membres
    })





def Commission_Sociale(request):
        membres = CommissionSociale.objects.all()[:12]  # limite à 12
        return render(request, 'Commissions/Commission_Sociale.html', {
        'membres': membres
    })




def Commission_Sportive(request):
        membres = CommissionSportive.objects.all()[:12]  # limite à 12
        return render(request, 'Commissions/Commission_Sportive.html', {
        'membres':  membres
    })




def Evenement_Futur(request):
    Ev_F = Ev_Futur.objects.all()
    return render(request, 'evenements/Evenement_Futur.html', {"Ev_F": Ev_F})
    




def Evenement_Scientifique(request):
    slides = Ev_Scientifique.objects.all()
    return render(request, 'evenements/Evenement_Scientifique.html', {"slides": slides})



def Evenement_Culturelle(request):
    slides = Ev_Culturelle.objects.all()
    return render(request, 'evenements/Evenement_Culturelle.html', {"slides": slides})



def Evenement_Social(request):
    slides = Ev_Social.objects.all()
    return render(request, 'evenements/Evenement_Social.html', {"slides": slides})


def Evenement_Sportif(request):
    slides = Ev_Sportif.objects.all()
    return render(request, 'evenements/Evenement_Sportif.html', {"slides": slides})






def Contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)

        if form.is_valid():
            nom = form.cleaned_data['nom']
            email = form.cleaned_data['email']
            objet = form.cleaned_data['objet']
            message_user = form.cleaned_data['message']

            # Construction du message
            sujet = f"Nouveau message - {objet}"

            contenu = f"""
Nom : {nom}
Email : {email}
Objet : {objet}

Message :
{message_user}
            """

            # Email sécurisé avec reply_to
            email_message = EmailMessage(
                subject=sujet,
                body=contenu,
                from_email="mamadoulabbos88@gmail.com",
                to=["mamadoulabbos88@gmail.com"],
                reply_to=[email]   # ✔ fonctionne dans EmailMessage
            )

            email_message.send()

            messages.success(request, "Votre message a été envoyé avec succès !")
            return redirect("Contact")  # éviter renvoi multiple POST

        else:
            messages.error(request, "Veuillez corriger les erreurs dans le formulaire.")
    else:
        form = ContactForm()

    return render(request, "Babalee/Contact.html", {"form": form})




def journal_list(request):
    journaux =journal.objects.all().order_by('-date_publication')
    return render(request, 'Babalee/journal_list.html', {'journaux': journaux})

def journal_detail(request, id):
    j = get_object_or_404(journal, id=id)
    return render(request, 'Babalee/journal_detail.html', {'j': j})


def Guide_maroc(request):
    guide =Guide.objects.all()
    return render(request, 'Babalee/Guide.html', {'guide': guide})


def Etude_maroc(request):
    etude =Etude.objects.all()
    return render(request, 'Babalee/Etude.html', {'etude': etude})


def Sejour_maroc(request):
    sejour =Sejour.objects.all()
    return render(request, 'Babalee/carte_sejour.html', {'sejour': sejour})