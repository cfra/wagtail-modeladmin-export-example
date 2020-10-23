from import_export.fields import Field
from import_export.resources import ModelResource
from wagtail.contrib.modeladmin.options import (
    ModelAdmin,
    modeladmin_register
)
from wma_export_example.apps.wma_export.exporter import WMAExporter, WMAExportMixin

from .models import Person


class PersonResource(ModelResource):
    class Meta:
        model = Person
        fields = ("given_name", "family_name", "date_of_birth",)


class PersonExporter(WMAExporter):
    resource = PersonResource


class PersonAdmin(WMAExportMixin, ModelAdmin):
    exporter_class = PersonExporter
    model = Person
    menu_icon = "user"
    list_display = ("given_name", "family_name", "date_of_birth",)
    search_fields = ("given_name", "family_name",)


modeladmin_register(PersonAdmin)
