# $processModuleInstall->downloadModuleFromDirectory($url, $destinationDir = ''): bool|string

Source: `wire/modules/Process/ProcessModule/ProcessModuleInstall.php`

Download module from directory

## Usage

~~~~~
// basic usage
$bool = $processModuleInstall->downloadModuleFromDirectory($url);

// usage with all arguments
$bool = $processModuleInstall->downloadModuleFromDirectory($url, $destinationDir = '');
~~~~~

## Arguments

- `$url` `string`
- `$destinationDir` (optional) `string`

## Return value

- `bool|string`

## Since

3.0.162
