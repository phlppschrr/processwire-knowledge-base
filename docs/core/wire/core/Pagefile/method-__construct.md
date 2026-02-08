# Pagefile::__construct()

Source: `wire/core/Pagefile.php`

Construct a new Pagefile

~~~~~
// Construct a new Pagefile, assumes that $page->files is a FieldtypeFile Field
$pagefile = new Pagefile($page->files, '/path/to/file.pdf');
~~~~~

@param Pagefiles $pagefiles The Pagefiles WireArray that will contain this file.

@param string $filename Full path and filename to this Pagefile.
