# $comment->getFormattedCommentText(array $options = array()): string

Source: `wire/modules/Fieldtype/FieldtypeComments/Comment.php`

Get comment text as formatted string

Note that the default options behavior is to return comment text with paragraphs split by `</p><p>`
but without the first `<p>` and last `</p>` since it is assumed these will be the markup you wrap
the comment in. If you want it to include the wrapping `<p>…</p>` tags then specify true for the
`wrapParagraph` option in the `$options` argument.

## Arguments

- array $options - `useParagraphs` (bool): Convert newlines to paragraphs? (default=true) - `wrapParagraph` (bool): Use wrapping <p>…</p> tags around return value? (default=false) - `useLinebreaks` (bool): Convert single newlines to <br> tags? (default=true)

## Return value

string

## Meta

- @since 3.0.169
