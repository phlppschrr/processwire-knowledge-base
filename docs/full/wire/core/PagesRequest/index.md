# PagesRequest

Source: `wire/core/PagesRequest.php`

Inherits: `Wire`


Groups:
Group: [other](group-other.md)

ProcessWire Pages Request

Pages Request
$pages->request
Methods for identifying and loading page from current request URL.
Methods in this class should be accessed from `$pages->request()`, i.e.
~~~~~
$page = $pages->request()->getPage();
~~~~~

Methods:
- [`__construct(Pages $pages)`](method-__construct.md)
- [`__construct(Pages $pages)`](method-__construct.md)
- [`init()`](method-init.md)
- [`setPage(Page|NullPage|null $page): Page|NullPage|null`](method-setpage.md)
- [`getPage(array $options = array()): Page|NullPage`](method-___getpage.md) (hookable)
- [`getPageInfo(): array`](method-getpageinfo.md)
- [`getPageForUser(Page $page, User $user): Page|NullPage`](method-___getpageforuser.md) (hookable)
- [`getClosestPage(): Page|NullPage`](method-___getclosestpage.md) (hookable)
- [`getRequestPage(): NullPage|Page`](method-getrequestpage.md)
- [`getRequestPagePath(): bool|string`](method-getrequestpagepath.md)
- [`checkRequestFile(string &$path): bool|Page|NullPage`](method-checkrequestfile.md)
- [`checkRequestFilePrefix(string &$path): bool`](method-checkrequestfileprefix.md)
- [`getLoginPageOrUrl(?Page $page = null): string|Page|null`](method-___getloginpageorurl.md) (hookable)
- [`checkAccess(Page $page, User $user): Page|string|null`](method-checkaccess.md)
- [`checkAccessDelegated(Page $page): Page|null|bool`](method-checkaccessdelegated.md)
- [`checkAccessRepeater(Page $page): Page|null|bool`](method-checkaccessrepeater.md)
- [`checkScheme(Page $page)`](method-checkscheme.md)
- [`checkRequestMethod(Page $page): bool`](method-checkrequestmethod.md)
- [`pagefileSecurePossibleUrl(string $url): bool`](method-pagefilesecurepossibleurl.md)
- [`setResponseCode(int $code, string $message = '')`](method-setresponsecode.md)
- [`getResponseCodeNames(): array`](method-getresponsecodenames.md)
- [`getResponseCodeName(): string`](method-getresponsecodename.md)
- [`getResponseCode(): int`](method-getresponsecode.md)
- [`setRequestPath(string $requestPath)`](method-setrequestpath.md)
- [`getRequestPath(): string`](method-getrequestpath.md)
- [`getLanguageName(): string`](method-getlanguagename.md)
- [`setRedirectPath(string $redirectPath, int $type = 301)`](method-setredirectpath.md)
- [`setRedirectUrl(string $redirectUrl, int $type = 301)`](method-setredirecturl.md)
- [`getRedirectUrl(): string`](method-getredirecturl.md)
- [`getRedirectType(): int`](method-getredirecttype.md)
- [`getPageNum(): null|int`](method-getpagenum.md)
- [`getPageNumPrefix(): null|string`](method-getpagenumprefix.md)
- [`getFile(): string`](method-getfile.md)
- [`getRequestFile(): string`](method-getrequestfile.md)
- [`getResponseError(): string`](method-getresponseerror.md)
- [`setResponseMessage(string $message, bool $append = false)`](method-setresponsemessage.md)
- [`getResponseMessage(): string`](method-getresponsemessage.md)
