# Inputfield::entityEncode()

Source: `wire/core/Inputfield.php`

Entity encode a string with optional Markdown support.

- Markdown support provided with second argument.
- If string is already entity-encoded it will first be decoded.


@param string $str String to encode

@param bool|int $markdown Optionally specify one of the following:
  - `true` (boolean): To allow Markdown using default "textFormat" setting (which is basic Markdown by default).
  - `false` (boolean): To disallow Markdown support (this is the default when $markdown argument omitted).
  - `Inputfield::textFormatNone` (constant): Disallow Markdown support (default).
  - `Inputfield::textFormatBasic` (constant): To support basic/inline Markdown.
  - `Inputfield::textFormatMarkdown` (constant): To support full Markdown and HTML.

@return string Entity encoded string or HTML string
