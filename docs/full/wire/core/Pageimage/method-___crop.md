# Pageimage::___crop()

Source: `wire/core/Pageimage.php`

Create a crop and return it as a new Pageimage.

~~~~~
// Create a crop starting 100 pixels from left, 200 pixels from top
// at 150 pixels wide and 100 pixels tall
$image = $page->images->first();
$crop = $image->crop(100, 200, 150, 100);

// Output the crop
echo "<img src='$crop->url' />";
~~~~~


@param int $x Starting X position (left) in pixels

@param int $y Starting Y position (top) in pixels

@param int $width Width of crop in pixels

@param int $height Height of crop in pixels

@param array $options See options array for `Pageimage::size()` method.
  Avoid setting crop properties in $options since we are overriding them.

@return Pageimage
