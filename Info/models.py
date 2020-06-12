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
    SDM_Outcome = models.CharField(max_length=80, blank=True)
    STRUM_Outcome = models.CharField(max_length=80, blank=True)
    mCSM_Outcome = models.CharField(max_length=80, blank=True)
    PredictSNP_prediction = models.CharField(max_length=80, blank=True)
    MAPP_prediction = models.CharField(max_length=80, blank=True)
    phDSNP_prediction = models.CharField(max_length=80, blank=True)
    PolyPhen1_prediction = models.CharField(max_length=80, blank=True)
    PolyPhen2_prediction = models.CharField(max_length=80, blank=True)
    SIFT_prediction = models.CharField(max_length=80, blank=True)
    SNAP_prediction = models.CharField(max_length=80, blank=True)
    nsSNPAnalyzer_prediction = models.CharField(max_length=80, blank=True)
    PANTHER_prediction = models.CharField(max_length=80, blank=True)

