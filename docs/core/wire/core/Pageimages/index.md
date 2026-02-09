# Pageimages

Source: `wire/core/Pageimages.php`

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

Groups:
Group: [other](group-other.md)

Methods:
Method: [add()](method-add.md)
Method: [getFile()](method-getfile.md)
Method: [getAllVariations()](method-getallvariations.md)
Method: [render()](method-___render.md) (hookable)
