# ProcessWire 3.0.105 core updates

Source: https://processwire.com/blog/posts/processwire-3.0.105-core-updates/

## Sections


## ProcessWire 3.0.105 core updates

1 June 2018 by Ryan Cramer [ 4 Comments](/blog/posts/processwire-3.0.105-core-updates/#comments)


## ProcessWire 3.0.105

This latest version on the dev branch adds a new site profile to the core, adds useful new functions to our $mail API variable, and makes significant enhancements to our $sanitizer API variable.


### New site profile in core

The “Regular” site profile has been added to the core as an installation option. You might already be familiar with this site profile from the last year, and it's been available on its own GitHub repo for quite some time. This site profile demonstrates a lot of PW3 specific features in ways the other profiles don't, and I thought it was a good time to go ahead and add it.

This site profile is still fairly simple, not unlike the default site profiles, but it goes quite a bit further in serving as a good introduction to developing with ProcessWire. For example, it demonstrates these things that the other core profiles don't:

- Use of Markup Regions
- Integration of a front-end framework (Uikit 3 in this case)
- Implementation of a basic blog with categories and comments
- Use of front-end editing
- Use of Page references
- Using a [library of helper functions](https://github.com/processwire/processwire/blob/dev/site-regular/templates/_uikit.php) for front-end output
- Use of the $cache API variable for caching markup (new)
- Use of pagination

If you are already familiar with the Regular site profile, this version added to the core is upgraded a bit from the one previously available on GitHub. It includes a much more powerful [ukNav() function](https://github.com/processwire/processwire/blob/dev/site-regular/templates/_uikit.php#L50) for rendering navigation. This is used to render the off-canvas navigation, which now lets you navigate not just primary navigation, but secondary navigation too (and further, if you want it). This version of the profile on the core also adds a [demonstration of the $cache API variable](https://github.com/processwire/processwire/blob/dev/site-regular/templates/_main.php#L115), for caching that off-canvas navigation. While not really necessary here, it does demonstrate just how simple and easy it is to use ProcessWire's built in markup caching capabilities. Lastly, this version of the profile lets you [choose](https://github.com/processwire/processwire/blob/dev/site-regular/templates/_main.php#L7) between CDN and locally hosted versions of Uikit 3 and jQuery.

All in all, I think this site profile serves as a useful introduction to modern development in ProcessWire, as well as a good starting point for developing a ProcessWire site using Uikit 3, or another framework, if preferred. If you find any ways that you think we can improve it or simplify it, please be sure to let us know.


### Updates to the $mail API variable

Added a new [$mail->mail()](https://github.com/processwire/processwire/blob/dev/wire/core/WireMailTools.php#L209) function which does the same thing as $mail->send(), except that it acts as a drop-in replacement for PHP’s mail() function, maintaining the same arguments. Meaning, you can generally change a PHP `mail()` call to a WireMail call just by prepending $mail-> to it, i.e. `$mail->mail(...)`.

Added a new [$mail->sendHTML()](https://github.com/processwire/processwire/blob/dev/wire/core/WireMailTools.php#L184) function which works the same as the $mail->send() function except that it assumes the given $body is HTML rather than text. The text-only version is automatically generated from the HTML version. An equivalent `$mail->mailHTML()` function has also been added, which is the same thing except that it duplicates the arguments from PHP’s mail() function.

Several parts of the WireMail class have been rewritten to improve various internal aspects of it. However, the external interface has not changed, nor should it affect any WireMail modules that extend it.


### Upgrades to $sanitizer

**Improvements to text() and textarea() sanitizers** Several [new options](https://github.com/processwire/processwire/blob/dev/wire/core/Sanitizer.php#L965) have been added, as outlined below:

**Improvements to $sanitizer->unentities()** The unentities() function has been [improved](https://github.com/processwire/processwire/blob/dev/wire/core/Sanitizer.php#L1868) to support a new $flags option that supports converting all entities, including those that PHP’s functions do not recognize. It converts all named entities, all decimal based entities and all hex based entities. If any apparent entities remain, it removes them. To use this option, specify boolean true for the $flags argument. i.e. `$sanitizer->unentities($str, true);`

**New $sanitizer->removeWhitespace() function** This [newly added function](https://github.com/processwire/processwire/blob/dev/wire/core/Sanitizer.php#L1983) can remove, collapse or replace all known kinds of possible whitespace in a string. This goes well beyond just spaces, tabs and newlines. It includes 99 different types of UTF-8 and HTML entity based representations of whitespace, ensuring nobody can play any whitespace games or trickery with your strings. You can optionally collapse them to a single whitespace or replace the with a whitespace character that you specify. In addition, you can optionally choose to allow certain kinds of whitespace by specifying it as an option.

In addition to the above, there are also various other small fixes and updates in the core, as usual. A huge thanks to those that help us out every week on GitHub. I hope that you all have a great weekend and enjoy reading the [ProcessWire Weekly](http://weekly.pw).
