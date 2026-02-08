# FilenameArray

Source: `wire/core/FilenameArray.php`

ProcessWire FilenameArray

Manages array of filenames or file URLs, like for $config->scripts and $config->styles.

ProcessWire 3.x, Copyright 2023 by Ryan Cramer
https://processwire.com

## add()

Add a file

@param string $filename

@return $this

## getKey()

Get key for $filename that excludes query strings

@param string $filename

@return string

## prepend()

Prepend $filename to the beginning

@param string $filename

@return $this

## append()

Append $filename to the end

@param string $filename

@return FilenameArray

## getIterator()

Make iterable

@return \ArrayObject

## urls()

Get cache-busting URLs for this FilenameArray

This is the same as iterating this FilenameArray except that it appends cache-busting
query strings to the URLs that resolve to physical files.

@param bool|null|string $useVersion See Config::versionUrls() for arument details

@return array

@throws WireException

@see Config::versionUrls()

@since 3.0.227

## unique()

Make FilenameArray unique (deprecated)

@deprecated no longer necessary since the add() function ensures uniqueness

@return FilenameArray

## remove()

Remove filename

@param string $filename

@return $this

## removeAll()

Remove all filenames

@return $this

## replace()

Replace one file with another

@param string $oldFile

@param string $newFile

@return $this

@since 3.0.215

## __toString()

String value containing print_r() dump of all filenames

@return string

## count()

Return count of items in this FilenameArray

@return int
