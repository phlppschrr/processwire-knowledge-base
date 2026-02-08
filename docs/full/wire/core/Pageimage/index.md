# Pageimage

Source: `wire/core/Pageimage.php`

ProcessWire Pageimage

Represents an image item attached to a page, typically via an Image Fieldtype.
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

Groups:
Group: [resize-and-crop](group-resize-and-crop.md)
Group: [variations](group-variations.md)
Group: [other](group-other.md)

Methods:
Method: [__construct()](method-__construct.md)
Method: [url()](method-url.md)
Method: [filename()](method-filename.md)
Method: [suffix()](method-suffix.md)
Method: [focus()](method-focus.md)
Method: [set()](method-set.md)
Method: [size()](method-size.md)
Method: [sizeName()](method-sizename.md)
Method: [crop()](method-___crop.md) (hookable)
Method: [width()](method-width.md)
Method: [height()](method-height.md)
Method: [maxWidth()](method-maxwidth.md)
Method: [maxHeight()](method-maxheight.md)
Method: [maxSize()](method-maxsize.md)
Method: [ratio()](method-ratio.md)
Method: [getVariations()](method-getvariations.md)
Method: [rebuildVariations()](method-___rebuildvariations.md) (hookable)
Method: [isVariation()](method-___isvariation.md) (hookable)
Method: [removeVariations()](method-removevariations.md)
Method: [createdVariation()](method-___createdvariation.md) (hookable)
Method: [setOriginal()](method-setoriginal.md)
Method: [getOriginal()](method-getoriginal.md)
Method: [render()](method-___render.md) (hookable)
Method: [webp()](method-webp.md)
Method: [rename()](method-rename.md)
Method: [getFiles()](method-getfiles.md)
Method: [filenameDoesNotExist()](method-___filenamedoesnotexist.md) (hookable)
Method: [__debugInfo()](method-__debuginfo.md)
Method: [getDebugInfo()](method-getdebuginfo.md)
