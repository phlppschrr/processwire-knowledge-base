# $pageimage->__construct(Pagefiles $pagefiles, $filename)

Source: `wire/core/Pageimage.php`

Construct a new Pageimage

## Example

~~~~~
// Construct a new Pageimage, assumes that $page->images is a FieldtypeImage Field
$pageimage = new Pageimage($page->images, '/path/to/file.png');
~~~~~

## Usage

~~~~~
// basic usage
$result = $pageimage->__construct($pagefiles, $filename);

// usage with all arguments
$result = $pageimage->__construct(Pagefiles $pagefiles, $filename);
~~~~~

## Arguments

- `$pagefiles` `Pagefiles`
- `$filename` `string` Full path and filename to this pagefile

## Exceptions

- `WireException`
