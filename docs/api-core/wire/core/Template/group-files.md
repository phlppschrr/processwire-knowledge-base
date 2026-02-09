# Template: files

Source: `wire/core/Template.php`

- [`$filename: string`](method-filename.md) Template filename, including path (this is auto-generated from the name, though you may modify it at runtime if it suits your need).
- `$altFilename: string` Alternate filename for template file, if not based on template name.
- `$contentType: string` Content-type header or index (extension) of content type header from `$config->contentTypes`
- `$noPrependTemplateFile: int|bool` Disable automatic prepend of `$config->prependTemplateFile` (if in use).
- `$noAppendTemplateFile: int|bool` Disabe automatic append of `$config->appendTemplateFile` (if in use).
- `$prependFile: string` File to prepend to template file (separate from `$config->prependTemplateFile`).
- `$appendFile: string` File to append to template file (separate from `$config->appendTemplateFile`).
- `$pagefileSecure: int` Use secure pagefiles for pages using this template? 0=No/not set, 1=Yes (for non-public pages), 2=Always (3.0.166+)
