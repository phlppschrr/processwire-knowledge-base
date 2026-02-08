# Templates: other

Source: `wire/core/Templates.php`

@method bool save(Template $template) Save the given Template.

@method bool delete() delete(Template $template) Delete the given Template. Note that this will throw a fatal error if the template is in use by any pages.

@method array getExportData(Template $template) Export Template data for external use.

@method array setImportData(Template $template, array $data) Given an array of Template export data, import it to the given Template.

@method void fileModified(Template $template) Hook called when a template detects that its file has been modified.

@method array getTags($getTemplateNames = false) Get tags for all templates (3.0.179+)
