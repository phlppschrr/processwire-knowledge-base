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

ProcessWire 3.x, Copyright 2019 by Ryan Cramer
https://processwire.com

## other

@method string render($markup = '', $options = array())

## add()

Add a new Pageimage item, or create one from given filename and add it.

@param Pageimage|string $item If item is a string (filename) then the Pageimage instance will be created automatically.

@return Pageimages|Pagefiles

## getFile()

Does this field have the given file name? If so, return it, if not return null.

@param string $name Basename is assumed

@return null|Pagefile|Pageimage Returns Pagefile object if found, null if not

## getAllVariations()

Get an array of all image variations on this field indexed by original file name.

More information on any variation filename can be retrieved from `Pageimage::isVariation()`.

~~~~~
$variations = $page->images->getAllVariations();
print_r($variations);
// Example output:
// array(
//   'foo.jpg' => array(
//      'foo.100x100.jpg',
//      'foo.200x200.jpg'
//   ),
//   'bar.jpg' => array(
//      'bar.300x300.jpg'
//   )
// );
~~~~~

@return array Array indexed by file name, each containing array of variation file names

@see Pageimage::isVariation()

## ___render()

Render markup for all images here (optionally using a provided markup template string and/or image size options)

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
 - `{original.name}` Replace “name” with any of the properties above to refer to original/full-size image.
    If there is no original image then these just refer back to the current image.

~~~~~
// default output
echo $page->images->render();

// custom output
echo $page->images->render("<img class='pw-image' src='{url}' alt='{alt}'>");

// custom output with options
echo $page->images->render("<img src='{url}' alt='{alt}'>", [ 'width' => 300 ]);

// options can go in first argument if you prefer
echo $page->images->render([ 'width' => 300, 'height' => 200 ]);

// if only width/height are needed, they can also be specified as a string (1st or 2nd arg)
echo $page->images->render('300x200');

// custom output with link to original/full-size and square crop of 300x300 for thumbnails
echo "<ul>" . $page->images->render([
  'markup' => "<li><a href='{original.url}'><img src='{url}' alt='{alt}'></a></li>",
  'width' => 300,
  'height' => 300
]) . "</ul>";
~~~~~

@param string|array $markup Markup template string or optional $options array if you do not want the template string here.

@param array|string $options Optionally resize image with these options sent to size() method:
 - `width` (int): Target width or 0 for current image size (or proportional if height specified).
 - `height` (int): Target height or 0 for current image size (or proportional if width specified).
 - `markup` (string): Markup template string (same as $markup argument), or omit for default (same as $markup argument).
 - `link` (bool): Link image to original size? Though you may prefer to do this with your own $markup (see examples). (default=false)
 - `limit` (int): Render no more than this many images (default=0, no limit).
 - Plus any option available to the $options argument on the `Pageimage::size()` method.
 - If you only need width and/or height, you can specify a width x height string, i.e. 123x456 (use 0 for proportional).

@return string

@since 3.0.126
