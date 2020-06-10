# Generated by Django 3.0.6 on 2020-06-10 08:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Info', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='result',
            old_name='MAPPprediction',
            new_name='MAPP_prediction',
        ),
        migrations.RenameField(
            model_name='result',
            old_name='PANTHERprediction',
            new_name='PANTHER_prediction',
        ),
        migrations.RenameField(
            model_name='result',
            old_name='PolyPhen1prediction',
            new_name='PolyPhen1_prediction',
        ),
        migrations.RenameField(
            model_name='result',
            old_name='PolyPhen2prediction',
            new_name='PolyPhen2_prediction',
        ),
        migrations.RenameField(
            model_name='result',
            old_name='PredictSNPprediction',
            new_name='PredictSNP_prediction',
        ),
        migrations.RenameField(
            model_name='result',
            old_name='SDMOutcome',
            new_name='SDM_Outcome',
        ),
        migrations.RenameField(
            model_name='result',
            old_name='SIFTprediction',
            new_name='SIFT_prediction',
        ),
        migrations.RenameField(
            model_name='result',
            old_name='SNAPprediction',
            new_name='SNAP_prediction',
        ),
        migrations.RenameField(
            model_name='result',
            old_name='STRUMOutcome',
            new_name='STRUM_Outcome',
        ),
        migrations.RenameField(
            model_name='result',
            old_name='mCSMOutcome',
            new_name='mCSM_Outcome',
        ),
        migrations.RenameField(
            model_name='result',
            old_name='nsSNPAnalyzerprediction',
            new_name='nsSNPAnalyzer_prediction',
        ),
        migrations.RenameField(
            model_name='result',
            old_name='phDSNPprediction',
            new_name='phDSNP_prediction',
        ),
    ]
