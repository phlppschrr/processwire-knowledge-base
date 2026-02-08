# $pageimage->___crop($x, $y, $width, $height, $options = array()): Pageimage

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

## Arguments

- int $x Starting X position (left) in pixels
- int $y Starting Y position (top) in pixels
- int $width Width of crop in pixels
- int $height Height of crop in pixels
- array $options See options array for `Pageimage::size()` method. Avoid setting crop properties in $options since we are overriding them.

## Return value

Pageimage
