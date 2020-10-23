from django.conf.urls import url
from django.contrib.admin import ModelAdmin as DjangoModelAdmin
from django.core.exceptions import ImproperlyConfigured
from django.utils.http import urlencode
from django.utils.translation import gettext_lazy as _
from import_export.admin import ExportMixin
from wagtail.contrib.modeladmin.helpers import ButtonHelper


class ExporterDummySite:
    name = None

    def each_context(self, request):
        return {}


class WMAExporter(ExportMixin, DjangoModelAdmin):
    export_template_name = 'wma_export/export.html'

    def __init__(self, wagtail_model_admin):
        self.wagtail_model_admin = wagtail_model_admin
        super().__init__(wagtail_model_admin.model, ExporterDummySite())

    def get_export_queryset(self, request):
        index_view = self.wagtail_model_admin.index_view_class(
            model_admin=self.wagtail_model_admin
        )
        index_view.dispatch(request)
        return index_view.get_queryset(request)


class ExportButtonHelper(ButtonHelper):
    export_button_classnames = ['bicolor', 'icon', 'icon-download']

    def export_button(self, classnames_add=None, classnames_exclude=None):
        if classnames_add is None:
            classnames_add = []
        if classnames_exclude is None:
            classnames_exclude = []
        classnames = self.export_button_classnames + classnames_add
        cn = self.finalise_classname(classnames, classnames_exclude)
        return {
            'url': self.url_helper.get_action_url("export") + '?' + urlencode(self.view.params),
            'label': _('Export'),
            'classname': cn,
            'title': _('Export these %s') % self.verbose_name_plural,
        }


class WMAExportMixin:
    button_helper_class = ExportButtonHelper
    exporter_class = None

    def get_admin_urls_for_registration(self):
        return super().get_admin_urls_for_registration() + (
            url(self.url_helper._get_action_url_pattern("export"),
                self.export_view,
                name=self.url_helper.get_action_url_name("export")),
        )

    def export_view(self, request):
        if self.exporter_class is None:
            raise ImproperlyConfigured(f"{self.__class__.__name__}.exporter_class not set!")
        exporter = self.exporter_class(self)
        return exporter.export_action(request)
