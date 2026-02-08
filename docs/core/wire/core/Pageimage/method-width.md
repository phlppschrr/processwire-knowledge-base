# $pageimage->width($n = 0, $options = array()): int|Pageimage

Source: `wire/core/Pageimage.php`

Return the width of this image OR return an image sized with a given width (and proportional height).

- If given a width, it'll return a new Pageimage object sized to that width.
- If not given a width, it'll return the current width of this Pageimage.


~~~~~
// Get width of image
$px = $image->width();

// Create a new variation at 200px width
$thumb = $image->width(200);
~~~~~

## Arguments

- int $n Optional width if you are creating a new size.
- array|string|int|bool $options See `Pageimage::size()` $options argument for details.

## Return value

int|Pageimage Returns width (in px) when given no arguments, or Pageimage when given a width argument.
