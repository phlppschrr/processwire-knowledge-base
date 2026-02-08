# Config: modules

Source: `wire/core/Config.php`

@property array $pageList Settings specific to Page lists.

@property array $pageEdit Settings specific to Page editors.

@property array $pageAdd Settings specific to Page adding.

@property string $moduleServiceURL URL where the modules web service can be accessed

@property string $moduleServiceKey API key for modules web service

@property bool $moduleCompile Allow use of compiled modules?

@property array $moduleInstall Admin module install options you allow.

@property array $substituteModules Associative array with names of substitute modules for when requested module doesn't exist

@property array $markupQA Optional settings for MarkupQA class used by FieldtypeTextarea module.
