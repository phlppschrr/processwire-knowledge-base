# $wireUpload->setValidExtensions(array $extensions): $this

Source: `wire/core/WireUpload.php`

Set allowed file extensions

## Usage

~~~~~
// basic usage
$result = $wireUpload->setValidExtensions($extensions);

// usage with all arguments
$result = $wireUpload->setValidExtensions(array $extensions);
~~~~~

## Arguments

- `$extensions` `array` Array of file extensions (strings), not including periods

## Return value

- `$this`
