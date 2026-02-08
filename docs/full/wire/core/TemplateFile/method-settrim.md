# $templateFile->setTrim($trim)

Source: `wire/core/TemplateFile.php`

Set whether rendered output should have leading/trailing whitespace trimmed

By default whitespace is trimmed so you would call `$templateFile->setTrim(false);` to disable.

## Usage

~~~~~
// basic usage
$result = $templateFile->setTrim($trim);
~~~~~

## Arguments

- `$trim` `bool`

## Since

3.0.154
