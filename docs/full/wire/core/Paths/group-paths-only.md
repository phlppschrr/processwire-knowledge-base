# Paths: paths-only

Source: `wire/core/Paths.php`

These properties are only useful when accessed from `$config->paths` as they are not HTTP accessible as URLs.

- $fieldTemplates: string Site field templates /site/templates/fields/
- $cache: string Site-specific cache: /site/assets/cache/
- $logs: string Site-specific logs: /site/assets/logs/
- $tmp: string Temporary files: /site/assets/tmp/
- $sessions: string Session files: /site/assets/sessions/
- $classes: string Site-specific class files: /site/classes/
