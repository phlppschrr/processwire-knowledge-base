# $processModuleInstall->canInstallFromDirectory($notify = true): bool

Source: `wire/modules/Process/ProcessModule/ProcessModuleInstall.php`

Module install/upgrade from directory allowed?

## Usage

~~~~~
// basic usage
$bool = $processModuleInstall->canInstallFromDirectory();

// usage with all arguments
$bool = $processModuleInstall->canInstallFromDirectory($notify = true);
~~~~~

## Arguments

- `$notify` (optional) `bool`

## Return value

- `bool`
