# $pageimage->__construct(Pagefiles $pagefiles, $filename)

Source: `wire/core/Pageimage.php`

Construct a new Pageimage

~~~~~
// Construct a new Pageimage, assumes that $page->images is a FieldtypeImage Field
$pageimage = new Pageimage($page->images, '/path/to/file.png');
~~~~~

## Arguments

- `$pagefiles` `Pagefiles`
- `$filename` `string` Full path and filename to this pagefile

## Throws

- WireException
