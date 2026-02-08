# $pagesRequest->___getPageForUser(Page $page, User $user): Page|NullPage

Source: `wire/core/PagesRequest.php`

Update/get page for given user

Must be called once the current $user is known as it may change the $page.
Returns NullPage if user lacks access or page out of bounds.
Returns different page if it should be substituted due to lack of access (like login page).

## Arguments

- `$page` `Page`
- `$user` `User`

## Return value

Page|NullPage
