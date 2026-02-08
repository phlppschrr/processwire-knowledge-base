# $imageSizerEngineGD->hasEnoughMemory($filename = '', $double = true, $factor = 1, $action = 'action', $throwIfNot = false): bool

Source: `wire/core/ImageSizerEngineGD.php`

Additional functionality on top of existing checkMemoryForImage function for the flip/rotate actions

## Usage

~~~~~
// basic usage
$bool = $imageSizerEngineGD->hasEnoughMemory();

// usage with all arguments
$bool = $imageSizerEngineGD->hasEnoughMemory($filename = '', $double = true, $factor = 1, $action = 'action', $throwIfNot = false);
~~~~~

## Arguments

- `$filename` (optional) `string` Filename to check. Default is whatever was set to this ImageSizer.
- `$double` (optional) `bool` Need enough for both src and dst files loaded at same time? (default=true)
- `$factor` (optional) `int|float` Tweak factor (multiply needed memory by this factor), i.e. 2 for rotate actions. (default=1)
- `$action` (optional) `string` Name of action (if something other than "action")
- `$throwIfNot` (optional) `bool` Throw WireException if not enough memory? (default=false)

## Return value

- `bool`

## Exceptions

- `WireException`
