# Pageimage::height()

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

@param int $n Optional height if you are creating a new size.

@param array|string|int|bool $options See `Pageimage::size()` $options argument for details.

@return int|Pageimage Returns height (in px) when given no arguments, or Pageimage when given a height argument.
