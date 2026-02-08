# $sanitizer->url($value, $options = array()): string

Source: `wire/core/Sanitizer.php`

Sanitize and validate given URL or return blank if it can’t be made valid

- Performs some basic sanitization like adding a scheme to the front if it's missing, but leaves alone local/relative URLs.
- URL is not required to conform to ProcessWire conventions unless a relative path is given.
- Please note that URLs should always be entity encoded in your output. Many evil things are technically allowed in a valid URL,
  so your output should always entity encoded any URLs that came from user input.

~~~~~~
$url = $sanitizer->url('processwire.com/api/');
echo $sanitizer->entities($url); // outputs: http://processwire.com/api/
~~~~~~

## Arguments

- `$value` `string` URL to validate
- `$options` (optional) `bool|array` Array of options to modify default behavior, including: - `allowRelative` (boolean): Whether to allow relative URLs, i.e. those without domains (default=true). - `allowIDN` (boolean): Whether to allow internationalized domain names (default=false). - `allowQuerystring` (boolean): Whether to allow query strings (default=true). - `allowSchemes` (array): Array of allowed schemes, lowercase (default=[] any). - `disallowSchemes` (array): Array of disallowed schemes, lowercase (default=['file']). - `requireScheme` (bool): Specify true to require a scheme in the URL, if one not present, it will be added to non-relative URLs (default=true). - `convertEncoded` (boolean): Convert most encoded hex characters characters (i.e. “%2F”) to non-encoded? (default=true) - `encodeSpace` (boolean): Encoded space to “%20” or allow “%20“ in URL? Only useful if convertEncoded is true. (default=false) - `stripTags` (bool): Specify false to prevent tags from being stripped (default=true). - `stripQuotes` (bool): Specify false to prevent quotes from being stripped (default=true). - `maxLength` (int): Maximum length in bytes allowed for URLs (default=4096). - `throw` (bool): Throw exceptions on invalid URLs (default=false).

## Return value

string Returns a valid URL or blank string if it can’t be made valid.

## Throws

- WireException on invalid URLs, only if `$options['throw']` is true.
