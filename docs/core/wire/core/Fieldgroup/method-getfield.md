# Fieldgroup::getField()

Source: `wire/core/Fieldgroup.php`

Get a field that is part of this fieldgroup

Same as `Fieldgroup::get()` except that it only checks fields, not other properties of a fieldgroup.
Meaning, this is the preferred way to retrieve a Field from a Fieldgroup.


@param string|int|Field $key Field object, name or id.

@param bool|string $useFieldgroupContext Optionally specify one of the following (default=false):
  - `true` (boolean) Returned Field will be a clone of the original with context data set.
  - Specify a namespace (string) to retrieve context within that namespace.

@return Field|null Field object when present in this Fieldgroup, or null if not.
