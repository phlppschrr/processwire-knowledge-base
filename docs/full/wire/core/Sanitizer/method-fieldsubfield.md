# $sanitizer->fieldSubfield($value, $limit = 1): string

Source: `wire/core/Sanitizer.php`

Sanitize as a field name but with optional subfield(s) like “field.subfield”

- Periods must be present to indicate subfield(s), otherwise behaves same as fieldName() sanitizer.
- By default allows just one subfield. To allow more, increase the $limit argument.
- To allow any quantity of subfields, specify -1.
- To reduce a `field.subfield...` combo to just `field` specify 0 for limit argument.
- Maximum length of returned string is (128 + ($limit * 128)).

~~~~~~
echo $sanitizer->fieldSubfield('a.b.c'); // outputs: a.b (default behavior)
echo $sanitizer->fieldSubfield('a.b.c', 2); // outputs: a.b.c
echo $sanitizer->fieldSubfield('a.b.c', 0); // outputs: a
echo $sanitizer->fieldSubfield('a.b.c', -1); // outputs: a.b.c (any quantity)
echo $sanitizer->fieldSubfield('foo bar.baz'); // outputs: foo_bar.baz
echo $sanitizer->fieldSubfield('foo bar baz'); // outputs: foo_bar_baz
~~~~~~

## Arguments

- `$value` `string` Value to sanitize
- `$limit` (optional) `int` Max allowed quantity of subfields, or use -1 for any quantity (default=1).

## Return value

string

## Since

3.0.126
