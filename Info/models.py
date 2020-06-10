from __future__ import unicode_literals
from django.db import models


class Genome(models.Model):
    name = models.CharField(primary_key=True,max_length=50)

    def __str__(self):
        return self.name


class Residue(models.Model):
    Gene = models.ForeignKey(Genome,to_field='name',on_delete=models.CASCADE,null=True)
    Mutation = models.CharField(primary_key=True,max_length=100)

    def __str__(self):
        return self.Mutation


class result(models.Model):
     Mutation = models.ForeignKey(Residue,to_field='Mutation',on_delete=models.CASCADE)
     SDMOutcome = models.CharField(max_length=80, blank=True)
     STRUMOutcome =  models.CharField(max_length=80, blank=True)
     mCSMOutcome = models.CharField(max_length=80, blank=True)
     PredictSNPprediction = models.CharField(max_length=80, blank=True)
     MAPPprediction = models.CharField(max_length=80, blank=True)
     phDSNPprediction = models.CharField(max_length=80, blank=True)
     PolyPhen1prediction = models.CharField(max_length=80, blank=True)
     PolyPhen2prediction = models.CharField(max_length=80, blank=True)
     SIFTprediction = models.CharField(max_length=80, blank=True)
     SNAPprediction = models.CharField(max_length=80, blank=True)
     nsSNPAnalyzerprediction = models.CharField(max_length=80, blank=True)
     PANTHERprediction = models.CharField(max_length=80, blank=True)
     mut = models.CharField(max_length=80,blank=True)

     def __str__(self):
         return self.mut
