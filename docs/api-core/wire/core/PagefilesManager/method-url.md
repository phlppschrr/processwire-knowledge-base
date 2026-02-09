# $pagefilesManager->url(): string

Source: `wire/core/PagefilesManager.php`

Get the published URL for files

## Usage

~~~~~
// basic usage
$string = $pagefilesManager->url();
~~~~~

## Return value

- `string`

## Exceptions

- `WireException` if attempting to access this on a Page that doesn't yet exist in the database
