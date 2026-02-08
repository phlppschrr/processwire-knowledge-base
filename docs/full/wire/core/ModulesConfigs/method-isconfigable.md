# ModulesConfigs::isConfigable()

Source: `wire/core/ModulesConfigs.php`

Indicates whether module accepts config settings, whether interactively or API only

- Returns false if module does not accept config settings.
- Returns integer `30` if module accepts config settings but is not interactively configurable.
- Returns true, int or string if module is interactively configurable, see `Modules::isConfigurable()` return values.

@param string|Module $class

@param bool $useCache

@return bool|int|string

@since 3.0.179
