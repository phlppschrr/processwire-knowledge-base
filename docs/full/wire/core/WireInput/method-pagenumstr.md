# $wireInput->pageNumStr($pageNum = 0): string

Source: `wire/core/WireInput.php`

Return the string that represents the page number URL segment

Returns blank when page number is 1, since page 1 is assumed when no pagination number present in URL.

This is the string that gets appended to the URL and typically looks like `page123`,
but can be changed by modifying the `$config->pageNumUrlPrefix` setting, or specifying
language-specific page number settings in the LanguageSupportPageNames module.

## Usage

~~~~~
// basic usage
$string = $wireInput->pageNumStr();

// usage with all arguments
$string = $wireInput->pageNumStr($pageNum = 0);
~~~~~

## Arguments

- `$pageNum` (optional) `int` Optionally specify page number to use (default=0, which means use current page number)

## Return value

- `string`

## Since

3.0.106
