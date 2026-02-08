# Config::setUrl()

Source: `wire/core/Config.php`

Change or set just the URL for the named location (leaving server disk path as-is)

- If you want to update both disk path and URL at the same time, or if URL and path are going to be the same relative to
  installation root, use the `setLocation()` method instead.

- Paths relative to PW installation root should omit the leading slash, i.e. use `site/templates/` and NOT `/site/templates/`.

- The `$for` argument can be: `cache`, `logs`, `files`, `tmp`, `templates`, or one of your own. Other named locations may
  also work, but since they can potentially be used before PW’s “ready” state, they may not be reliable.

- **Warning:** anything that changes a system URL may make the URL no longer have the protection of the root .htaccess file.
  As a result, if you modify system URLs for anything on a live server, you should also update your .htaccess file to
  reflect your changes (while leaving existing rules for original URL in place).

The following examples would go in /site/ready.php.

Let’s say we created a symbolic link in our web root `/tiedostot/` (Finnish for “files”) that points to /site/assets/files/.
We want all of our file URLs to appear as “/tiedostot/1234/img.jpg” rather than “/site/assets/files/1234/img.jpg”. We would
change the URL for ProcessWire’s `$config->urls->files` to point there like this example below. (Please also see warning above)
~~~~~
if($page->template != 'admin') {
  $config->setUrl('files', 'tiedostot/');
}
~~~~~
In this next example, we are changing all of our file URLs on the front-end to point a cookieless subdomain that maps all
requests to the root path of https://files.domain.com to /site/assets/files/. The example works for CDNs as well.
~~~~~
if($page->template != 'admin) {
  $config->setUrl('files', 'https://files.domain.com/');
}
~~~~~


@param string $for Named location from `$config->urls`, one of: `cache`, `logs`, `files`, `tmp`, `templates`, or your own.

@param string $url URL relative to PW installation root (no leading slash) or absolute URL if not (optionally including scheme and domain).

@return self

@throws WireException

@since 3.0.141
