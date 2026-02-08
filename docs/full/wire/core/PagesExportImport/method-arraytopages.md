# $pagesExportImport->arrayToPages(array $a, array $options = array()): PageArray|int

Source: `wire/core/PagesExportImport.php`

Import an array of page data to create or update pages

Provided array ($a) must originate from the pagesToArray() method format.

## Arguments

- array $a Array of import data
- array $options - `count` (bool):  Return count of imported pages, rather than PageArray? Reduces memory requirements. (default=false) - `pageArray` (PageArray): PageArray object to populate, or omit to return new PageArray (default=null)

## Return value

PageArray|int

## Throws

- WireException
