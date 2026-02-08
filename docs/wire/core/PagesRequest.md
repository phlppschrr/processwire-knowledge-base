# PagesRequest

Source: `wire/core/PagesRequest.php`

ProcessWire Pages Request

Pages Request
$pages->request
Methods for identifying and loading page from current request URL.
Methods in this class should be accessed from `$pages->request()`, i.e.
~~~~~
$page = $pages->request()->getPage();
~~~~~

ProcessWire 3.x, Copyright 2025 by Ryan Cramer
https://processwire.com

## other

@method Page|NullPage getPage()

@method Page|null getPageForUser(Page $page, User $user)

@method Page|NullPage getClosestPage()

@method Page|string getLoginPageOrUrl(Page $page)

## __construct()

*********************************************************************************

## __construct()

Construct

@param Pages $pages

## init()

Initialize

## setPage()

Set current request page

@param Page|NullPage|null $page

@return Page|NullPage|null

## ___getPage()

Get the requested page

- Populates identified urlSegments or page numbers to $input.
- Returns NullPage for error, call getResponseCode() and/or getResponseMessage() for details.
- Returned page should be validated with getPageForUser() method before rendering it.
- Call getFile() method afterwards to see if request resolved to file managed by returned page.

@param array $options

@return Page|NullPage

## getPageInfo()

Get array of page info (as provided by PagePathFinder)

See the PagesPathFinder::get() method return value for a description of
what this method returns.

If this method returns a blank array, it means that the getPage()
method has not yet been called or that it did not match a page.

@return array

@since 3.0.242

## ___getPageForUser()

Update/get page for given user

Must be called once the current $user is known as it may change the $page.
Returns NullPage if user lacks access or page out of bounds.
Returns different page if it should be substituted due to lack of access (like login page).

@param Page $page

@param User $user

@return Page|NullPage

## ___getClosestPage()

Get closest matching page when getPage() returns an error/NullPage

This is useful for a 404 page to suggest if maybe the user intended a different page
and give them a link to it. For instance, you might have the following code in the
template file used by your 404 page:
~~~~~
echo "<h1>404 Page Not Found</h1>";
$p = $pages->request()->getClosestPage();
if($p->id) {
  echo "<p>Are you looking for <a href='$p->url'>$p->title</a>?</p>";
}
~~~~~

@return Page|NullPage

## getRequestPage()

Get page that was requested

If this is different from the Page returned by getPageForUser() then it would
represent the page that the user lacked access to.

@return NullPage|Page

## getRequestPagePath()

Get the requested path

@return bool|string Return false on fail, path on success

## checkRequestFile()

Check if the requested path is to a secured page file

- This function sets $this->requestFile when it finds one.
- Returns Page when a pagefile was found and matched to a page.
- Returns NullPage when request should result in a 404.
- Returns true and updates $path when pagefile was found using deprecated prefix method.
- Returns false when none found.

@param string $path Request path

@return bool|Page|NullPage

## checkRequestFilePrefix()

Check for secured filename: method 2 (deprecated)

Used only if $config->pagefileUrlPrefix is defined

@param string $path

@return bool

## ___getLoginPageOrUrl()

Get login Page object or URL to redirect to for login needed to access given $page

- When a Page is returned, it is suggested the Page be rendered in this request.
- When a string/URL is returned, it is suggested you redirect to it.
- When null is returned no login page or URL could be identified and 404 should render.

@param Page|null $page Page that access was requested to or omit to get admin login page

@return string|Page|null Login page object or string w/redirect URL, null if 404

## checkAccess()

Check that the current user has access to the page and return it

If the user doesn’t have access, then a login Page or NULL (for 404) is returned instead.

@param Page $page

@param User $user

@return Page|string|null Page to render, URL to redirect to, or null for 404

## checkAccessDelegated()

Check access to a delegated page (like a repeater)

Note: this should move to PagePermissions.module or FieldtypeRepeater.module
if a similar check is needed somewhere else in the core.

@param Page $page

@return Page|null|bool

## checkAccessRepeater()

Check access to a delegated repeater

@param Page $page

@return Page|null|bool

## checkScheme()

If the template requires a different scheme/protocol than what is here, then redirect to it.

This method just silently sets the $this->redirectUrl var if a redirect is needed.
Note this does not work if GET vars are present in the URL -- they will be lost in the redirect.

@param Page $page

## checkRequestMethod()

Check current request method

@param Page $page

@return bool True if current request method allowed, false if not

## pagefileSecurePossibleUrl()

Are secure pagefiles possible on this system and url?

@param string $url

@return bool

@since 3.0.166

## setResponseCode()

Set response code and type

@param int $code

@param string $message Optional message string

## getResponseCodeNames()

Get all possible response code names indexed by http response code

@return array

## getResponseCodeName()

Get response type name for this request

Returns string, one of:

- unknown: request not yet analyzed (0)
- ok: successful request (200)
- fileOk: successful file request (200)
- fileNotFound: requested file not found (404)
- maybeRedirect: needs decision about whether to redirect (300)
- permRedirect: permanent redirect (301)
- tempRedirect: temporary redirect (302)
- tempRedo: temporary redirect and redo using same method (307)
- permRedo: permanent redirect and redo using same method (308)
- badRequest: bad request/page path error (400)
- unauthorized: login required (401)
- forbidden: authenticated user lacks access (403)
- pageNotFound: page not found (404)
- methodNotAllowed: request method is not allowed by template (405)
- pathTooLong: path too long or segment too long (414)

@return string

## getResponseCode()

Get response http code for this request

Returns integer, one of:

- 0: unknown/request not yet analyzed
- 200: successful request
- 300: maybe redirect (needs decision)
- 301: permanent redirect
- 302: temporary redirect
- 307: temporary redirect and redo using same method
- 308: permanent redirect and redo using same method
- 400: bad request/page path error
- 401: unauthorized/login required
- 403: forbidden/authenticated user lacks access
- 404: page not found
- 405: method not allowed
- 414: request path too long or segment too long

@return int

## setRequestPath()

Set request path

@param string $requestPath

## getRequestPath()

Get request path

@return string

## getLanguageName()

Get request language name

@return string

## setRedirectPath()

Set the redirect path

@param string $redirectPath

@param int $type 301 or 302

## setRedirectUrl()

Set the redirect URL

@param string $redirectUrl

@param int $type

## getRedirectUrl()

Get the redirect URL

@return string

## getRedirectType()

Get the redirect type (0, 301, 302, 307, 308)

@return int

## getPageNum()

Get the requested pagination number

@return null|int

## getPageNumPrefix()

Get the requested pagination number prefix

@return null|string

## getFile()

Get the requested file

@return string

## getRequestFile()

Get the requested file (alias of getFile method)

@return string

## getResponseError()

Get message about response only if response was an error, blank otherwise

@return string

## setResponseMessage()

Set response message

@param string $message

@param bool $append Append to existing message?

## getResponseMessage()

Get message string about response

@return string
