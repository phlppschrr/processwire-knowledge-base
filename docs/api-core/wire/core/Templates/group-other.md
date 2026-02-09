# Templates: other

Source: `wire/core/Templates.php`

- [`save(Template $template): bool`](method-___save.md) Save the given Template.
- [`delete(): bool`](method-___delete.md) delete(Template $template) Delete the given Template. Note that this will throw a fatal error if the template is in use by any pages.
- [`getExportData(Template $template): array`](method-___getexportdata.md) Export Template data for external use.
- [`setImportData(Template $template, array $data): array`](method-___setimportdata.md) Given an array of Template export data, import it to the given Template.
- [`fileModified(Template $template): void`](method-___filemodified.md) Hook called when a template detects that its file has been modified.
- [`getTags($getTemplateNames = false): array`](method-___gettags.md) Get tags for all templates (3.0.179+)
