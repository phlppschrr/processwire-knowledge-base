# $modules->getModuleInfo($class, array $options = array()): array

Source: `wire/core/Modules.php`

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

## Example

~~~~~
// example of getting module info
$moduleInfo = $modules->getModuleInfo('InputfieldCKEditor');

// example of getting verbose module info
$moduleInfo = $modules->getModuleInfoVerbose('MarkupAdminDataTable');
~~~~~

## Usage

~~~~~
// basic usage
$array = $modules->getModuleInfo($class);

// usage with all arguments
$array = $modules->getModuleInfo($class, array $options = array());
~~~~~

## Arguments

- `$class` `string|Module|int` Specify one of the following: - Module object instance - Module class name (string) - Module ID (int) - To get info for ALL modules, specify `*` or `all`. - To get system information, specify `ProcessWire` or `PHP`. - To get a blank module info template, specify `info`.
- `$options` (optional) `array` Optional options to modify behavior of what gets returned - `verbose` (bool): Makes the info also include verbose properties, which are otherwise blank. (default=false) - `minify` (bool): Remove non-applicable and properties that match defaults? (default=false, or true when getting `all`) - `noCache` (bool): prevents use of cache to retrieve the module info. (default=false)

## Return value

- `array` Associative array of module information. - On error, an `error` index is also populated with an error message. - When requesting a module that does not exist its `id` value will be `0` and its `name` will be blank.

## See Also

- [Modules::getModuleInfoVerbose()](method-getmoduleinfoverbose.md)

## Details

- @todo move all getModuleInfo methods to their own ModuleInfo class and break this method down further.
