# $imageSizer->__construct($filename = '', $options = array())

Source: `wire/core/ImageSizer.php`

Construct the ImageSizer for a single image

## Usage

~~~~~
// basic usage
$result = $imageSizer->__construct();

// usage with all arguments
$result = $imageSizer->__construct($filename = '', $options = array());
~~~~~

## Arguments

- `$filename` (optional) `string` Filename to resize. Omit only if instantiating class for a getEngines() call.
- `$options` (optional) `array` Initial options to the engine.
