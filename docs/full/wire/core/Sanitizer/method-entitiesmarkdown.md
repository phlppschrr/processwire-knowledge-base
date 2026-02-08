# $sanitizer->entitiesMarkdown($str, $options = array()): string

Source: `wire/core/Sanitizer.php`

Entity encode while translating some markdown tags to HTML equivalents

If you specify boolean TRUE for the `$options` argument, full markdown is applied. Otherwise,
only basic markdown allowed, as outlined in the examples.

The primary reason to use this over full-on Markdown is that it has less overhead
and is faster then full-blown Markdown, for when you don't need it. It's also safer
for text coming from user input since it doesn't allow any other HTML. But if you just
want full markdown, then specify TRUE for the `$options` argument.

Basic allowed markdown currently includes:
- `**strong**`
- `*emphasis*`
- `[anchor-text](url)`
- `~~strikethrough~~`
- code surrounded by backticks

## Example

~~~~~
// basic markdown
echo $sanitizer->entitiesMarkdown($str);

// full markdown
echo $sanitizer->entitiesMarkdown($str, true);
~~~~~

## Usage

~~~~~
// basic usage
$string = $sanitizer->entitiesMarkdown($str);

// usage with all arguments
$string = $sanitizer->entitiesMarkdown($str, $options = array());
~~~~~

## Arguments

- `$str` `string` String to apply markdown to
- `$options` (optional) `array|bool|int` Options include the following, or specify boolean TRUE to apply full markdown. - `fullMarkdown` (bool): Use full markdown rather than basic? (default=false) when true, most options no longer apply. Note: A markdown flavor integer may also be supplied for the fullMarkdown option. - `flags` (int): PHP htmlentities() flags. Default is ENT_QUOTES. - `encoding` (string): PHP encoding type. Default is 'UTF-8'. - `doubleEncode` (bool): Whether to double encode (if already encoded). Default is true. - `allow` (array): Only markdown that translates to these tags will be allowed. Default is most inline HTML tags. - `disallow` (array): Specified tags (in the default allow list) that won't be allowed. Default=[] empty array. (Note: The 'disallow' is an alternative to the default 'allow'. No point in using them both.) - `linkMarkup` (string): Markup to use for links. Default=`<a href="{url}" rel="nofollow" target="_blank">{text}</a>`. - `allowBrackets` (bool): Allow some inline-level bracket tags, i.e. `[span.detail]text[/span]` ? (default=false)

## Return value

- `string` Formatted with a flavor of markdown
