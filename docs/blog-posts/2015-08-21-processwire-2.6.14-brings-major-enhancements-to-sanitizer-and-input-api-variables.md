# ProcessWire 2.6.14 brings major enhancements to $sanitizer and $input API variables

Source: https://processwire.com/blog/posts/processwire-2.6.14-brings-major-enhancements-to-sanitizer-and-input-api-variables/

## Sections


## ProcessWire 2.6.14 brings major enhancements to $sanitizer and $input API variables

21 August 2015 by Ryan Cramer [ 2 Comments](/blog/posts/processwire-2.6.14-brings-major-enhancements-to-sanitizer-and-input-api-variables/#comments)


## ProcessWire 2.6.14

This week's version makes some nice improvements to the API side of ProcessWire, particularly with regard to ease of input sanitization. This version also includes several tweaks and fixes reported on GitHub and the forums–thanks to all of you that are participating in making ProcessWire the best that it can be. We hope that you have a great weekend and week ahead, and remember to visit the [ProcessWire weekly](http://weekly.pw) this weekend and [subscribe](/contact/subscribe/) to our emails if you'd like.


### $sanitizer and $input are now a couple

Lets face it, user input should always be considered dirty, and you've always got to sanitize anything you get from it, whether from $input->get, $input->post, their PHP equivalents, or anywhere input comes into the system. Of course, this is true of all user input–it's the grimy part of our job as web developers, but also one of the most important. The simpler and more bulletproof we can make it, the better.

I've always thought we needed better communication between our `$sanitizer` and `$input` API variables, which are two separate things. You retrieve input from GET or POST variables via `$input->get` and `$input->post`, and you sanitize values with $sanitizer. They are separate classes and separate method calls. That's relatively simple, but it's also more verbose and prone to error than it needs to be. When you sanitize input, you are usually writing API code like this (using the pageName sanitizer just as an example):

```
$dirtyValue = $input->post('var_name');
$cleanValue = $sanitizer->pageName($dirtyValue);
```

This works perfectly well, but wouldn't it be nice if you could just retrieve sanitized values directly from $input? In ProcessWire 2.6.14+ you can now do this:

```
$cleanValue = $input->post->pageName('var_name');
```

The `$input` and `$sanitizer` work together with just one method call. The `$input->post`, `$input->get`, and `$input->cookie` properties of `$input` will now accept any `$sanitizer` method call. You only need to supply the name of the variable you want to retrieve from input, and it will do the rest.

If the `$sanitizer` method call accepts additional arguments, you can specify them as well. For instance, the following would accept input from a POST variable name start_date, in any recognized format, and return a string with that date in ISO-8601 format (i.e. 2015-08-21):

```
$cleanValue = $input->post->date('start_date', 'Y-m-d');
```

For more details about all the methods that you can call for sanitization, see the [Sanitizer documentation page](../api-full/wire/core/Sanitizer/index.md). We'll also be updating the `$input` documentation page once this feature makes its way to the master branch.


### Finding love at last, $sanitizer is now rocking a bunch of new skills

Now that `$input` and `$sanitizer` are a happy couple, it made sense to add several new Sanitizer methods to cover common input sanitization scenarios. This enables greater consistency in code, so that you can sanitize most input in the same way. This is preferable to using sanitizer for some things, typecasting for other things, and perhaps some other PHP functions for yet others. Now you should be able to accommodate most input sanitization with methods provided by `$sanitizer`, making it a more complete solution than it was before. Though please let us know if you think we are missing anything important here and we'll be glad to continue expanding it where appropriate.

Following are just the new methods added in 2.6.14, this is in addition to all the existing [sanitizer methods](../api-full/wire/core/Sanitizer/index.md).

|  |  |
| --- | --- |
| `$sanitizer->string($value)` | Sanitize value to string. Note that this makes no assumptions about what is a "safe" string, so you should always apply another sanitizer to it. This method is primarily used internally by the Sanitizer class methods that require a string, and you may also find it handy for the same purpose. Unlike string typecasting in PHP, this method won't fail in scenarios where PHP can't convert a value to a string. |
| `$sanitizer->string($value, 'name')` | Same as above, except applies a secondary sanitizer 'name' to the returned value. The 'name' can be any sanitizer method name. Perhaps it goes without saying, but make sure that 'name' is not coming from user input. |
| `$sanitizer->date($value)` | Sanitize a date or date/time string, making sure it is valid, and return a unix timestamp. |
| `$sanitizer->date($value, $format)` | Same as above, but returns the date in the given PHP date(), strftime() or wireDate() format (string) rather than a unix timestamp. Note: you may also provide a 3rd array `$options` argument for more options–see the phpdoc with the method for full details. |
| `$sanitizer->match($value, $regex)` | Validate that `$value` matches `$regex` pattern. If it does, value is returned. If not, blank is returned. The `$regex` pattern can be any valid PCRE regular expression. |
| `$sanitizer->int($value)` | Sanitized an integer (unsigned, unless you specify a negative minimum value: see `$options` in next row) |
| `$sanitizer->int($value, $options)` | Same as above, but with an extra `$options` array that you provide, containing one or more of the following properties: "min" (int) containing the minimum allowed value; "max" (int) containing the maximum allowed value; "blankValue" (mixed) containing the value you want to substitute rather than "0" as a blank value (null or blank string, for example). |
| `$sanitizer->intUnsigned($value)` | Sanitize to unsigned (0 or positive) integer. Behavior is the same as the int() method above with no options. You may also specify an `$options` array as the second argument. See the int() method for details. |
| `$sanitizer->intSigned($value)` | Sanitize to signed integer (negative or positive). You may also specify an `$options` array as the second argument. See the int() method for details. |
| `$sanitizer->float($value)` | Sanitize to floating point value. Unlike PHP float typecasting, this method can translate any international floating point format to a PHP float value. |
| `$sanitizer->float($value, $options)` | Same as above, but with an `$options` array to modify behavior, containing one or more of the following: "precision" (int) containing the number of digits to round to; "mode" (int) containing a PHP round constant with default being PHP_ROUND_HALF_UP; "blankValue" (mixed) containing the value to return when given a null or blank string (default=0.0); "min" (float) containing the minimum value you allow; "max" (float) containing the maximum value you allow. |
| `$sanitizer->array($value)` | Sanitize array or CSV string to array of strings. If given something other than an array or CSV string, it becomes the first item in the returned array. |
| `$sanitizer->array($value, 'name')` | Same as above, but applies the given sanitizer method 'name' to all items in the array. The 'name' can be any sanitizer method. Make sure that 'name' is not coming from user input. |
| `$sanitizer->array($value, 'name', $options)` | Same as above, but with additional options to modify behavior. See the phpdoc with this method for full details. |
| `$sanitizer->intArray($value)` | Sanitize array or CSV string to array of unsigned integers. Can also sanitize to unsigned integers if given a negative 'min' option; see the next method variation below. |
| `$sanitizer->intArray($value, $options)` | Same as above, but with an array of `$options` to modify behavior. It accepts any option that the array() or int() method accepts. For example, specify a 'min' (int) option to make that the minimum allowed value, or a 'max' (int) option to make that the maximum allowed value. |
| `$sanitizer->option($value, $allowed)` | Return `$value` if it exists in the `$allowed` array of values, or null if it doesn't. |
| `$sanitizer->options($values, $allowed)` | Return array of given `$values` that that also exist in `$allowed` array whitelist of values. |
| `$sanitizer->bool($value)` | Convert the given value to a boolean. Behaves similarly to PHP bool typecasting, except that it can identify "true" and "false" as strings and return the appropriate boolean. If given an array, it returns true if the array contains at least one item, or false if it is empty. |
| `$sanitizer->testAll($value)` | Tests the given `$value` against all available Sanitizer methods. Returns an associative array indexed by method name with each element containing the sanitized result. |

The above is just a summary of these method calls. See the phpdoc included in /wire/core/Sanitizer.php for full details on each method call.

That last mentioned method `$sanitizer->testAll()` is a fun one. Try running the output of that one through `print_r()` or `var_export()`.


## Core and Pro Module Updates


### New version of CKEditor (4.5.3)

Last week we added a workaround for a bug in CKEditor 4.5.0 / 4.5.1 / 4.5.2. This week we removed it. The folks at CKEditor released 4.5.3, which fixed the bug that we implemented a workaround for, so it was no longer necessary. We've updated the core version of CKEditor to the latest 4.5.3.


### New versions of Lister and ListerPro (1.0.7)

Both Lister and ListerPro were updated to correct some minor bugs with regard to image and file output. The latest version of ListerPro (1.0.7) is available for download now in the ListerPro board, and it requires ProcessWire 2.6.14 (today's release version).


### Image Fieldtype API improvements for hidpi (retina)

The Image Fieldtype (FieldtypeImage) has been updated to expand the capabilities of the `$image->hidpiWidth()` and `$image->hidpiHeight()` methods. This makes them consistent with the behavior of the existing `$image->width()` and `$image->height()` methods. Previously these hidpi methods simply returned the width or height of the image necessary to render it at hidpi (retina) resolution. Now these methods can also perform a hidpi resize on an image, if you provide a width or height to them as the first argument, i.e. `$resized = $page->image->hidpiWidth(300);` You may also specify a second $options array argument to the method calls, like you can for any of the other image resizing methods.
