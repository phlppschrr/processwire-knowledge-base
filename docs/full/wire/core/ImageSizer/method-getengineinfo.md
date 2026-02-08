# $imageSizer->getEngineInfo($name = ''): array

Source: `wire/core/ImageSizer.php`

Get array of information for all ImageSizer engines (or optionally a specific ImageSizer engine)

Returns array of arrays indexed by engine name, each with the following:

 - `name` (string): engine name
 - `title` (string): engine title
 - `class` (string): PHP class name for engine
 - `summary` (string): Single sentence summary of the engine
 - `author` (string): Authr name (if available)
 - `moduleVersion` (string): Version of the module that powers this engine
 - `libraryVersion` (string): Version of the library that powers this engine
 - `sources` (array): Supported formats for source images it reads (i.e. JPG, JPEG, PNG, PNG24, GIF, GIF87, etc.)
 - `targets` (array): Supported formats for target images it creates (i.e. JPG, PNG, PNG24, WEBP, etc.)
 - `quality` (int): Current quality setting configured with the engine
 - `sharpening` (string): Current sharpening setting configured with the engine
 - `priority` (int): Engine priority (lower is higher priority)
 - `runOrder` (int): Order ImageSizer will try this engine in relative to others (lower runs first), derived from priority.

## Arguments

- `$name` (optional) `string` Specify engine name to get info just for that engine or omit to get info for all engines (default)

## Return value

array Array of arrays indexed by engine name, or if $name specified then just array of info for that engine. Returns empty array on error.

## Since

3.0.138
