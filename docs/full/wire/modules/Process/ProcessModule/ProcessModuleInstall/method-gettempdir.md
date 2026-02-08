# $processModuleInstall->getTempDir(): string|bool

Source: `wire/modules/Process/ProcessModule/ProcessModuleInstall.php`

Returns a temporary directory (path) for use by this object

## Usage

~~~~~
// basic usage
$string = $processModuleInstall->getTempDir();
~~~~~

## Return value

- `string|bool` Returns false if you specified $create=false, and the dir doesn't exist

## Exceptions

- `WireException` If can't create temporary dir
