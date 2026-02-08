# $modules->getModuleInfoVerbose($class, array $options = array()): array

Source: `wire/core/Modules.php`

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

## Arguments

- string|Module|int $class May be class name, module instance, or module ID
- array $options Optional options to modify behavior of what gets returned: - `noCache` (bool): prevents use of cache to retrieve the module info - `noInclude` (bool): prevents include() of the module file, applicable only if it hasn't already been included

## Return value

array Associative array of module information

## See also

- [Modules::getModuleInfo()](method-getmoduleinfo.md)
