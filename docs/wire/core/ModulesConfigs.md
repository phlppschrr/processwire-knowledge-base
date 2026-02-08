# ModulesConfigs

Source: `wire/core/ModulesConfigs.php`

ProcessWire Modules: Configs

ProcessWire 3.x, Copyright 2023 by Ryan Cramer
https://processwire.com

## getModuleEditUrl()

Return the URL where the module can be edited, configured or uninstalled

If module is not installed, it returns URL to install the module.


@param string|Module $className

@param bool $collapseInfo

@return string

## getConfig()

Given a module name, return an associative array of configuration data for it

- Applicable only for modules that support configuration.
- Configuration data is stored encoded in the database "modules" table "data" field.

~~~~~~
// Getting, modifying and saving module config data
$data = $modules->getConfig('HelloWorld');
$data['greeting'] = 'Hello World! How are you today?';
$modules->saveConfig('HelloWorld', $data);

// Getting just one property 'apiKey' from module config data

@apiKey = $modules->getConfig('HelloWorld', 'apiKey');
~~~~~~

3.0.16 Changed from more verbose name `getModuleConfigData()`, which can still be used.

@param string|Module $class

@param string $property Optionally just get value for a specific property (omit to get all config)

@return array|string|int|float Module configuration data, returns array unless a specific $property was requested

@see Modules::saveConfig()

@since 3.0.16 Use method getModuleConfigData() with same arguments for prior versions (can also be used on any version).

## isConfigurable()

Is the given module interactively configurable?

This method can be used to simply determine if a module is configurable (yes or no), or more specifically
how it is configurable.

~~~~~
// Determine IF a module is configurable
if($modules->isConfigurable('HelloWorld')) {
  // Module is configurable
} else {
  // Module is NOT configurable
}
~~~~~
~~~~~
// Determine HOW a module is configurable
$configurable = $module->isConfigurable('HelloWorld');
if($configurable === true) {
  // configurable in a way compatible with all past versions of ProcessWire
} else if(is_string($configurable)) {
  // configurable via an external configuration file
  // file is identifed in $configurable variable
} else if(is_int($configurable)) {
  // configurable via a method in the class
  // the $configurable variable contains a number with specifics
} else {
  // module is NOT configurable
}
~~~~~

### Return value details

#### If module is configurable via external configuration file:

- Returns string of full path/filename to `ModuleName.config.php` file

#### If module is configurable because it implements a configurable module interface:

- Returns boolean `true` if module is configurable via the static `getModuleConfigInputfields()` method.
  This particular method is compatible with all past versions of ProcessWire.
- Returns integer `2` if module is configurable via the non-static `getModuleConfigInputfields()` and requires no arguments.
- Returns integer `3` if module is configurable via the non-static `getModuleConfigInputfields()` and requires `$data` array.
- Returns integer `4` if module is configurable via the non-static `getModuleConfigInputfields()` and requires `InputfieldWrapper` argument.
- Returns integer `19` if module is configurable via non-static `getModuleConfigArray()` method.
- Returns integer `20` if module is configurable via static `getModuleConfigArray()` method.

#### If module is not configurable:

- Returns boolean `false` if not configurable

*This method is named isConfigurableModule() in ProcessWire versions prior to to 3.0.16.*


@param Module|string $class Module name

@param bool $useCache Use caching? This accepts a few options:
	- Specify boolean `true` to allow use of cache when available (default behavior).
	- Specify boolean `false` to disable retrieval of this property from getModuleInfo (forces a new check).
	- Specify string `interface` to check only if module implements ConfigurableModule interface.
	- Specify string `file` to check only if module has a separate configuration class/file.

@return bool|string|int See details about return values in method description.

@since 3.0.16

@todo this method has two distinct parts (file and interface) that need to be split in two methods.

## isConfigable()

Indicates whether module accepts config settings, whether interactively or API only

- Returns false if module does not accept config settings.
- Returns integer `30` if module accepts config settings but is not interactively configurable.
- Returns true, int or string if module is interactively configurable, see `Modules::isConfigurable()` return values.

@param string|Module $class

@param bool $useCache

@return bool|int|string

@since 3.0.179

## setModuleConfigData()

Populate configuration data to a ConfigurableModule

If the Module has a 'setConfigData' method, it will send the array of data to that.
Otherwise it will populate the properties individually.

@param Module $module

@param array|null $data Configuration data [key=value], or omit/null if you want it to retrieve the config data for you.

@param array|null $extraData Additional runtime configuration data to merge (default=null) 3.0.169+

@return bool True if configured, false if not configurable

## saveConfig()

Save provided configuration data for the given module

- Applicable only for modules that support configuration.
- Configuration data is stored encoded in the database "modules" table "data" field.

~~~~~~
// Getting, modifying and saving module config data
$data = $modules->getConfig('HelloWorld');
$data['greeting'] = 'Hello World! How are you today?';
$modules->saveConfig('HelloWorld', $data);
~~~~~~

3.0.16 Changed name from the more verbose saveModuleConfigData(), which will still work.

@param string|Module $class Module or module name

@param array|string $data Associative array of configuration data, or name of property you want to save.

@param mixed|null $value If you specified a property in previous arg, the value for the property.

@return bool True on success, false on failure

@throws WireException

@see Modules::getConfig()

@since 3.0.16 Use method saveModuleConfigData() with same arguments for prior versions (can also be used on any version).
