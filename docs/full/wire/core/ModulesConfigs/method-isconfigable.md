# $modulesConfigs->isConfigable($class, $useCache = true): bool|int|string

Source: `wire/core/ModulesConfigs.php`

Indicates whether module accepts config settings, whether interactively or API only

- Returns false if module does not accept config settings.
- Returns integer `30` if module accepts config settings but is not interactively configurable.
- Returns true, int or string if module is interactively configurable, see `Modules::isConfigurable()` return values.

## Usage

~~~~~
// basic usage
$bool = $modulesConfigs->isConfigable($class);

// usage with all arguments
$bool = $modulesConfigs->isConfigable($class, $useCache = true);
~~~~~

## Arguments

- `$class` `string|Module`
- `$useCache` (optional) `bool`

## Return value

- `bool|int|string`

## Since

3.0.179
