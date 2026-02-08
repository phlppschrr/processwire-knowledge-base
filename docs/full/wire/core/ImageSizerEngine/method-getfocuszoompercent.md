# ImageSizerEngine::getFocusZoomPercent()

Source: `wire/core/ImageSizerEngine.php`

Get current zoom percentage setting or 0 if not set

Value is determined from the $this->cropping array index 2 and is used only if index 0 and
index 1 are percentages (and indicated as such with a percent sign).

@return int
