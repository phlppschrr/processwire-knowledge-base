# $pagefile->__construct(Pagefiles $pagefiles, $filename)

Source: `wire/core/Pagefile.php`

Construct a new Pagefile

## Example

~~~~~
// Construct a new Pagefile, assumes that $page->files is a FieldtypeFile Field
$pagefile = new Pagefile($page->files, '/path/to/file.pdf');
~~~~~

## Usage

~~~~~
// basic usage
$result = $pagefile->__construct($pagefiles, $filename);

// usage with all arguments
$result = $pagefile->__construct(Pagefiles $pagefiles, $filename);
~~~~~

## Arguments

- `$pagefiles` `Pagefiles` The Pagefiles WireArray that will contain this file.
- `$filename` `string` Full path and filename to this Pagefile.
