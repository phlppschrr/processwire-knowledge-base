# $pagefile->__construct(Pagefiles $pagefiles, $filename)

Source: `wire/core/Pagefile.php`

Construct a new Pagefile

~~~~~
// Construct a new Pagefile, assumes that $page->files is a FieldtypeFile Field
$pagefile = new Pagefile($page->files, '/path/to/file.pdf');
~~~~~

## Arguments

- Pagefiles $pagefiles The Pagefiles WireArray that will contain this file.
- string $filename Full path and filename to this Pagefile.
