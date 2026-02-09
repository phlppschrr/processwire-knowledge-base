# Pageimage

Source: `wire/core/Pageimage.php`

Inherits: `Pagefile`


Groups:
Group: [resize-and-crop](group-resize-and-crop.md)
Group: [variations](group-variations.md)
Group: [other](group-other.md)

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



Properties inherited from Pagefile
==================================

- [$url: string](method-url.md) URL to the file on the server.
- $httpUrl: string URL to the file on the server including scheme and hostname.
- $URL: string Same as $url property but with browser cache busting query string appended.
- $HTTPURL: string Same as the cache-busting uppercase “URL” property, but includes scheme and hostname.
- [$filename: string](method-filename.md) Full disk path to the file on the server.
- $name: string Returns the filename without the path, same as the "basename" property.
- $hash: string Get a unique hash (for the page) representing this Pagefile.
- $tagsArray: array Get file tags as an array. @since 3.0.17
- $basename: string Returns the filename without the path.
- $description: string Value of the file’s description field (string), if enabled. Note you can also set this property directly.
- $tags: string Value of the file’s tags field (string), if enabled.
- $ext: string File’s extension (i.e. last 3 or so characters)
- $filesize: int File size (number of bytes).
- $modified: int Unix timestamp of when Pagefile (file, description or tags) was last modified.
- $modifiedStr: string Readable date/time string of when Pagefile was last modified.
- $mtime: int Unix timestamp of when file (only) was last modified.
- $mtimeStr: string Readable date/time string when file (only) was last modified.
- $created: int Unix timestamp of when file was created.
- $createdStr: string Readable date/time string of when Pagefile was created
- $filesizeStr: string File size as a formatted string, i.e. “123 Kb”.
- $pagefiles: Pagefiles The Pagefiles WireArray that contains this file.
- $page: Page The Page object that this file is part of.
- $field: Field The Field object that this file is part of.
- $debugInfo: PageimageDebugInfo

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

Hookable methods
================

- [isVariation($basename, $options = array()): bool|array](method-___isvariation.md)
- [crop($x, $y, $width, $height, $options = array()): Pageimage](method-___crop.md)
- [rebuildVariations($mode = 0, array $suffix = array(), array $options = array()): array](method-___rebuildvariations.md)
- [install($filename)()](method-install-filename.md)
- @method render($markup = '', $options = array()) render($markup = '', $options = array())
- [createdVariation(Pageimage $image, array $data): void](method-___createdvariation.md) Called after new image variation created (3.0.180+)
- [filenameDoesNotExist($filename): bool](method-___filenamedoesnotexist.md) Hook called when a filename does not exist
