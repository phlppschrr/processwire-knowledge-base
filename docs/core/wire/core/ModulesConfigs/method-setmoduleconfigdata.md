# $modulesConfigs->setModuleConfigData(Module $module, $data = null, $extraData = null): bool

Source: `wire/core/ModulesConfigs.php`

Populate configuration data to a ConfigurableModule

If the Module has a 'setConfigData' method, it will send the array of data to that.
Otherwise it will populate the properties individually.

## Arguments

- Module $module
- array|null $data Configuration data [key=value], or omit/null if you want it to retrieve the config data for you.
- array|null $extraData Additional runtime configuration data to merge (default=null) 3.0.169+

## Return value

bool True if configured, false if not configurable
