# Pageimages

Source: `wire/core/Pageimages.php`

Inherits: `Pagefiles`


Groups:
Group: [other](group-other.md)

ProcessWire Pageimages

Pageimages are a type of WireArray containing Pageimage objects. They represent the value of multi-image field in ProcessWire.

Most of the methods you are likely to use are inherited from `Pagefiles` and `WireArray` so be sure to take a look at those as well.
Pageimages is dedicated to containing `Pageimage` objects.

~~~~~
// Example of outputting a thumbnail gallery of Pageimage objects
foreach($page->images as $image) {
  // $page->images is a Pageimages object
  // $image and $thumb are both Pageimage objects
  $thumb = $image->size(200, 200);
  echo "<a href='$image->url'>";
  echo "<img src='$thumb->url' alt='$image->description' />";
  echo "</a>";
}
~~~~~

Typically a Pageimages object will be associated with a specific field attached to a Page.
There may be multiple instances of Pageimages attached to a given Page (depending on what fields are in it's fieldgroup).

Methods:
- [`add(Pageimage|string $item): Pageimages|Pagefiles`](method-add.md)
- [`getFile(string $name): null|Pagefile|Pageimage`](method-getfile.md)
- [`getAllVariations(): array`](method-getallvariations.md)
- [`render(string|array $markup = '', array|string $options = array()): string`](method-___render.md) (hookable)
