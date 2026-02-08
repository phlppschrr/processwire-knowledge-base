# $imageSizer->___resize($targetWidth, $targetHeight = 0): bool

Source: `wire/core/ImageSizer.php`

Resize the image proportionally to the given width/height

## Arguments

- `$targetWidth` `int` Target width in pixels, or 0 for proportional to height
- `$targetHeight` (optional) `int` Target height in pixels, or 0 for proportional to width. Optional-if not specified, 0 is assumed.

## Return value

bool True if the resize was successful, false if not

## Throws

- WireException when not enough memory to load image or missing required data
