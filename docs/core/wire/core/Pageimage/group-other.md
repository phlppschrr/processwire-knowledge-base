# Pageimage: other

Source: `wire/core/Pageimage.php`

@property-read int $width Width of image, in pixels.

@property-read int $height Height of image, in pixels.

@property-read array $focus Focus array contains 'top' (float), 'left' (float), 'zoom' (int), and 'default' (bool) properties.

@property-read string $focusStr Readable string containing focus information.

@property-read bool $hasFocus Does this image have custom focus settings? (i.e. $focus['default'] == true)

@property-read array $suffix Array containing file suffix(es).

@property-read string $suffixStr String of file suffix(es) separated by comma.

@property-read string $alt Convenient alias for the 'description' property, unless overridden (since 3.0.125).

@property-read string $src Convenient alias for the 'url' property, unless overridden (since 3.0.125).

@property-read PagefileExtra $webp Access webp version of image (since 3.0.132)

@property-read float $ratio Image ratio where 1.0 is square, >1 is wider than tall, >2 is twice as wide as well, <1 is taller than wide, etc. (since 3.0.154+)
