# $pageimage->size($width, $height = 0, $options = array()): Pageimage

Source: `wire/core/Pageimage.php`

Return an image (Pageimage) sized/cropped to the specified dimensions.

`$thumb = $image->size($width, $height, $options);`

The default behavior of this method is to simply create and return a new resized version of the image,
leaving the original in tact. Width and height of the target size are the the first two arguments.
The third argument called `$options` enables you to modify the default behavior of the size() method
in various ways. This method only creates the newly sized image once, and then it caches it. Future
calls simply refer back to the previously resized image.


**About the $options argument**

- If given a *string*, it is assumed to be the value for the "cropping" option.
- If given an *integer*, it is assumed you are specifying a "quality" value (1-100).
- If given a *boolean*, it is assumed you are specifying whether or not you want to allow "upscaling".
- If given an *array*, you may specify any of the options below together:

**All available $options**

 - `quality` (int): Quality setting 1-100 (default=90, or as specified in /site/config.php).
 - `upscaling` (bool): Allow image to be upscaled? (default=true).
 - `cropping` (string|bool|array): Cropping mode, see possible values in "cropping" section below (default=true).
 - `suffix` (string|array): Suffix word to identify the new image, or use array of words for multiple (default=none).
 - `forceNew` (bool): Force re-creation of the image even if it already exists? (default=false).
 - `sharpening` (string): Sharpening mode: "none", "soft", "medium", or "strong" (default=soft).
 - `autoRotation` (bool): Automatically correct rotation of images that provide this info? (default=true)
 - `rotate` (int): Rotate the image this many degrees, specify one of: 0, -270, -180, -90, 90, 180, or 270 (default=0).
 - `flip` (string): To flip, specify either "vertical" or "horizontal" (default=none).
 - `hidpi` (bool): Use HiDPI/retina pixel doubling? (default=false).
 - `hidpiQuality` (bool): Quality setting for HiDPI (default=40, typically lower than regular quality setting).
 - `cleanFilename` (bool): Clean filename of historical resize information for shorter filenames? (default=false).
 - `nameWidth` (int): Width to use for filename (default is to use specified $width argument).
 - `nameHeight` (int): Height to use for filename (default is to use specified $height argument).
 - `focus` (bool): Should resizes that result in crop use focus area if available? (default=true).
    In order for focus to be applicable, resize must include both width and height.
 - `allowOriginal` (bool): Return original if already at width/height? May not be combined with other options. (default=false)
 - `webpAdd` (bool): Also create a secondary .webp image variation? (default=false)
 - `webpQuality` (int): Quality setting for extra webp images (default=90).

**Possible values for "cropping" option**

 - `true` (bool): Auto detect and allow use of focus (default).
 - `false` (bool): Disallow cropping.
 - `center` (string): to crop to center of image.
 - `x111y222` (string): to crop by pixels, 111px from left and 222px from top (replacing 111 and 222 with your values).
 - `north` (string): Crop North (top), may also be just "n".
 - `northwest` (string): Crop from Northwest (top left), may also be just "nw".
 - `northeast` (string): Crop from Northeast (top right), may also be just "ne".
 - `south` (string): Crop South (bottom), may also be just "s".
 - `southwest` (string): Crop Southwest (bottom left), may also be just "sw".
 - `southeast` (string): Crop Southeast (bottom right), may also be just "se".
 - `west` (string): Crop West (left), may also be just "w".
 - `east` (string): Crop East (right), may alos be just "e".
 - `blank` (string): Specify a blank string to disallow cropping during resize.
 - `array(111,222)` (array): Array of integers index 0 is left pixels and index 1 is top pixels.
 - `array('11%','22%')` (array): Array of '%' appended strings where index 0 is left percent and index 1 is top percent.

**Note about "quality" and "upscaling" options**

ProcessWire doesn't keep separate copies of images with different "quality" or "upscaling" values.
If you change these and a variation image at the existing dimensions already exists, then you'll still get the old version.
To clear out an old version of an image, use the `Pageimage::removeVariations()` method in this class before calling
size() with new quality or upscaling settings.

## Example

~~~~~
// Get an image to resize
$image = $page->images->first();

// Create 400x300 thumbnail cropped to center
$thumb = $image->size(400, 300);

// Create thumbnail with cropping to top
$thumb = $image->size(400, 300, 'north');

// Create thumbnail while specifying $options
$thumb = $image->size(400, 300, [
  'cropping' => 'north',
  'quality' => 60,
  'upscaling' => false,
  'sharpening' => 'medium'
]);

// Output thumbnail
echo "<img src='$thumb->url' />";

// Create image of size predefined in $config->imageSizes (3.0.151+)
$photo = $image->size('landscape');
~~~~~

## Usage

~~~~~
// basic usage
$pageimage = $pageimage->size($width);

// usage with all arguments
$pageimage = $pageimage->size($width, $height = 0, $options = array());
~~~~~

## Arguments

- `$width` `int|string` Target width of new image or (3.0.151+) specify prefined image size name
- `$height` (optional) `int|array` Target height of new image or (3.0.151+) options array if no height argument needed
- `$options` (optional) `array|string|int` Array of options to override default behavior: - Specify `array` of options as indicated in the section above. - Or you may specify type `string` containing "cropping" value. - Or you may specify type `int` containing "quality" value. - Or you may specify type `bool` containing "upscaling" value.

## Return value

- `Pageimage` Returns a new Pageimage object that is a variation of the original. If the specified dimensions/options are the same as the original, then the original will be returned.
