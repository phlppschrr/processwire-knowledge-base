# ProcessWire security: template files

Source: https://processwire.com/docs/security/template-files/

## Sections


## Security for template files in ProcessWire

While ProcessWire handles a lot of the common security considerations before your template files are even loaded, you should also follow security best practices within your template files as you would in any other PHP framework.

Your ProcessWire installation is only as secure as your template files. ProcessWire template files are PHP files, and anything that is possible in PHP is also possible in your template files.

If your template files deal with any kind of user input, they must sanitize and validate any user input. Never send any kind of user input directly to ProcessWire's API methods (other than those provided by [$sanitizer](/docs/start/variables/sanitizer/)) without first sanitizing it, and validating it where appropriate.

For example, here is something you don't want to do. This code block is sending the GET variable `$text` directly to a `$pages->find()` call, without sanitizing the value or even confirming that it was present:

```php
// do not do this
$text = $input->get('text');
$items = $pages->find("body%=$text");
```

Here is the same example as above, but with sanitization (for use in a selector string) and confirmation that the value is present before attempting to use it:

```php
$text = $sanitizer->selectorValue($input->get('text')); 
if($text) {
  $items = $pages->find("body%=$text");
}
```

This is only a single ProcessWire-specific example, but the scope of PHP best practices for handling user input is outside the scope of this document. When in doubt, ask in our forums. If dealing with user input, get familiar with ProcessWire's built-in [$sanitizer](/docs/start/variables/sanitizer/) as well as general [PHP data filtering and sanitization](http://www.phptherightway.com/#data_filtering) and other PHP security best practices, as your project scope and needs dictate.
