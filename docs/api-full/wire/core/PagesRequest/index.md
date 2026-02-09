# PagesRequest

Source: `wire/core/PagesRequest.php`

Inherits: `Wire`

## Summary

ProcessWire Pages Request

Common methods:
- [`init()`](method-init.md)
- [`setPage()`](method-setpage.md)
- [`getPage()`](method-___getpage.md)
- [`getPageInfo()`](method-getpageinfo.md)
- [`getPageForUser()`](method-___getpageforuser.md)

Groups:
Group: [other](group-other.md)

Pages Request
`$pages->request`
Methods for identifying and loading page from current request URL.
Methods in this class should be accessed from `$pages->request()`, i.e.
~~~~~
$page = $pages->request()->getPage();
~~~~~

## Methods
- [`__construct(Pages $pages)`](method-__construct.md) Construct
- [`init()`](method-init.md) Initialize
- [`setPage(Page|NullPage|null $page): Page|NullPage|null`](method-setpage.md) Set current request page
- [`getPage(array $options = array()): Page|NullPage`](method-___getpage.md) (hookable) Get the requested page
- [`getPageInfo(): array`](method-getpageinfo.md) Get array of page info (as provided by PagePathFinder)
- [`getPageForUser(Page $page, User $user): Page|NullPage`](method-___getpageforuser.md) (hookable) Update/get page for given user
- [`getClosestPage(): Page|NullPage`](method-___getclosestpage.md) (hookable) Get closest matching page when getPage() returns an error/NullPage
- [`getRequestPage(): NullPage|Page`](method-getrequestpage.md) Get page that was requested
- [`getRequestPagePath(): bool|string`](method-getrequestpagepath.md) Get the requested path
- [`checkRequestFile(string &$path): bool|Page|NullPage`](method-checkrequestfile.md) Check if the requested path is to a secured page file
- [`checkRequestFilePrefix(string &$path): bool`](method-checkrequestfileprefix.md) Check for secured filename: method 2 (deprecated)
- [`getLoginPageOrUrl(?Page $page = null): string|Page|null`](method-___getloginpageorurl.md) (hookable) Get login Page object or URL to redirect to for login needed to access given $page
- [`checkAccess(Page $page, User $user): Page|string|null`](method-checkaccess.md) Check that the current user has access to the page and return it
- [`checkAccessDelegated(Page $page): Page|null|bool`](method-checkaccessdelegated.md) Check access to a delegated page (like a repeater)
- [`checkAccessRepeater(Page $page): Page|null|bool`](method-checkaccessrepeater.md) Check access to a delegated repeater
- [`checkScheme(Page $page)`](method-checkscheme.md) If the template requires a different scheme/protocol than what is here, then redirect to it.
- [`checkRequestMethod(Page $page): bool`](method-checkrequestmethod.md) Check current request method
- [`pagefileSecurePossibleUrl(string $url): bool`](method-pagefilesecurepossibleurl.md) Are secure pagefiles possible on this system and url?
- [`setResponseCode(int $code, string $message = '')`](method-setresponsecode.md) Set response code and type
- [`getResponseCodeNames(): array`](method-getresponsecodenames.md) Get all possible response code names indexed by http response code
- [`getResponseCodeName(): string`](method-getresponsecodename.md) Get response type name for this request
- [`getResponseCode(): int`](method-getresponsecode.md) Get response http code for this request
- [`setRequestPath(string $requestPath)`](method-setrequestpath.md) Set request path
- [`getRequestPath(): string`](method-getrequestpath.md) Get request path
- [`getLanguageName(): string`](method-getlanguagename.md) Get request language name
- [`setRedirectPath(string $redirectPath, int $type = 301)`](method-setredirectpath.md) Set the redirect path
- [`setRedirectUrl(string $redirectUrl, int $type = 301)`](method-setredirecturl.md) Set the redirect URL
- [`getRedirectUrl(): string`](method-getredirecturl.md) Get the redirect URL
- [`getRedirectType(): int`](method-getredirecttype.md) Get the redirect type (0, 301, 302, 307, 308)
- [`getPageNum(): null|int`](method-getpagenum.md) Get the requested pagination number
- [`getPageNumPrefix(): null|string`](method-getpagenumprefix.md) Get the requested pagination number prefix
- [`getFile(): string`](method-getfile.md) Get the requested file
- [`getRequestFile(): string`](method-getrequestfile.md) Get the requested file (alias of getFile method)
- [`getResponseError(): string`](method-getresponseerror.md) Get message about response only if response was an error, blank otherwise
- [`setResponseMessage(string $message, bool $append = false)`](method-setresponsemessage.md) Set response message
- [`getResponseMessage(): string`](method-getresponsemessage.md) Get message string about response
