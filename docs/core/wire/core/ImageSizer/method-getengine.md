# $imageSizer->getEngine($engineName = ''): ImageSizerEngine|null

Source: `wire/core/ImageSizer.php`

Get the current ImageSizerEngine

## Arguments

- string $engineName Optionally specify a specific engine name to get a new instance of that engine When used, returned engine is in an unprepared state (no filename assigned, etc.). Since 3.0.138.

## Return value

ImageSizerEngine|null Returns ImageSizerEngine or null only if requested $engineName is not found. If no $engineName is specified this method may return an existing instance from a previous call.

## Throws

- WireException
