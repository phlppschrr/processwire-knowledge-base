# Pageimage: other

Source: `wire/core/Pageimage.php`

- [$width: int](method-width.md) Width of image, in pixels.

- [$height: int](method-height.md) Height of image, in pixels.

- [$focus: array](method-focus.md) Focus array contains 'top' (float), 'left' (float), 'zoom' (int), and 'default' (bool) properties.

- $focusStr: string Readable string containing focus information.

- $hasFocus: bool Does this image have custom focus settings? (i.e. $focus['default'] == true)

- [$suffix: array](method-suffix.md) Array containing file suffix(es).

- $suffixStr: string String of file suffix(es) separated by comma.

- $alt: string Convenient alias for the 'description' property, unless overridden (since 3.0.125).

- $src: string Convenient alias for the 'url' property, unless overridden (since 3.0.125).

- [$webp: PagefileExtra](method-webp.md) Access webp version of image (since 3.0.132)

- [$ratio: float](method-ratio.md) Image ratio where 1.0 is square, >1 is wider than tall, >2 is twice as wide as well, <1 is taller than wide, etc. (since 3.0.154+)
