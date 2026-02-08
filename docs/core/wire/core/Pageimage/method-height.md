# $pageimage->height($n = 0, $options = array()): int|Pageimage

Source: `wire/core/Pageimage.php`

Return the height of this image OR return an image sized with a given height (and proportional width).

- If given a height, it'll return a new Pageimage object sized to that height.
- If not given a height, it'll return the height of this Pageimage.


~~~~~
// Get height of image
$px = $image->height();

// Create a new variation at 200px height
$thumb = $image->height(200);
~~~~~

## Arguments

- `$n` (optional) `int` Optional height if you are creating a new size.
- `$options` (optional) `array|string|int|bool` See `Pageimage::size()` $options argument for details.

## Return value

int|Pageimage Returns height (in px) when given no arguments, or Pageimage when given a height argument.
