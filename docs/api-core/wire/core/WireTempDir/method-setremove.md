# $wireTempDir->setRemove($remove = true): $this

Source: `wire/core/WireTempDir.php`

Call this with 'false' to prevent temp dir from being removed automatically when object is destructed

If you do this, then you accept responsibility for removing the directory by calling $tempDir->remove();
If you do not remove it yourself, WireTempDir will remove as part of the daily maintenance.

## Usage

~~~~~
// basic usage
$result = $wireTempDir->setRemove();

// usage with all arguments
$result = $wireTempDir->setRemove($remove = true);
~~~~~

## Arguments

- `$remove` (optional) `bool`

## Return value

- `$this`
