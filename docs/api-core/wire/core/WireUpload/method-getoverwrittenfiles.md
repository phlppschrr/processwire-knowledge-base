# $wireUpload->getOverwrittenFiles(): array

Source: `wire/core/WireUpload.php`

Get files that were overwritten (for overwrite mode only)

WireUpload keeps a temporary backup of replaced files. The backup will be removed at __destruct()
You may retrieve backed up files temporarily if needed.

## Usage

~~~~~
// basic usage
$array = $wireUpload->getOverwrittenFiles();
~~~~~

## Return value

- `array` associative array of ('backup path/file' => 'replaced basename')
