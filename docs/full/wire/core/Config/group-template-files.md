# Config: template-files

Source: `wire/core/Config.php`

- $templateExtension: string Default is 'php'
- [$contentTypes: array](method-contenttypes.md) Array of extensions and the associated MIME type for each (for template file output).
- $prependTemplateFile: string PHP file in /site/templates/ that will be loaded before each page's template file (default=none)
- $appendTemplateFile: string PHP file in /site/templates/ that will be loaded after each page's template file (default=none)
- $templateCompile: bool Allow use of compiled templates?
- $ignoreTemplateFileRegex: string Regular expression to ignore template files
