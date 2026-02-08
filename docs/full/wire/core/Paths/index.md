# Paths

Source: `wire/core/Paths.php`

ProcessWire configuration paths and URLs

Configuration paths and URLs (Paths class)
Maintains lists of file paths or URLs, primarily used by the ProcessWire $config->paths and $urls API variables.
$urls

The Paths class is used by `$config->paths` and `$config->urls` (or just `$urls`). The `$config->paths` refers to server disk paths
while `$config->urls` refers to web server URLs. All of the same properties are present on both, though several properties
are only useful on one or the other (as outlined below). You can access a path or URL like this:
~~~~~
$path = $config->paths->templates; // i.e. /path/to/htdocs/site/templates/
$url = $config->urls->templates; // i.e. /site/templates/
~~~~~
The `$config->urls` property can also be accessed more directly via the `$urls` API variable (in PW 3.x+):
~~~~~
$url = $urls->templates; // i.e. /site/templates/
~~~~~
For `$config->urls` (or `$urls`), if you prepend `http` to any of the property names (making it camelCase) it will
return the full http/https URL rather then the relative URL:
~~~~~
$httpUrl = $config->urls->httpTemplates; // i.e. https://domain.com/site/templates/
$httpUrl = $urls->httpTemplates; // same as above
~~~~~
You may optionally add your own properties as well. If you add a path/url without a leading slash “/” it is assumed to
be relative to the `root` property. If it has a leading slash, then it is absolute.
~~~~~
// add new urls properties
$urls->set('css', 'site/templates/css/'); // relative to site root
$urls->set('uikit', '/uikit/dist/'); // absolute

// get properties that were set
echo $urls->get('css'); // i.e. /site/templates/css/
echo $urls->get('uikit'); // i.e. /uikit/dist/
echo $urls->get('httpCss'); // i.e. https://domain.com/site/templates/css/
echo $urls->get('httpUikit'); // i.e. https://domain.com/uikit/dist/
echo $urls->httpUikit; // same as above (using get method call is optional for any of these)
~~~~~
Do not set `http` properties directly, as they are dynamically generated from `urls` properties at runtime upon request.

In the examples on this page, you can replace the `$urls` variable with `$config->paths` if you need to get the server path
instead of a URL. As indicated earlier, `$urls` can aso be accessed at the more verbose `$config->urls` if you prefer.

> Please note in the property/method descriptions below that use the placeholder `$urls` refers to either `$config->paths` or
`$config->urls` (or the shorter alias `$urls`). So `$urls->files` (for example) in the definitions below can refer to either
`$config->paths->files` or `$config->urls->files` (or the shorter alias `$urls->files`). We use `$urls` here because it’s
just the shortest option for example purposes.


ProcessWire 3.x, Copyright 2024 by Ryan Cramer
https://processwire.com

This file is licensed under the MIT license
https://processwire.com/about/license/mit/


The following properties are only in $config->urls
==================================================

@property string $admin Admin URL

@property string|null $next URL to next pagination of current page, when applicable (populated by MarkupPagerNav, after render)

@property string|null $prev URL to previous pagination of current page, when applicable (populated by MarkupPagerNav, after render)

The following are in $config->urls and equivalent to previously mentioned properties, but include scheme + host
===============================================================================================================

@property-read string $httpRoot Full http/https URL to site root (i.e. https://domain.com/).

@property-read string $httpTemplates  Full http/https URL to site templates (i.e. https://domain.com/site/templates/).

@property-read string $httpModules Full http/https URL to core (wire) modules.

@property-read string $httpSiteModules Full http/https URL to site modules.

@property-read string $httpMarkupRegions Full http/https URL to files added by Markup Regions. (3.0.254+)

@property-read string $httpAssets Full http/https URL to site assets (i.e. https://domain.com/site/assets/).

@property-read string $httpFiles Full http/https URL to site assets files (i.e. https://domain.com/site/assets/files/).

@property-read string $httpNext Full http/https URL to next pagination of current page (when applicable).

@property-read string $httpPrev Full http/https URL to prev pagination of current page (when applicable).

The "http" may be optionally prepended to any property accessed from $config->urls (including those you add yourself).

Groups:
Group: [other](group-other.md)
Group: [paths-only](group-paths-only.md)

Methods:
Method: [__construct()](method-__construct.md)
Method: [set()](method-set.md)
Method: [get()](method-get.md)
