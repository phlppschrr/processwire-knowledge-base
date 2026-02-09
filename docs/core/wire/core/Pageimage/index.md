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

- [`$url: string`](method-url.md) URL to the file on the server.
- `$httpUrl: string` URL to the file on the server including scheme and hostname.
- `$URL: string` Same as $url property but with browser cache busting query string appended.
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

Methods:
- [`__construct(Pagefiles $pagefiles, string $filename)`](method-__construct.md)
- [`url(): string`](method-url.md)
- [`filename(): string`](method-filename.md)
- [`suffix(string $s = ''): array|bool`](method-suffix.md)
- [`focus(null|float|int|array|false $top = null, null|float|int $left = null, null|int $zoom = null): array|bool|Pageimage`](method-focus.md)
- [`set(string $key, mixed $value): Pageimage|WireData`](method-set.md)
- [`size(int|string $width, int|array $height = 0, array|string|int $options = array()): Pageimage`](method-size.md)
- [`sizeName(string $name, array $options = array()): Pageimage`](method-sizename.md)
- [`crop(int $x, int $y, int $width, int $height, array $options = array()): Pageimage`](method-___crop.md) (hookable)
- [`width(int $n = 0, array|string|int|bool $options = array()): int|Pageimage`](method-width.md)
- [`height(int $n = 0, array|string|int|bool $options = array()): int|Pageimage`](method-height.md)
- [`maxWidth(int $n, array $options = array()): Pageimage`](method-maxwidth.md)
- [`maxHeight(int $n, array $options = array()): Pageimage`](method-maxheight.md)
- [`maxSize(int $width, int $height, array $options = array()): Pageimage`](method-maxsize.md)
- [`ratio(int $precision = 2): float`](method-ratio.md)
- [`getVariations(array $options = array()): Pageimages|array`](method-getvariations.md)
- [`rebuildVariations(int $mode = 0, array $suffix = array(), array $options = array()): array`](method-___rebuildvariations.md) (hookable)
- [`isVariation(string $basename, array|bool $options = array()): bool|string|array`](method-___isvariation.md) (hookable)
- [`removeVariations(array $options = array()): PageImageVariations|array`](method-removevariations.md)
- [`createdVariation(Pageimage $image, array $data)`](method-___createdvariation.md) (hookable)
- [`setOriginal(Pageimage $image): $this`](method-setoriginal.md)
- [`getOriginal(): Pageimage|null`](method-getoriginal.md)
- [`render(string|array $markup = '', array|string $options = array()): string`](method-___render.md) (hookable)
- [`webp(array $webpOptions = array()): PagefileExtra`](method-webp.md)
- [`rename(string $basename): string|bool`](method-rename.md)
- [`getFiles(): array`](method-getfiles.md)
- [`filenameDoesNotExist(string $filename): bool`](method-___filenamedoesnotexist.md) (hookable)
- [`__debugInfo(): array`](method-__debuginfo.md)
- [`getDebugInfo(array $options = array(), string $returnType = 'string'): array|object|string`](method-getdebuginfo.md)

Hookable methods
================

- [`isVariation($basename, $options = array()): bool|array`](method-___isvariation.md)
- [`crop($x, $y, $width, $height, $options = array()): Pageimage`](method-___crop.md)
- [`rebuildVariations($mode = 0, array $suffix = array(), array $options = array()): array`](method-___rebuildvariations.md)
- [`install($filename)()`](method-install-filename.md)
- `@method render($markup = '', $options = array())` render($markup = '', $options = array())
- [`createdVariation(Pageimage $image, array $data): void`](method-___createdvariation.md) Called after new image variation created (3.0.180+)
- [`filenameDoesNotExist($filename): bool`](method-___filenamedoesnotexist.md) Hook called when a filename does not exist
