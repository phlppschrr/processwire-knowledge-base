# WireInput::__get()

Source: `wire/core/WireInput.php`

Retrieve the get, post, cookie or whitelist vars using a direct reference, i.e. $input->cookie

Can also be used with URL segments, i.e. $input->urlSegment1, $input->urlSegment2, $input->urlSegment3, etc.
And can also be used for $input->pageNum.

@param string $key

@return string|int|null
