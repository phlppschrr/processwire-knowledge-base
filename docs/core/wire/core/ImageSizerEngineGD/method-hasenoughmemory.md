# $imageSizerEngineGD->hasEnoughMemory($filename = '', $double = true, $factor = 1, $action = 'action', $throwIfNot = false): bool

Source: `wire/core/ImageSizerEngineGD.php`

Additional functionality on top of existing checkMemoryForImage function for the flip/rotate actions

## Arguments

- string $filename Filename to check. Default is whatever was set to this ImageSizer.
- bool $double Need enough for both src and dst files loaded at same time? (default=true)
- int|float $factor Tweak factor (multiply needed memory by this factor), i.e. 2 for rotate actions. (default=1)
- string $action Name of action (if something other than "action")
- bool $throwIfNot Throw WireException if not enough memory? (default=false)

## Return value

bool

## Throws

- WireException
