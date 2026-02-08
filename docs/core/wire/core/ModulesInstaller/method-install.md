# ModulesInstaller::install()

Source: `wire/core/ModulesInstaller.php`

Install the given module name


@param string $class Module name (class name)

@param array|bool $options Optional associative array that can contain any of the following:
 - `dependencies` (boolean): When true, dependencies will also be installed where possible. Specify false to prevent installation of uninstalled modules. (default=true)
 - `resetCache` (boolean): When true, module caches will be reset after installation. (default=true)
 - `force` (boolean): Force installation, even if dependencies can't be met.

@return null|Module Returns null if unable to install, or ready-to-use Module object if successfully installed.

@throws WireException
