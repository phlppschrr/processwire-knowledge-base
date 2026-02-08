# $imageSizerEngineGD->processAction($srcFilename, $dstFilename, $action, $value): bool

Source: `wire/core/ImageSizerEngineGD.php`

Process a rotate or flip action

## Arguments

- string $srcFilename
- string $dstFilename
- string $action One of 'rotate' or 'flip'
- int|string $value If rotate, specify int of degrees. If flip, specify one of 'vertical', 'horizontal' or 'both'.

## Return value

bool

## Throws

- WireException
