# Pageimage

Source: `wire/core/Pageimage.php`

Inherits: `Pagefile`

## Summary

ProcessWire Pageimage

Common methods:
- [`url()`](method-url.md)
- [`filename()`](method-filename.md)
- [`suffix()`](method-suffix.md)
- [`focus()`](method-focus.md)
- [`set()`](method-set.md)

Groups:
Group: [resize-and-crop](group-resize-and-crop.md)
Group: [variations](group-variations.md)
Group: [other](group-other.md)

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



## Properties Inherited From Pagefile

- [`$url: string`](method-url.md) URL to the file on the server.
- `$httpUrl: string` URL to the file on the server including scheme and hostname.
- `$URL: string` Same as `$url` property but with browser cache busting query string appended.
- `$HTTPURL: string` Same as the cache-busting uppercase “URL” property, but includes scheme and hostname.
- [`$filename: string`](method-filename.md) Full disk path to the file on the server.
- `$name: string` Returns the filename without the path, same as the "basename" property.
- `$hash: string` Get a unique hash (for the page) representing this Pagefile.
- `$tagsArray: array` Get file tags as an array. @since 3.0.17
- `$basename: string` Returns the filename without the path.
- `$description: string` Value of the file’s description field (string), if enabled. Note you can also set this property directly.
- `$tags: string` Value of the file’s tags field (string), if enabled.
- `$ext: string` File’s extension (i.e. last 3 or so characters)
- `$filesize: int` File size (number of bytes).
- `$modified: int` Unix timestamp of when Pagefile (file, description or tags) was last modified.
- `$modifiedStr: string` Readable date/time string of when Pagefile was last modified.
- `$mtime: int` Unix timestamp of when file (only) was last modified.
- `$mtimeStr: string` Readable date/time string when file (only) was last modified.
- `$created: int` Unix timestamp of when file was created.
- `$createdStr: string` Readable date/time string of when Pagefile was created
- `$filesizeStr: string` File size as a formatted string, i.e. “123 Kb”.
- `$pagefiles: Pagefiles` The Pagefiles WireArray that contains this file.
- `$page: Page` The Page object that this file is part of.
- `$field: Field` The Field object that this file is part of.
- `$debugInfo: PageimageDebugInfo`

## Hookable Methods

- [`isVariation($basename, $options = array()): bool|array`](method-___isvariation.md)
- [`crop($x, $y, $width, $height, $options = array()): Pageimage`](method-___crop.md)
- [`rebuildVariations($mode = 0, array $suffix = array(), array $options = array()): array`](method-___rebuildvariations.md)
- `install($filename)`
- [`render($markup = '', $options = array())`](method-___render.md)
- [`createdVariation(Pageimage $image, array $data): void`](method-___createdvariation.md) Called after new image variation created (3.0.180+)
- [`filenameDoesNotExist($filename): bool`](method-___filenamedoesnotexist.md) Hook called when a filename does not exist

## Methods
- [`__construct(Pagefiles $pagefiles, string $filename)`](method-__construct.md) Construct a new Pageimage
- [`url(): string`](method-url.md) Return the web accessible URL to this image file
- [`filename(): string`](method-filename.md) Returns the full disk path to the image file
- [`suffix(string $s = ''): array|bool`](method-suffix.md) Returns array of suffixes for this file, or true/false if this file has the given suffix.
- [`focus(null|float|int|array|false $top = null, null|float|int $left = null, null|int $zoom = null): array|bool|Pageimage`](method-focus.md) Get or set focus area for crops to use
- [`set(string $key, mixed $value): Pageimage|WireData`](method-set.md) Set property
- [`size(int|string $width, int|array $height = 0, array|string|int $options = array()): Pageimage`](method-size.md) Return an image (Pageimage) sized/cropped to the specified dimensions.
- [`sizeName(string $name, array $options = array()): Pageimage`](method-sizename.md) Return image of size indicated by predefined setting
- [`crop(int $x, int $y, int $width, int $height, array $options = array()): Pageimage`](method-___crop.md) (hookable) Create a crop and return it as a new Pageimage.
- [`width(int $n = 0, array|string|int|bool $options = array()): int|Pageimage`](method-width.md) Return the width of this image OR return an image sized with a given width (and proportional height).
- [`height(int $n = 0, array|string|int|bool $options = array()): int|Pageimage`](method-height.md) Return the height of this image OR return an image sized with a given height (and proportional width).
- [`maxWidth(int $n, array $options = array()): Pageimage`](method-maxwidth.md) Return an image no larger than the given width.
- [`maxHeight(int $n, array $options = array()): Pageimage`](method-maxheight.md) Return an image no larger than the given height.
- [`maxSize(int $width, int $height, array $options = array()): Pageimage`](method-maxsize.md) Return an image no larger than the given width and height
- [`ratio(int $precision = 2): float`](method-ratio.md) Get ratio of width divided by height
- [`getVariations(array $options = array()): Pageimages|array`](method-getvariations.md) Get all size variations of this image
- [`rebuildVariations(int $mode = 0, array $suffix = array(), array $options = array()): array`](method-___rebuildvariations.md) (hookable) Rebuilds variations of this image
- [`isVariation(string $basename, array|bool $options = array()): bool|string|array`](method-___isvariation.md) (hookable) Given a file name (basename), return array of info if this is a variation for this instance’s file, or false if not.
- [`removeVariations(array $options = array()): PageImageVariations|array`](method-removevariations.md) Delete all the alternate sizes associated with this Pageimage
- [`createdVariation(Pageimage $image, array $data)`](method-___createdvariation.md) (hookable) Hook called after successful creation of image variation
- [`setOriginal(Pageimage $image): $this`](method-setoriginal.md) Identify this Pageimage as a variation, by setting the Pageimage it was resized from.
- [`getOriginal(): Pageimage|null`](method-getoriginal.md) If this image is a variation, return the original, otherwise return null.
- [`render(string|array $markup = '', array|string $options = array()): string`](method-___render.md) (hookable) Render markup for this image (optionally using a provided markup template string and/or image size options)
- [`webp(array $webpOptions = array()): PagefileExtra`](method-webp.md) Get WebP "extra" version of this Pageimage
- [`rename(string $basename): string|bool`](method-rename.md) Rename this file
- [`getFiles(): array`](method-getfiles.md) Get all filenames associated with this image
- [`filenameDoesNotExist(string $filename): bool`](method-___filenamedoesnotexist.md) (hookable) Hook called by the size() method when a source/original filename does not exist
- [`__debugInfo(): array`](method-__debuginfo.md) Basic debug info
- [`getDebugInfo(array $options = array(), string $returnType = 'string'): array|object|string`](method-getdebuginfo.md) Verbose debug info (via @horst)
