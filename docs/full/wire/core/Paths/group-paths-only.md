# Paths: paths-only

Source: `wire/core/Paths.php`

These properties are only useful when accessed from `$config->paths` as they are not HTTP accessible as URLs.

@property string $fieldTemplates Site field templates /site/templates/fields/

@property string $cache Site-specific cache: /site/assets/cache/

@property string $logs Site-specific logs: /site/assets/logs/

@property string $tmp Temporary files: /site/assets/tmp/

@property string $sessions Session files: /site/assets/sessions/

@property string $classes Site-specific class files: /site/classes/
