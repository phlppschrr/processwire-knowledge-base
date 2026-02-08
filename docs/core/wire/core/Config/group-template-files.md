# Config: template-files

Source: `wire/core/Config.php`

@property string $templateExtension Default is 'php'

@property array $contentTypes Array of extensions and the associated MIME type for each (for template file output).

@property string $prependTemplateFile PHP file in /site/templates/ that will be loaded before each page's template file (default=none)

@property string $appendTemplateFile PHP file in /site/templates/ that will be loaded after each page's template file (default=none)

@property bool $templateCompile Allow use of compiled templates?

@property string $ignoreTemplateFileRegex Regular expression to ignore template files
