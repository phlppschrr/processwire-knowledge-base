# Pageimage::__construct()

Source: `wire/core/Pageimage.php`

Construct a new Pageimage

~~~~~
// Construct a new Pageimage, assumes that $page->images is a FieldtypeImage Field
$pageimage = new Pageimage($page->images, '/path/to/file.png');
~~~~~

@param Pagefiles $pagefiles

@param string $filename Full path and filename to this pagefile

@throws WireException
