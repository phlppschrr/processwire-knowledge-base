# $processModuleInstall->downloadModuleFromUrl($url, $destinationDir = ''): bool|string

Source: `wire/modules/Process/ProcessModule/ProcessModuleInstall.php`

Download module from URL

## Usage

~~~~~
// basic usage
$bool = $processModuleInstall->downloadModuleFromUrl($url);

// usage with all arguments
$bool = $processModuleInstall->downloadModuleFromUrl($url, $destinationDir = '');
~~~~~

## Arguments

- `$url` `string`
- `$destinationDir` (optional) `string`

## Return value

- `bool|string`

## Since

3.0.162
