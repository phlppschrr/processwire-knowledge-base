# $pagesRawFinder->findReferences(array $colNames)

Source: `wire/core/PagesRaw.php`

Populate a 'references' to the raw results that includes other pages referencing the found ones

To use this specify `references` in the fields to return. Or, to get page references that are
indexed by field name, specify `references.field` instead. To get something more than the id
of page references, specify properties or fields as `references.field_name` replacing `field_name`
with a page property or field name, i.e. `references.title`.

## Arguments

- `$colNames` `array`

## Since

3.0.193
