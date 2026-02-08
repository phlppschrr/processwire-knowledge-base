# $wireTextTools->diffMarkup($old, $new, array $options = array()): string

Source: `wire/core/WireTextTools.php`

Given two strings ($old and $new) return a diff string in HTML markup

## Arguments

- `$old` `string` Old string value
- `$new` `string` New string value
- `$options` (optional) `array` Options to modify behavior: - `ins` (string) Markup to use for diff insertions (default: `<ins>{out}</ins>`) - `del` (string) Markup to use for diff deletions (default: `<del>{out}</del>`) - `entityEncode` (bool): Entity encode values, other than added ins/del tags? (default=true) - `split` (string): Regex used to split strings for parts to diff (default=`\s+`)

## Return value

string

## Since

3.0.144
