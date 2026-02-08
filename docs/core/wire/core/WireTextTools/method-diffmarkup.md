# WireTextTools::diffMarkup()

Source: `wire/core/WireTextTools.php`

Given two strings ($old and $new) return a diff string in HTML markup

@param string $old Old string value

@param string $new New string value

@param array $options Options to modify behavior:
 - `ins` (string) Markup to use for diff insertions (default: `<ins>{out}</ins>`)
 - `del` (string) Markup to use for diff deletions (default: `<del>{out}</del>`)
 - `entityEncode` (bool): Entity encode values, other than added ins/del tags? (default=true)
 - `split` (string): Regex used to split strings for parts to diff (default=`\s+`)

@return string

@since 3.0.144
