from django.contrib import admin
from .models import Bureau,Etude,Guide,Sejour,journal, Ev_Futur,Elites,Ev_Scientifique,Ev_Culturelle,Ev_Social,Ev_Sportif, CommissionScientifique,CommissionCulturelle,CommissionSociale,CommissionSportive,Celluledecom,Cellulederecolte,SecretaireGeneraux

admin.site.register(Bureau)
admin.site.register(Guide)
admin.site.register(Etude)
admin.site.register(Sejour)
admin.site.register(journal)
admin.site.register(SecretaireGeneraux)
admin.site.register(Celluledecom)
admin.site.register(Cellulederecolte)
admin.site.register(Elites)
admin.site.register(Ev_Futur)
admin.site.register(Ev_Scientifique)
admin.site.register(Ev_Culturelle)
admin.site.register(Ev_Social)
admin.site.register(Ev_Sportif)
admin.site.register(CommissionScientifique)
admin.site.register(CommissionCulturelle)
admin.site.register(CommissionSociale)
admin.site.register(CommissionSportive)

class JournalAdmin(admin.ModelAdmin):
    list_display = ('titre', 'date_publication',)
    