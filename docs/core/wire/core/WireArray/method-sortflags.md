# $wireArray->sortFlags($sortFlags = false): int

Source: `wire/core/WireArray.php`

Get or set sort flags that affect behavior of any sorting functions

The following constants may be used when setting the sort flags:

- `SORT_REGULAR` compare items normally (don’t change types)
- `SORT_NUMERIC` compare items numerically
- `SORT_STRING` compare items as strings
- `SORT_LOCALE_STRING` compare items as strings, based on the current locale
- `SORT_NATURAL` compare items as strings using “natural ordering” like natsort()
- `SORT_FLAG_CASE` can be combined (bitwise OR) with SORT_STRING or SORT_NATURAL to sort strings case-insensitively
- `SORT_APPEND_NULLS` can be used on its own or combined with any of above (bitwise OR) to specify that null
   or blank values should be treated as unsortable and appended to the end of the sortable set rather than sorted as
   blank values. This duplicates the behavior prior to 3.0.194 (available only in 3.0.194+). Note that this flag
   is unique to ProcessWire only and is not in PHP.

For more details, see `$sort_flags` argument at: https://www.php.net/manual/en/function.sort.php

## Arguments

- `$sortFlags` (optional) `bool` Optionally specify flag(s) to set

## Return value

int Returns current flags

## Since

3.0.129
