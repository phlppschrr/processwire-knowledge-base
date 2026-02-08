# $wireCache->renderFile($filename, $expire = null, array $options = array()): string|bool

Source: `wire/core/WireCache.php`

Render a file as a ProcessWire template file and cache the output

This method is similar to the `$files->render()` method and actually delegates the file
rendering to that method (when creating the cache). The important difference is that this
method caches the output according to WireCache rules for the `$expire` argument, rather
than re-rendering the file on every call.

If there are any changes to the source file `$filename` the cache will be automatically
re-created, regardless of what is specified for the `$expire` argument.

~~~~~~
// render primary nav from site/templates/partials/primary-nav.php
// and cache for 3600 seconds (1 hour)
echo $cache->renderFile('partials/primary-nav.php', 3600);
~~~~~~

## Arguments

- string $filename Filename to render (typically PHP file). Can be full path/file, or dir/file relative to current work directory (which is typically /site/templates/). If providing a file relative to current dir, it should not start with "/". File must be somewhere within site/templates/, site/modules/ or wire/modules/, or provide your own `allowedPaths` option. Please note that $filename receives API variables already (you don’t have to provide them).
- int|Page|string|null $expire Lifetime of this cache, in seconds, OR one of the following: - Specify one of the `WireCache::expire*` constants. - Specify the future date you want it to expire (as unix timestamp or any `strtotime()` compatible date format) - Provide a `Page` object to expire when any page using that template is saved. - Specify `WireCache::expireNever` to prevent expiration. - Specify `WireCache::expireSave` to expire when any page or template is saved. - Specify selector string matching pages that–when saved–expire the cache. - Omit for default value, which is `WireCache::expireDaily`.
- array $options Accepts all options for the `WireFileTools::render()` method, plus these additional ones: - `name` (string): Optionally specify a unique name for this cache, otherwise $filename will be used as the unique name. (default='') - `vars` (array): Optional associative array of extra variables to send to template file. (default=[]) - `allowedPaths` (array): Array of paths that are allowed (default is anywhere within templates, core modules and site modules) - `throwExceptions` (bool): Throw exceptions when fatal error occurs? (default=true)

## Return value

string|bool Rendered template file or boolean false on fatal error (and throwExceptions disabled)

## Throws

- WireException if given file doesn’t exist

## See also

- [WireFileTools::render()](../WireFileTools/method-render.md)

## Meta

- @since 3.0.130
