# $pageimage->___crop($x, $y, $width, $height, $options = array()): Pageimage

Source: `wire/core/Pageimage.php`

Create a crop and return it as a new Pageimage.

## Example

~~~~~
// Create a crop starting 100 pixels from left, 200 pixels from top
// at 150 pixels wide and 100 pixels tall
$image = $page->images->first();
$crop = $image->crop(100, 200, 150, 100);

// Output the crop
echo "<img src='$crop->url' />";
~~~~~

## Usage

~~~~~
// basic usage
$pageimage = $pageimage->___crop($x, $y, $width, $height);

// usage with all arguments
$pageimage = $pageimage->___crop($x, $y, $width, $height, $options = array());
~~~~~

## Arguments

- `$x` `int` Starting X position (left) in pixels
- `$y` `int` Starting Y position (top) in pixels
- `$width` `int` Width of crop in pixels
- `$height` `int` Height of crop in pixels
- `$options` (optional) `array` See options array for `Pageimage::size()` method. Avoid setting crop properties in $options since we are overriding them.

## Return value

- `Pageimage`
