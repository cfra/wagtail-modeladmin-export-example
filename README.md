# Wagtail ModelAdmin Export Example

This example shows how [django-import-export](https://github.com/django-import-export/django-import-export)
can be integrated into the [Wagtail](https://wagtail.io/)
[ModelAdmin](https://docs.wagtail.io/en/latest/reference/contrib/modeladmin/index.html).

## Usage

Install the requirements using either:

- `poetry install`

Run Migrations:

- `poetry run ./manage.py migrate`

Create a super-user:

- `poetry run ./manage.py createsuperuser`

Run the Development server:

- `poetry run ./manage.py runserver`

Navigate to <http://127.0.0.1:8000>.

Create a few persons.

Use the export button on the top right.

???

## Design

The glue that adapts between the Django `ModelAdmin` and the Wagtail `ModelAdmin` is in
`wma_export_example.apps.wma_export`. It should be reusable for other projects.

The example app is `wma_export_example.apps.persons`. It shows how the `wma_export` app can be used
to provide a Wagtail `ModelAdmin` with export functionality.

The mixins provided by django-import-export are tailored to be used with a Django `ModelAdmin` which
has a different API than the Wagtail `ModelAdmin`.

This example internally uses a Django `ModelAdmin` mixed with the `ExportMixin` and registers its
`export_action` as a view on the Wagtail `ModelAdmin` to provide the export functionality in Wagtail.
