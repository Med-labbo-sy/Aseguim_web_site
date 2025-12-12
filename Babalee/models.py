from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

class Ev_Futur(models.Model):
    titre = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    image = models.ImageField(upload_to='membres_images/')

    def __str__(self):
        return self.titre

    class Meta:
        db_table = 'Ev_Futur'
        verbose_name = "Ev_Futur"
        verbose_name_plural = "Evenements Futurs"     


class Bureau(models.Model):
    nom = models.CharField(max_length=255)
    poste = models.CharField(max_length=255)
    image = models.ImageField(upload_to='membres_images/')

    def __str__(self):
        return self.nom

    class Meta:
        db_table = 'Bureau'
        verbose_name = "Bureau"
        verbose_name_plural = "Bureau"     
        



class SecretaireGeneraux(models.Model):
    nom = models.CharField(max_length=255)
    mandat= models.CharField(max_length=255)
    image = models.ImageField(upload_to='membres_images/')

    def __str__(self):
        return self.nom

    class Meta:
        db_table = 'SecretaireGeneraux'
        verbose_name = "SecretaireGeneraux"
        verbose_name_plural = "Secretaires Generaux"     




class Elites(models.Model):
    nom = models.CharField(max_length=255)
    domaine = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    image = models.ImageField(upload_to='membres_images/')

    def __str__(self):
        return self.nom
    class Meta:
        db_table = 'Elites'
        verbose_name = "Elite"
        verbose_name_plural = "Elites"      



class CommissionScientifique(models.Model):
    nom = models.CharField(max_length=255)
    poste = models.CharField(max_length=255)
    image = models.ImageField(upload_to='membres_images/')

    def __str__(self):
        return self.nom
    class Meta:
        db_table = 'CommissionScientifique'
        verbose_name = "Commission Scientifique"
        verbose_name_plural = "Commission Scientifique"     

class Celluledecom(models.Model):
    nom = models.CharField(max_length=255)
    poste = models.CharField(max_length=255)
    image = models.ImageField(upload_to='membres_images/')

    def __str__(self):
        return self.nom
    class Meta:
        db_table = 'Celluledecom'
        verbose_name = "Cellule de com"
        verbose_name_plural = "Cellule de com"     

class Cellulederecolte(models.Model):
    nom = models.CharField(max_length=255)
    poste = models.CharField(max_length=255)
    image = models.ImageField(upload_to='membres_images/')

    def __str__(self):
        return self.nom
    class Meta:
        db_table = 'Cellulederecolte'
        verbose_name = "Cellule de recolte"
        verbose_name_plural = "Cellule de recolte"     


class CommissionCulturelle(models.Model):
    nom = models.CharField(max_length=255)
    poste = models.CharField(max_length=255)
    image = models.ImageField(upload_to='membres_images/')

    def __str__(self):
        return self.nom
    class Meta:
        db_table = 'CommissionCulturelle'
        verbose_name = "Commission Culturelle"
        verbose_name_plural = "Commission Culturelle"     

class CommissionSociale(models.Model):
    nom = models.CharField(max_length=255)
    poste = models.CharField(max_length=255)
    image = models.ImageField(upload_to='membres_images/')

    def __str__(self):
        return self.nom
    class Meta:
        db_table = 'CommissionSociale'
        verbose_name = "Commission Sociale"
        verbose_name_plural = "Commission Sociale"       

class CommissionSportive(models.Model):
    nom = models.CharField(max_length=255)
    poste = models.CharField(max_length=255)
    image = models.ImageField(upload_to='membres_images/')

    def __str__(self):
        return self.nom

    
    class Meta:
        db_table = 'CommissionSportive'
        verbose_name = "Commission Sportive"
        verbose_name_plural = "Commission Sportive"        


class Ev_Scientifique(models.Model):
    titre = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to="carousel/")

    def __str__(self):
        return self.titre

    
    class Meta:
        db_table = 'Ev_Scientifique'
        verbose_name = "Evenement Scientifique"
        verbose_name_plural = "Evenements Scientifiques"    



class Ev_Culturelle(models.Model):
    titre = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to="carousel/")

    def __str__(self):
        return self.titre

    
    class Meta:
        db_table = 'Ev_Culturelle'
        verbose_name = "Evenement Culturelle"
        verbose_name_plural = "Evenements Culturelles"    



class Ev_Social(models.Model):
    titre = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to="carousel/")

    def __str__(self):
        return self.titre

    
    class Meta:
        db_table = 'Ev_Social'
        verbose_name = "Evenement Social"
        verbose_name_plural = "Evenements Sociaux"
            


class Ev_Sportif(models.Model):
    titre = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to="carousel/")

    def __str__(self):
        return self.titre
    
        
    
    class Meta:
        db_table = 'Ev_Sportif'
        verbose_name = "Evenement Sportif"
        verbose_name_plural = "Evenements Sportifs"




class journal(models.Model):
    titre = models.CharField(max_length=200)
    contenu = RichTextUploadingField()
   # image = models.ImageField(upload_to='journal_images/', null=True, blank=True)
    date_publication = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titre

    class Meta:
        db_table = 'journal'
        verbose_name = "Journal"
        verbose_name_plural = "Journaux"     



class Guide(models.Model):
    titre = models.CharField(max_length=200)
    contenu = RichTextUploadingField()
   # image = models.ImageField(upload_to='journal_images/', null=True, blank=True)
 

    def __str__(self):
        return self.titre

    class Meta:
        db_table = 'Guide'
        verbose_name = "Guide"
        verbose_name_plural = "Guide"     



class Etude(models.Model):
    titre = models.CharField(max_length=200)
    contenu = RichTextUploadingField()
   # image = models.ImageField(upload_to='journal_images/', null=True, blank=True)
   

    def __str__(self):
        return self.titre

    class Meta:
        db_table = 'Etude'
        verbose_name = "Etude"
        verbose_name_plural = "Etudes"     


class Sejour(models.Model):
    titre = models.CharField(max_length=150)
    contenu = RichTextUploadingField()
   # image = models.ImageField(upload_to='journal_images/', null=True, blank=True)
   

    def __str__(self):
        return self.titre


    class Meta:
        db_table = 'Sejour'
        verbose_name = "Sejour"
        verbose_name_plural = "Sejour"     
