# ModulesInfo

Source: `wire/core/ModulesInfo.php`

ProcessWire Modules: Info

ProcessWire 3.x, Copyright 2023 by Ryan Cramer
https://processwire.com

## other

@property-read array $moduleInfoCache

@property-read array $moduleInfoCacheVerbose

@property-read array $moduleInfoCacheUninstalled

@property-read array $moduleInfoVerboseKeys

@property-read array $modulesLastVersions

## moduleInfoCacheName

Filename for module info cache file

## moduleInfoCacheVerboseName

Filename for verbose module info cache file

## moduleInfoCacheUninstalledName

Filename for uninstalled module info cache file

## moduleLastVersionsCacheName

Cache name for module version change cache

## defaultNamespace

Default namespace

## moduleInfoCacheEmpty()

Is the module info cache empty?

@return bool

## moduleInfoCacheHas()

Does the module info cache have an entry for given module ID?

@param int $moduleID

@return bool

## getModuleInfoExternal()

Retrieve module info from ModuleName.info.json or ModuleName.info.php

@param string $moduleName

@return array

## getModuleInfoInternal()

Retrieve module info from internal getModuleInfo function in the class

@param Module|string $module

@param string $namespace

@return array

## getModuleInfoSystem()

Retrieve module info for system properties: PHP or ProcessWire

@param string $moduleName

@param array $options

@return array

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

@see self::getModuleInfoVerbose()

@todo move all getModuleInfo methods to their own ModuleInfo class and break this method down further.

## getModuleInfoAll()

Get info arrays for all modules indexed by module name

@param array $options See options for getModuleInfo() method

@return array

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

## extractModuleOperatorVersion()

Return array of ($module, $operator, $requiredVersion)

$version will be 0 and $operator blank if there are no requirements.

@param string $require Module class name with operator and version string

@return array of array($moduleClass, $operator, $version)

## saveModuleInfoCache()

Save the module information cache

## clearModuleInfoCache()

Clear the module information cache

@param bool|null $showMessages Specify true to show message notifications

## updateModuleVersionsCache()

Update the cache of queued module version changes

## checkModuleVersion()

Check the module version to make sure it is consistent with our moduleInfo

When not consistent, this triggers the moduleVersionChanged hook, which in turn
triggers the $module->___upgrade($fromVersion, $toVersion) method.

@param Module $module

## modulesLastVersions()

@param int|null $id

@return string|null|array

## moduleVersionChanged()

Module version changed

This calls the module's ___upgrade($fromVersion, $toVersion) method.

@param Module|_Module $module

@param int|string $fromVersion

@param int|string $toVersion

## getNamespaces()

Get an array of all unique, non-default, non-root module namespaces mapped to directory names

@return array
