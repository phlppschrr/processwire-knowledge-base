# PagesLoaderCache

Source: `wire/core/PagesLoaderCache.php`

ProcessWire Pages Loader Cache

Pages Loader Cache
$pages->cacher
Implements page caching of loaded pages and PageArrays for $pages API variable

ProcessWire 3.x, Copyright 2025 by Ryan Cramer
https://processwire.com

## __construct()

Construct

@param Pages $pages

## getCacheStatus()

Get cache status

Returns count of each cache type, or contents of each cache type of verbose option is specified.


@param bool|null $verbose Specify true to get contents of cache, false to get string counts, or omit for array of counts

@return array|string

@since 3.0.198

## getCache()

Given a Page ID, return it if it's cached, or NULL of it's not.

If no ID is provided, then this will return an array copy of the full cache.

You may also pass in the string "id=123", where 123 is the page_id


@param int|string|null $id

@return Page|array|null

## hasCache()

Is given page ID in the cache?


@param int page ID

@return bool

@since 3.0.243

## cache()

Cache the given page in memory


@param Page $page

@return void

## cacheGroup()

Cache given page into a named group that it can be uncached with


@param Page $page

@param string $groupName

@since 3.0.198

## uncache()

Remove the given page from the cache.

Note: does not remove pages from selectorCache. Call uncacheAll to do that.


@param Page|int $page Page to uncache or ID of page (prior to 3.0.153 only Page object was accepted)

@param array $options Additional options to modify behavior:
  - `shallow` (bool): By default, this method also calls $page->uncache(). To prevent call to $page->uncache(), set 'shallow' => true.

@return bool True if page was uncached, false if it didn't need to be

## uncacheAll()

Remove all pages from the cache


@param Page|null $page Optional Page that initiated the uncacheAll

@param array $options Additional options to modify behavior:
  - `shallow` (bool): By default, this method also calls $page->uncache(). To prevent call to $page->uncache(), set 'shallow' => true.

@return int Number of pages uncached

## uncacheGroup()

Uncache pages that were cached with given group name


@param string $groupName

@param array $options

@return int

@since 3.0.198

## selectorCache()

Cache the given selector string and options with the given PageArray


@param string $selector

@param array $options

@param PageArray $pages

@return bool True if pages were cached, false if not

## optionsArrayToString()

Convert an options array to a string

@param array $options

@return string

## getSelectorCache()

Retrieve any cached page IDs for the given selector and options OR false if none found.

You may specify a third param as TRUE, which will cause this to just return the selector string (with hashed options)


@param string $selector

@param array $options

@param bool $returnSelector default false

@return array|null|string|PageArray
