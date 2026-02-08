# $modulesConfigs->isConfigurable($class, $useCache = true): bool|string|int

Source: `wire/core/ModulesConfigs.php`

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

## Arguments

- `$class` `Module|string` Module name
- `$useCache` (optional) `bool` Use caching? This accepts a few options: - Specify boolean `true` to allow use of cache when available (default behavior). - Specify boolean `false` to disable retrieval of this property from getModuleInfo (forces a new check). - Specify string `interface` to check only if module implements ConfigurableModule interface. - Specify string `file` to check only if module has a separate configuration class/file.

## Return value

bool|string|int See details about return values in method description.

## Since

3.0.16

## Details

- @todo this method has two distinct parts (file and interface) that need to be split in two methods.
