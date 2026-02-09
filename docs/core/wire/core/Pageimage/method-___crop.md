# $pageimage->crop($x, $y, $width, $height, $options = array()): Pageimage

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
$pageimage = $pageimage->crop($x, $y, $width, $height);

// usage with all arguments
$pageimage = $pageimage->crop($x, $y, $width, $height, $options = array());
~~~~~

## Arguments

- `$x` `int` Starting X position (left) in pixels
- `$y` `int` Starting Y position (top) in pixels
- `$width` `int` Width of crop in pixels
- `$height` `int` Height of crop in pixels
- `$options` (optional) `array` See options array for `Pageimage::size()` method. Avoid setting crop properties in $options since we are overriding them.

## Return value

- `Pageimage`

## Hooking

- Hookable method name: `crop`
- Implementation: `___crop`
- Hook with: `Pageimage::crop`

### Hooking Before

~~~~~
$this->addHookBefore('Pageimage::crop', function(HookEvent $event) {
  $pageimage = $event->object;

  // Get arguments
  $x = $event->arguments(0);
  $y = $event->arguments(1);
  $width = $event->arguments(2);
  $height = $event->arguments(3);
  $options = $event->arguments(4);

  // Your code here

  // Optionally change arguments
  $event->arguments(0, $x);
  $event->arguments(1, $y);
  $event->arguments(2, $width);
  $event->arguments(3, $height);
  $event->arguments(4, $options);
});
~~~~~

### Hooking After

~~~~~
$this->addHookAfter('Pageimage::crop', function(HookEvent $event) {
  $pageimage = $event->object;

  // Get arguments
  $x = $event->arguments(0);
  $y = $event->arguments(1);
  $width = $event->arguments(2);
  $height = $event->arguments(3);
  $options = $event->arguments(4);

  // Your code here

  // Optionally modify return value
  $return = $event->return;
  $event->return = $return;
});
~~~~~
