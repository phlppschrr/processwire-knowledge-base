# Modules

Source: `wire/core/Modules.php`

ProcessWire Modules

Loads and manages all runtime modules for ProcessWire

ProcessWire 3.x, Copyright 2023 by Ryan Cramer
https://processwire.com

Loads and manages all modules in ProcessWire.
The `$modules` API variable is most commonly used for getting individual modules to use their API.
~~~~~
// Getting a module by name
$m = $modules->get('MarkupPagerNav');

// Getting a module by name (alternate)
$m = $modules->MarkupPagerNav;
~~~~~


Note that when iterating, find(), or calling any other method that returns module(s), excepting get(), a ModulePlaceholder may be
returned rather than a real Module. ModulePlaceholders are used in instances when the module may or may not be needed at runtime
in order to save resources. As a result, anything iterating through these Modules should check to make sure it's not a ModulePlaceholder
before using it. If it's a ModulePlaceholder, then the real Module can be instantiated/retrieved by $modules->get($className).

## other

@method void refresh($showMessages = false) Refresh the cache that stores module files by recreating it

@method null|Module install($class, $options = array())

@method bool|int delete($class)

@method bool uninstall($class)

@method bool saveConfig($class, $data, $value = null)

@property-read array $installableFiles

@property-read string $coreModulesDir

@property-read string $coreModulesPath

@property-read string $siteModulesPath

@property-read array $moduleIDs

@property-read array $moduleNames

@property-read ModulesInfo $info

@property-read ModulesLoader $loader

@property-read ModulesFlags $flags

@property-read ModulesFiles $files

@property-read ModulesInstaller $installer

@property-read ModulesConfigs $configs

@property-read bool $refreshing

## flagsSingular

Flag indicating the module may have only one instance at runtime.

## flagsAutoload

Flag indicating that the module should be instantiated at runtime, rather than when called upon.

## flagsDuplicate

Flag indicating the module has more than one copy of it on the file system.

## flagsConditional

When combined with flagsAutoload, indicates that the autoload is conditional

## flagsDisabled

When combined with flagsAutoload, indicates that the module's autoload state is temporarily disabled

## flagsNoUserConfig

Indicates module that maintains a configurable interface but with no interactive Inputfields

## flagsNoFile

Module where no file could be located

## flagsSystemCache

Indicates row is for Modules system cache use and not an actual module

@since 3.0.218

## __construct()

Construct the Modules

@param string $path Core modules path (you may add other paths with addPath method)

## isValidItem()

*******************************************************************************************
WIREARRAY OVERRIDES

## get()

*******************************************************************************************
GETTING/LOADING MODULES

## get()

Get the requested Module

- If the module is not installed, but is installable, it will be installed, instantiated, and initialized.
  If you don't want that behavior, call `$modules->isInstalled('ModuleName')` as a conditional first.
- You can also get/load a module by accessing it directly, like `$modules->ModuleName`.
- To get a module with additional options, use `$modules->getModule($name, $options)` instead.

~~~~~
// Get the MarkupAdminDataTable module
$table = $modules->get('MarkupAdminDataTable');

// You can also do this
$table = $modules->MarkupAdminDataTable;
~~~~~

@param string|int $key Module name (also accepts database ID)

@return Module|_Module|null Returns a Module or null if not found

@throws WirePermissionException If module requires a particular permission the user does not have

@see Modules::getModule(), Modules::isInstalled()

## getModule()

Get the requested Module (with options)

This is the same as `$modules->get()` except that you can specify additional options to modify default behavior.
These are the options you can specify in the `$options` array argument:

 - `noPermissionCheck` (bool): Specify true to disable module permission checks (and resulting exception). (default=false)
 - `noInstall` (bool): Specify true to prevent a non-installed module from installing from this request. (default=false)
 - `noInit` (bool): Specify true to prevent the module from being initialized or configured. (default=false). See `configOnly` as alternative.
 - `noSubstitute` (bool): Specify true to prevent inclusion of a substitute module. (default=false)
 - `noCache` (bool): Specify true to prevent module instance from being cached for later getModule() calls. (default=false)
 - `noThrow` (bool): Specify true to prevent exceptions from being thrown on permission or fatal error. (default=false)
 - `returnError` (bool): Return an error message (string) on error, rather than null. (default=false)
 - `configOnly` (bool): Populate module config data but do not call its init() method. (default=false) 3.0.169+. Alternative to `noInit`.
 - `configData` (array): Associative array of additional config data to populate to module. (default=[]) 3.0.169+

If the module is not installed, but is installable, it will be installed, instantiated, and initialized.
If you don't want that behavior, call `$modules->isInstalled('ModuleName')` as a condition first, OR specify
true for the `noInstall` option in the `$options` argument.

@param string|int $key Module name or database ID.

@param array $options Optional settings to change load behavior, see method description for details.

@return Module|_Module|null|string Returns ready-to-use module or NULL|string if not found (string if `returnError` option used).

@throws WirePermissionException|\Exception If module requires a particular permission the user does not have

@see Modules::get()

## findByPrefix()

*******************************************************************************************
FINDER METHODS

## findByPrefix()

Find modules matching the given prefix (i.e. “Inputfield”)

By default this method returns module class names matching the given prefix.
To instead retrieve instantiated (ready-to-use) modules, specify boolean true
for the second argument. Regardless of `$load` argument all returned arrays
are indexed by module name.

~~~~~
// Retrieve array of all Textformatter module names
$items = $modules->findByPrefix('Textformatter');

// Retrieve array of all Textformatter modules (ready to use)
$items = $modules->findByPrefix('Textformatter', true);
~~~~~

@param string $prefix Specify prefix, i.e. "Process", "Fieldtype", "Inputfield", etc.

@param bool|int $load Specify one of the following (all indexed by module name):
 - Boolean true to return array of instantiated modules.
 - Boolean false to return array of module names (default).
 - Integer 1 to return array of module info for each matching module.
 - Integer 2 to return array of verbose module info for each matching module.
 - Integer 3 to return array of Module or ModulePlaceholder objects (whatever current state is). Added 3.0.146.

@return array Returns array of module class names, module info arrays, or Module objects. In all cases, array indexes are class names.

## findByInfo()

Find modules by matching a property or properties in their module info

@param string|array $selector Specify one of the following:
 - Selector string to match module info.
 - Array of [ 'property' => 'value' ] to match in module info (this is not a selector array).
 - Name of property that will match module if not empty in module info.

@param bool|int $load Specify one of the following:
 - Boolean true to return array of instantiated modules.
 - Boolean false to return array of module names (default).
 - Integer 1 to return array of module info for each matching module.
 - Integer 2 to return array of verbose module info for each matching module.

@return array Array of modules, module names or module info arrays, indexed by module name.

## getInstallable()

*******************************************************************************************
INSTALLER METHODS

## isInstalled()

Is the given module name installed?

@param string $class Just a module class name, or optionally: `ModuleClassName>=1.2.3` (operator and version)

@return bool True if installed, false if not

## ___install()

Install the given module name


@param string $class Module name (class name)

@param array|bool $options Optional associative array that can contain any of the following:
 - `dependencies` (boolean): When true, dependencies will also be installed where possible. Specify false to prevent installation of uninstalled modules. (default=true)
 - `resetCache` (boolean): When true, module caches will be reset after installation. (default=true)
 - `force` (boolean): Force installation, even if dependencies can't be met.

@return null|Module Returns null if unable to install, or ready-to-use Module object if successfully installed.

@throws WireException

## ___delete()

Delete the given module, physically removing its files


@param string $class Module name (class name)

@return bool

@throws WireException If module can't be deleted, exception will be thrown containing reason.

## ___uninstall()

Uninstall the given module name


@param string $class Module name (class name)

@return bool

@throws WireException

## getFlags()

*******************************************************************************************
MODULE FLAGS

## moduleInfoCache()

*******************************************************************************************
MODULE INFO

## getModuleID()

Returns the database ID of a given module class, or 0 if not found

@param string|int|Module $class Module, module name or ID

@return int

## getModuleInfo()

Returns an associative array of information for a Module

The array returned by this method includes the following:

 - `id` (int): module database ID.
 - `name` (string): module class name.
 - `title` (string): module title.
 - `version` (int): module version.
 - `icon` (string): Optional icon name (excluding the "fa-") part.
 - `requires` (array): module names required by this module.
 - `requiresVersions` (array): required module versions–module name is key, value is array($operator, $version).
 - `installs` (array): module names that this module installs.
 - `permission` (string): permission name required to execute this module.
 - `autoload` (bool): true if module is autoload, false if not.
 - `singular` (bool): true if module is singular, false if not.
 - `created` (int): unix-timestamp of date/time module added to system (for uninstalled modules, it is the file date).
 - `installed` (bool): is the module currently installed? (boolean, or null when not determined)
 - `configurable` (bool|int): true or positive number when the module is configurable.
 - `namespace` (string): PHP namespace that module lives in.

The following properties are also included when "verbose" mode is requested. When not in verbose mode, these
properties may be present but with empty values:

 - `versionStr` (string): formatted module version string.
 - `file` (string): module filename from PW installation root, or false when it can't be found.
 - `core` (bool): true when module is a core module, false when not.
 - `author` (string): module author, when specified.
 - `summary` (string): summary of what this module does.
 - `href` (string): URL to module details (when specified).
 - `permissions` (array): permissions installed by this module, associative array ('permission-name' => 'Description').
 - `page` (array): definition of page to create for Process module (see Process class)

The following properties appear only for "Process" modules, and only if specified by module.
See the Process class for more details:

 - `nav` (array): navigation definition
 - `useNavJSON` (bool): whether the Process module provides JSON navigation
 - `permissionMethod` (string|callable): method to call to determine permission
 - `page` (array): definition of page to create for Process module

On error, an `error` index in returned array contains error message. You can also identify errors
such as a non-existing module by the returned module info having an `id` index of `0`

~~~~~
// example of getting module info
$moduleInfo = $modules->getModuleInfo('InputfieldCKEditor');

// example of getting verbose module info
$moduleInfo = $modules->getModuleInfoVerbose('MarkupAdminDataTable');
~~~~~

@param string|Module|int $class Specify one of the following:
 - Module object instance
 - Module class name (string)
 - Module ID (int)
 - To get info for ALL modules, specify `*` or `all`.
 - To get system information, specify `ProcessWire` or `PHP`.
 - To get a blank module info template, specify `info`.

@param array $options Optional options to modify behavior of what gets returned
 - `verbose` (bool): Makes the info also include verbose properties, which are otherwise blank. (default=false)
 - `minify` (bool): Remove non-applicable and properties that match defaults? (default=false, or true when getting `all`)
 - `noCache` (bool): prevents use of cache to retrieve the module info. (default=false)

@return array Associative array of module information.
 - On error, an `error` index is also populated with an error message.
 - When requesting a module that does not exist its `id` value will be `0` and its `name` will be blank.

@see Modules::getModuleInfoVerbose()

@todo move all getModuleInfo methods to their own ModuleInfo class and break this method down further.

## getModuleInfoVerbose()

Returns a verbose array of information for a Module

This is the same as what’s returned by `Modules::getModuleInfo()` except that it has the following additional properties:

 - `versionStr` (string): formatted module version string.
 - `file` (string): module filename from PW installation root, or false when it can't be found.
 - `core` (bool): true when module is a core module, false when not.
 - `author` (string): module author, when specified.
 - `summary` (string): summary of what this module does.
 - `href` (string): URL to module details (when specified).
 - `permissions` (array): permissions installed by this module, associative array ('permission  - name' => 'Description').
 - `page` (array): definition of page to create for Process module (see Process class)

@param string|Module|int $class May be class name, module instance, or module ID

@param array $options Optional options to modify behavior of what gets returned:
 - `noCache` (bool): prevents use of cache to retrieve the module info
 - `noInclude` (bool): prevents include() of the module file, applicable only if it hasn't already been included

@return array Associative array of module information

@see Modules::getModuleInfo()

## getModuleInfoProperty()

Get just a single property of module info

@param Module|string $class Module instance or module name

@param string $property Name of property to get

@param array $options Additional options (see getModuleInfo method for options)

@return mixed|null Returns value of property or null if not found

@since 3.0.107

## getConfig()

*******************************************************************************************
MODULE CONFIG

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

## ___saveConfig()

Save provided configuration data for the given module

- Applicable only for modules that support configuration.
- Configuration data is stored encoded in the database "modules" table "data" field.

~~~~~~
// Getting, modifying and saving all module config data
$data = $modules->getConfig('HelloWorld');
$data['greeting'] = 'Hello World! How are you today?';
$modules->saveConfig('HelloWorld', $data);

// Getting a single configuration property
$value = $modules->getConfig('HelloWorld', 'some_property');

// Saving a single configuration property
$modules->saveConfig('HelloWorld', 'some_property', 'New Value');
~~~~~~

3.0.16 Changed name from the more verbose saveModuleConfigData(), which will still work.

@param string|Module $class Module or module name

@param array|string $data Associative array of configuration data, or name of property you want to save.

@param mixed|null $value If you specified a property in previous arg, the value for the property.

@return bool True on success, false on failure

@throws WireException

@see Modules::getConfig()

@since 3.0.16 Use method saveModuleConfigData() with same arguments for prior versions (can also be used on any version).

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

## getModuleEditUrl()

Return the URL where the module can be edited, configured or uninstalled

If module is not installed, it returns URL to install the module.


@param string|Module $className

@param bool $collapseInfo

@return string

## getModuleInstallUrl()

Get URL where an administrator can install given module name

If module is already installed, it returns the URL to edit the module.


@param string $className

@return string

@since 3.0.216

## isSingular()

*********************************************************************************************
TOOLS

## ___refresh()

Refresh the modules cache

This forces the modules file and information cache to be re-created.


@param bool $showMessages Show notification messages about what was found? (default=false) 3.0.172+

## getRequiredBy()

**********************************************************************************
DEPENDENCIES

## setSubstitute()

**********************************************************************************
SUBSTITUTES

## getModuleFile()

**********************************************************************************
FILES

## getModuleFile()

Get the path + filename (or optionally URL) for this module

@param string|Module $class Module class name or object instance

@param array|bool $options Options to modify default behavior:
	- `getURL` (bool): Specify true if you want to get the URL rather than file path (default=false).
	- `fast` (bool): Specify true to omit file_exists() checks (default=false).
 - `guess` (bool): Manufacture/guess a module location if one cannot be found (default=false) 3.0.170+
	- Note: If you specify a boolean for the $options argument, it is assumed to be the $getURL property.

@return bool|string Returns string of module file, or false on failure.

## getModuleLanguageFiles()

Get module language translation files

@param Module|string $module

@return array Array of translation files including full path, indexed by basename without extension

@since 3.0.181

## __invoke()

**********************************************************************************
DEBUG AND CLASS SUPPORT

## __invoke()

Enables use of $modules('ModuleName')

@param string $key

@return Module|null

## memcache()

**********************************************************************************
CACHES

## memcache()

Set a runtime memory cache

@param string $name

@param mixed $setValue

@return bool|array|mixed|null

## __get()

Direct read-only properties

@param string $name

@return mixed
