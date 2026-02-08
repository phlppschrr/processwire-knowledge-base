# Pageimage

Source: `wire/core/Pageimage.php`

ProcessWire Pageimage

Represents an image item attached to a page, typically via an Image Fieldtype.
A variation refers to an image that is based upon another (like a resized or cropped version for example).
Pageimage objects are usually contained by a `Pageimages` object, which is a type of `Pagefiles` and `WireArray`.
In addition to the methods and properties below, you'll also want to look at `Pagefile` which this class inherits
several important methods and properties from.

~~~~~
// Example of outputting a thumbnail gallery of Pageimage objects
foreach($page->images as $image) {
  // $image and $thumb are both Pageimage objects
  $thumb = $image->size(200, 200);
  echo "<a href='$image->url'>";
  echo "<img src='$thumb->url' alt='$image->description' />";
  echo "</a>";
}
~~~~~

ProcessWire 3.x, Copyright 2020 by Ryan Cramer
https://processwire.com


Properties inherited from Pagefile
==================================

@property-read string $url URL to the file on the server.

@property-read string $httpUrl URL to the file on the server including scheme and hostname.

@property-read string $URL Same as $url property but with browser cache busting query string appended.

@property-read string $HTTPURL Same as the cache-busting uppercase “URL” property, but includes scheme and hostname.

@property-read string $filename Full disk path to the file on the server.

@property-read string $name Returns the filename without the path, same as the "basename" property.

@property-read string $hash Get a unique hash (for the page) representing this Pagefile.

@property-read array $tagsArray Get file tags as an array. @since 3.0.17

@property string $basename Returns the filename without the path.

@property string $description Value of the file’s description field (string), if enabled. Note you can also set this property directly.

@property string $tags Value of the file’s tags field (string), if enabled.

@property string $ext File’s extension (i.e. last 3 or so characters)

@property-read int $filesize File size (number of bytes).

@property int $modified Unix timestamp of when Pagefile (file, description or tags) was last modified.

@property-read string $modifiedStr Readable date/time string of when Pagefile was last modified.

@property-read int $mtime Unix timestamp of when file (only) was last modified.

@property-read string $mtimeStr Readable date/time string when file (only) was last modified.

@property int $created Unix timestamp of when file was created.

@property-read string $createdStr Readable date/time string of when Pagefile was created

@property string $filesizeStr File size as a formatted string, i.e. “123 Kb”.

@property Pagefiles $pagefiles The Pagefiles WireArray that contains this file.

@property Page $page The Page object that this file is part of.

@property Field $field The Field object that this file is part of.

@property PageimageDebugInfo $debugInfo

Hookable methods
================

@method bool|array isVariation($basename, $options = array())

@method Pageimage crop($x, $y, $width, $height, $options = array())

@method array rebuildVariations($mode = 0, array $suffix = array(), array $options = array())

@method install($filename)

@method render($markup = '', $options = array())

@method void createdVariation(Pageimage $image, array $data) Called after new image variation created (3.0.180+)

@method bool filenameDoesNotExist($filename) Hook called when a filename does not exist

## resize-and-crop

@property-read string $error Last image resizing error message, when applicable.

## variations

@property-read Pageimage $original Reference to original $image, if this is a resized version.

## other

@property-read int $width Width of image, in pixels.

@property-read int $height Height of image, in pixels.

@property-read array $focus Focus array contains 'top' (float), 'left' (float), 'zoom' (int), and 'default' (bool) properties.

@property-read string $focusStr Readable string containing focus information.

@property-read bool $hasFocus Does this image have custom focus settings? (i.e. $focus['default'] == true)

@property-read array $suffix Array containing file suffix(es).

@property-read string $suffixStr String of file suffix(es) separated by comma.

@property-read string $alt Convenient alias for the 'description' property, unless overridden (since 3.0.125).

@property-read string $src Convenient alias for the 'url' property, unless overridden (since 3.0.125).

@property-read PagefileExtra $webp Access webp version of image (since 3.0.132)

@property-read float $ratio Image ratio where 1.0 is square, >1 is wider than tall, >2 is twice as wide as well, <1 is taller than wide, etc. (since 3.0.154+)

## __construct()

Construct a new Pageimage

~~~~~
// Construct a new Pageimage, assumes that $page->images is a FieldtypeImage Field
$pageimage = new Pageimage($page->images, '/path/to/file.png');
~~~~~

@param Pagefiles $pagefiles

@param string $filename Full path and filename to this pagefile

@throws WireException

## url()

Return the web accessible URL to this image file


@return string

## filename()

Returns the full disk path to the image file


@return string

## suffix()

Returns array of suffixes for this file, or true/false if this file has the given suffix.

When providing a suffix, this method can be thought of: hasSuffix(suffix)


@param string $s Optionally provide suffix to return true/false if file has the suffix

@return array|bool Returns array of suffixes, or true|false if given a suffix in the arguments.

## focus()

Get or set focus area for crops to use

These settings are used by $this->size() calls that specify BOTH width AND height. Focus helps to
ensure that the important subject of the photo is not cropped out when the requested size proportion
differs from the original image proportion. For example, not chopping off someone’s head in a photo.

Default behavior is to return an array containing "top" and "left" indexes, representing percentages
from top and left. When arguments are specified, you are either setting the top/left percentages, or
unsetting focus, or getting focus in different ways, described in arguments below.

A zoom argument/property is also present here for future use, but not currently supported.


@param null|float|int|array|false $top Omit to get focus array, or specify one of the following:
  - GET: Omit all arguments to get focus array (default behavior).
  - GET: Specify boolean TRUE to return TRUE if focus data is present or FALSE if not.
  - GET: Specify integer 1 to make this method return pixel dimensions rather than percentages.
  - SET: Specify both $top and $left arguments to set (values assumed to be percentages).
  - SET: Specify array containing "top" and "left" indexes to set (percentages).
  - SET: Specify array where index 0 is top and index 1 is left (percentages).
  - SET: Specify string in the format "top left", i.e. "25 70" or "top left zoom", i.e. "25 70 30" (percentages).
  - SET: Specify CSV key=value string in the format "top=25%, left=70%, zoom=30%" in any order
  - UNSET: Specify boolean false to remove any focus values.

@param null|float|int $left Set left value (when $top value is float|int)
  - This argument is only used when setting focus and should be omitted otherwise.

@param null|int $zoom Zoom percent (not currently supported)

@return array|bool|Pageimage Returns one of the following:
  - When getting returns array containing top, left and default properties.
  - When TRUE was specified for the $top argument, it returns either TRUE (has focus) or FALSE (does not have).
  - When setting or unsetting returns $this.

## set()

Set property

@param string $key

@param mixed $value

@return Pageimage|WireData

## size()

Return an image (Pageimage) sized/cropped to the specified dimensions.

`$thumb = $image->size($width, $height, $options);`

The default behavior of this method is to simply create and return a new resized version of the image,
leaving the original in tact. Width and height of the target size are the the first two arguments.
The third argument called `$options` enables you to modify the default behavior of the size() method
in various ways. This method only creates the newly sized image once, and then it caches it. Future
calls simply refer back to the previously resized image.

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


@param int|string $width Target width of new image or (3.0.151+) specify prefined image size name

@param int|array $height Target height of new image or (3.0.151+) options array if no height argument needed

@param array|string|int $options Array of options to override default behavior:
 - Specify `array` of options as indicated in the section above.
 - Or you may specify type `string` containing "cropping" value.
 - Or you may specify type `int` containing "quality" value.
 - Or you may specify type `bool` containing "upscaling" value.

@return Pageimage Returns a new Pageimage object that is a variation of the original.
 If the specified dimensions/options are the same as the original, then the original will be returned.

## sizeName()

Return image of size indicated by predefined setting

Settings for predefined sizes can be specified in `$config->imageSizes` array.
Each named item in this array must contain at least 'width' and 'height, but can also
contain any other option from the `Pageimage::size()` argument `$options`.

@param string $name Image size name

@param array $options Optionally add or override options defined for size.

@return Pageimage

@since 3.0.151

@throws WireException If given a $name that is not present in $config->imageSizes

## ___crop()

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

## width()

Return the width of this image OR return an image sized with a given width (and proportional height).

- If given a width, it'll return a new Pageimage object sized to that width.
- If not given a width, it'll return the current width of this Pageimage.


~~~~~
// Get width of image
$px = $image->width();

// Create a new variation at 200px width
$thumb = $image->width(200);
~~~~~

@param int $n Optional width if you are creating a new size.

@param array|string|int|bool $options See `Pageimage::size()` $options argument for details.

@return int|Pageimage Returns width (in px) when given no arguments, or Pageimage when given a width argument.

## height()

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

## maxWidth()

Return an image no larger than the given width.

If source image is equal to or smaller than the requested dimension,
then it will remain that way and the source image is returned (not a copy).

If the source image is larger than the requested dimension, then a new copy
will be returned at the requested dimension.


@param int $n Maximum width

@param array $options See `Pageimage::size()` method for options

@return Pageimage

## maxHeight()

Return an image no larger than the given height.

If source image is equal to or smaller than the requested dimension,
then it will remain that way and the source image is returned (not a copy).

If the source image is larger than the requested dimension, then a new copy
will be returned at the requested dimension.


@param int $n Maximum height

@param array $options See `Pageimage::size()` method for options

@return Pageimage

## maxSize()

Return an image no larger than the given width and height


@param int $width Max allowed width

@param int $height Max allowed height

@param array $options See `Pageimage::size()` method for options, or these additional options:
 - `allowOriginal` (bool): Allow original image to be returned if already within max requested dimensions? (default=false)

@return Pageimage

## ratio()

Get ratio of width divided by height

@param int $precision Optionally specify a value >2 for custom precision (default=2) 3.0.211+

@return float

@since 3.0.154

## getVariations()

Get all size variations of this image

This is useful after a delete of an image (for example). This method can be used to track down all the
child files that also need to be deleted.


@param array $options Optional, one or more options in an associative array of the following:
	- `info` (bool): when true, method returns variation info arrays rather than Pageimage objects (default=false).
 - `verbose` (bool|int): Return verbose array of info. If false, returns only filenames (default=true).
    This option does nothing unless the `info` option is true. Also note that if verbose is false, then all options
    following this one no longer apply (since it is no longer returning width/height info).
    When integer 1, returned info array also includes Pageimage variation options in 'pageimage' index of
    returned arrays (since 3.0.137).
	- `width` (int): only variations with given width will be returned
	- `height` (int): only variations with given height will be returned
	- `width>=` (int): only variations with width greater than or equal to given will be returned
	- `height>=` (int): only variations with height greater than or equal to given will be returned
	- `width<=` (int): only variations with width less than or equal to given will be returned
	- `height<=` (int): only variations with height less than or equal to given will be returned
	- `suffix` (string): only variations having the given suffix will be returned
 - `suffixes` (array): only variations having one of the given suffixes will be returned
 - `noSuffix` (string): exclude variations having this suffix
 - `noSuffixes` (array): exclude variations having any of these suffixes
 - `name` (string): only variations containing this text in filename will be returned (case insensitive)
 - `noName` (string): only variations NOT containing this text in filename will be returned (case insensitive)
 - `regexName` (string): only variations that match this PCRE regex will be returned

@return Pageimages|array Returns Pageimages array of Pageimage instances.
 Only returns regular array if provided `$options['info']` is true.

## ___rebuildVariations()

Rebuilds variations of this image

By default, this excludes crops and images with suffixes, but can be overridden with the `$mode` and `$suffix` arguments.

**Options for $mode argument**

- `0` (int): Rebuild only non-suffix, non-crop variations, and those w/suffix specified in $suffix argument. ($suffix is INCLUSION list)
- `1` (int): Rebuild all non-suffix variations, and those w/suffix specifed in $suffix argument. ($suffix is INCLUSION list)
- `2` (int): Rebuild all variations, except those with suffix specified in $suffix argument. ($suffix is EXCLUSION list)
- `3` (int): Rebuild only variations specified in the $suffix argument. ($suffix is ONLY-INCLUSION list)
- `4` (int): Rebuild only non-proportional, non-crop variations (variations that specify both width and height)

Mode 0 is the only truly safe mode, as in any other mode there are possibilities that the resulting
rebuild of the variation may not be exactly what was intended. The issues with other modes primarily
arise when the suffix means something about the technical details of the produced image, or when
rebuilding variations that include crops from an original image that has since changed dimensions or crops.


@param int $mode See the options for $mode argument above (default=0).

@param array $suffix Optional argument to specify suffixes to include or exclude (according to $mode).

@param array $options See $options for `Pageimage::size()` for details.

@return array Returns an associative array with with the following indexes:
 - `rebuilt` (array): Names of files that were rebuilt.
 - `skipped` (array): Names of files that were skipped.
 - `errors` (array): Names of files that had errors.
 - `reasons` (array): Reasons why files were skipped or had errors, associative array indexed by file name.

## ___isVariation()

Given a file name (basename), return array of info if this is a variation for this instance’s file, or false if not.

Returned array includes the following indexes:

- `original` (string): Original basename
- `url` (string): URL to image
- `path` (string): Full path + filename to image
- `width` (int): Specified width in filename
- `height` (int): Specified height in filename
- `actualWidth` (int): Actual width when checked manually
- `actualHeight` (int): Acual height when checked manually
- `crop` (string): Cropping info string or blank if none
- `suffix` (array): Array of suffixes

The following are only present if variation is based on another variation, and thus has a parent variation
image between it and the original:

- `suffixAll` (array): Contains all suffixes including among parent variations
- `parent` (array): Variation info array of direct parent variation file


@param string $basename Filename to check (basename, which excludes path)

@param array|bool $options Array of options to modify behavior, or boolean to only specify `allowSelf` option.
 - `allowSelf` (bool): When true, it will return variation info even if same as current Pageimage. (default=false)
 - `verbose` (bool): Return verbose array of info? If false, just returns basename (string) or false. (default=true)

@return bool|string|array Returns false if not a variation, or array (verbose) or string (non-verbose) of info if it is.

## removeVariations()

Delete all the alternate sizes associated with this Pageimage


@param array $options See options for getVariations() method to limit what variations are removed, plus these:
 - `dryRun` (bool): Do not remove now and instead only return the filenames of variations that would be deleted (default=false).
 - `getFiles` (bool): Return deleted filenames? Also assumed if the test option is used (default=false).

@return PageImageVariations|array Returns $this by default, or array of deleted filenames if the `getFiles` option is specified

## ___createdVariation()

Hook called after successful creation of image variation

@param Pageimage $image The variation image that was created

@param array $data Verbose associative array of data used to create the variation

@since 3.0.180

## setOriginal()

Identify this Pageimage as a variation, by setting the Pageimage it was resized from.


@param Pageimage $image

@return $this

## getOriginal()

If this image is a variation, return the original, otherwise return null.


@return Pageimage|null

## ___render()

Render markup for this image (optionally using a provided markup template string and/or image size options)

Given template string can contain any of the placeholders, which will be replaced:
 - `{url}` or `{src}` Image URL (typically used for src attribute)
 - `{httpUrl}` File URL with scheme and hostname (alternate for src attribute)
 - `{URL}` Same as url but with cache busting query string
 - `{HTTPURL}` Same as httpUrl but with cache busting query string
 - `{description}` or `{alt}` Image description (typically used in alt attribute)
 - `{tags}` File tags (might be useful in class attribute)
 - `{width}` Width of image
 - `{height}` Height of image
 - `{hidpiWidth}` HiDPI width of image
 - `{hidpiHeight}` HiDPI height of image
 - `{ext}` File extension
 - `{original.name}` Replace “name” with any of the properties above to refer to original image.
    If there is no original image then these just refer back to the current image.

~~~~~
$image = $page->images->first();
if($image) {
  // default output
  echo $image->render();

  // custom output
  echo $image->render("<img class='pw-image' src='{url}' alt='{alt}'>");

  // custom output with options
  echo $image->render("<img src='{url}' alt='{alt}'>", [ 'width' => 300 ]);

  // options can go in first argument if you prefer
  echo $image->render([ 'width' => 300, 'height' => 200 ]);

  // if only width/height are needed, they can also be specified as a string (1st or 2nd arg)
  echo $image->render('300x200');

  // custom output with link to original/full-size and square crop of 300x300 for thumbnail
  echo $image->render([
    'markup' => "<a href='{original.url}'><img src='{url}' alt='{alt}'></a>",
    'width' => 300,
    'height' => 300
  ]);
}
~~~~~

@param string|array $markup Markup template string or optional $options array if you do not want the template string here.

@param array|string $options Optionally resize image with these options sent to size() method:
 - `width` (int): Target width or 0 for current image size (or proportional if height specified).
 - `height` (int): Target height or 0 for current image size (or proportional if width specified).
 - `markup` (string): Markup template string (same as $markup argument), or omit for default (same as $markup argument).
 - `link` (bool): Link image to original size? Though you may prefer to do this with your own $markup (see examples). (default=false)
 - `alt` (string): Text to use for “alt” attribute (default=text from image description).
 - `class` (string): Text to use for “class” attribute, if `{class}` present in markup (default='').
 - Plus any option available to the $options argument on the `Pageimage::size()` method.
 - If you only need width and/or height, you can specify a width x height string, i.e. 123x456 (use 0 for proportional).

@return string

@see Pageimages::render()

@since 3.0.126

## webp()

Get WebP "extra" version of this Pageimage

@param array $webpOptions Optionally override certain defaults from `$config->webpOptions` (requires 3.0.229+):
 - `useSrcUrlOnSize` (bool): Fallback to source file URL when webp file is larger than source? (default=true)
 - `useSrcUrlOnFail` (bool): Fallback to source file URL when webp file fails for some reason? (default=true)
 - `quality' (int): Quality setting of 1-100 where higher is better but larger in file size (default=90)
    Note that his quality setting is only used if the .webp file does not already exist.

@return PagefileExtra

@since 3.0.132

## rename()

Rename this file

Remember to follow this up with a `$page->save()` for the page that the file lives on.


@param string $basename New name to use. Must be just the file basename (no path).

@return string|bool Returns new name (basename) on success, or boolean false if rename failed.

## getFiles()

Get all filenames associated with this image

@return array

@since 3.0.233

## ___filenameDoesNotExist()

Hook called by the size() method when a source/original filename does not exist

For the return value, override the default `false` return value and set
it to `true` in order to make it continue as if the filename did exist,
such as if your hook copied a file to $filename.

@param string $filename

@return bool

@since 3.0.254

## __debugInfo()

Basic debug info

@return array

## getDebugInfo()

Verbose debug info (via @horst)

Optionally with individual options array.

@param array $options The individual options you also passes with your image variation creation

@param string $returnType 'string'|'array'|'object', default is 'string' and returns markup or plain text

@return array|object|string

@since 3.0.132
