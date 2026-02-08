# $pageValues->getFieldValue(Page $page, $key, $selector = ''): null|mixed

Source: `wire/core/PageValues.php`

Get the value for a non-native page field, and call upon Fieldtype to join it if not autojoined

## Arguments

- string $key Name of field to get
- string $selector Optional selector to filter load by... ...or, if not in selector format, it becomes an __invoke() argument for object values .

## Return value

null|mixed
