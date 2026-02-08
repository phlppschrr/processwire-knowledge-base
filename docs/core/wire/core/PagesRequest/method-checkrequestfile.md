# PagesRequest::checkRequestFile()

Source: `wire/core/PagesRequest.php`

Check if the requested path is to a secured page file

- This function sets $this->requestFile when it finds one.
- Returns Page when a pagefile was found and matched to a page.
- Returns NullPage when request should result in a 404.
- Returns true and updates $path when pagefile was found using deprecated prefix method.
- Returns false when none found.

@param string $path Request path

@return bool|Page|NullPage
