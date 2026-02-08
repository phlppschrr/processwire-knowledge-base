# $modulesConfigs->isConfigable($class, $useCache = true): bool|int|string

Source: `wire/core/ModulesConfigs.php`

Indicates whether module accepts config settings, whether interactively or API only

- Returns false if module does not accept config settings.
- Returns integer `30` if module accepts config settings but is not interactively configurable.
- Returns true, int or string if module is interactively configurable, see `Modules::isConfigurable()` return values.

## Arguments

- string|Module $class
- bool $useCache

## Return value

bool|int|string

## Meta

- @since 3.0.179
