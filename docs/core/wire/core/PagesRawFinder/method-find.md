# PagesRawFinder::find()

Source: `wire/core/PagesRaw.php`

Find pages and return raw data from them in a PHP array

How to use the `$field` argument:

- If you provide an array for $field then it will return an array for each page, indexed by
  the field names you requested.

- If you provide a string (field name) or Field object, then it will return an array with
  the values of the 'data' column of that field.

- You may request field name(s) like `field.subfield` to retrieve a specific column/subfield.

- You may request field name(s) like `field.*` to return all columns/subfields for `field`,
  in this case, an associative array value will be returned for each page.

- If you specify an associative array for the $field argument, you can optionally rename
  fields in returned value. For example, if you wanted to get the 'title' field but return
  it as a field named 'headline' in the return value, you would specify the array
  `[ 'title' => 'headline' ]` for the $field argument. (3.0.176+)

@param string|array|Selectors $selector

@param string|Field|int|array $field Field/property name or array of of them

@param array $options See options for Pages::find

@return array

@since 3.0.172
