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

Groups:
Group: [other](group-other.md)

Methods:
Method: [__construct()](method-__construct.md)
Method: [__construct()](method-__construct.md)
Method: [init()](method-init.md)
Method: [setPage()](method-setpage.md)
Method: [getPage()](method-___getpage.md) (hookable)
Method: [getPageInfo()](method-getpageinfo.md)
Method: [getPageForUser()](method-___getpageforuser.md) (hookable)
Method: [getClosestPage()](method-___getclosestpage.md) (hookable)
Method: [getRequestPage()](method-getrequestpage.md)
Method: [getRequestPagePath()](method-getrequestpagepath.md)
Method: [checkRequestFile()](method-checkrequestfile.md)
Method: [checkRequestFilePrefix()](method-checkrequestfileprefix.md)
Method: [getLoginPageOrUrl()](method-___getloginpageorurl.md) (hookable)
Method: [checkAccess()](method-checkaccess.md)
Method: [checkAccessDelegated()](method-checkaccessdelegated.md)
Method: [checkAccessRepeater()](method-checkaccessrepeater.md)
Method: [checkScheme()](method-checkscheme.md)
Method: [checkRequestMethod()](method-checkrequestmethod.md)
Method: [pagefileSecurePossibleUrl()](method-pagefilesecurepossibleurl.md)
Method: [setResponseCode()](method-setresponsecode.md)
Method: [getResponseCodeNames()](method-getresponsecodenames.md)
Method: [getResponseCodeName()](method-getresponsecodename.md)
Method: [getResponseCode()](method-getresponsecode.md)
Method: [setRequestPath()](method-setrequestpath.md)
Method: [getRequestPath()](method-getrequestpath.md)
Method: [getLanguageName()](method-getlanguagename.md)
Method: [setRedirectPath()](method-setredirectpath.md)
Method: [setRedirectUrl()](method-setredirecturl.md)
Method: [getRedirectUrl()](method-getredirecturl.md)
Method: [getRedirectType()](method-getredirecttype.md)
Method: [getPageNum()](method-getpagenum.md)
Method: [getPageNumPrefix()](method-getpagenumprefix.md)
Method: [getFile()](method-getfile.md)
Method: [getRequestFile()](method-getrequestfile.md)
Method: [getResponseError()](method-getresponseerror.md)
Method: [setResponseMessage()](method-setresponsemessage.md)
Method: [getResponseMessage()](method-getresponsemessage.md)
