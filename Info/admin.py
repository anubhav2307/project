from __future__ import unicode_literals
from django.contrib import admin
from import_export import resources, fields
from import_export.widgets import ForeignKeyWidget
from .models import Genome,Residue,result
from import_export.admin import ImportExportActionModelAdmin, ImportExportModelAdmin


class GenomeResource(resources.ModelResource):

    class Meta:
        model = Genome
        exclude = ('id',)
        import_id_fields = ('name',)


class GenomeAdmin(ImportExportModelAdmin):
    resource_class = GenomeResource


admin.site.register(Genome,GenomeAdmin)


class ResidueResource(resources.ModelResource):

    class Meta:
        model = Residue
        exclude = ('id',)
        import_id_fields = ('Gene', 'Mutation',)


class ResidueAdmin(ImportExportModelAdmin):
    search_fields=['Mutation']
    resource_class = ResidueResource


admin.site.register(Residue,ResidueAdmin)


class resultResource(resources.ModelResource):

    class Meta:
        model = result
        exclude = ('id',)
        import_id_fields = ('Mutation', 'SDM_Outcome','STRUM_Outcome','mCSM_Outcome','PredictSNP_prediction','MAPP_prediction','phDSNP_prediction','PolyPhen1_prediction','PolyPhen2_prediction','SIFT_prediction','SNAP_prediction','nsSNPAnalyzer_prediction','PANTHER_prediction',)


class resultAdmin(ImportExportModelAdmin):
    search_fields=['Mutation__Mutation']
    resource_class = resultResource
    list_display = ['Mutation']


admin.site.register(result,resultAdmin)


 