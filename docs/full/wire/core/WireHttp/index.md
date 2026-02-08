# WireHttp

Source: `wire/core/WireHttp.php`

ProcessWire HTTP tools

Provides capability for sending POST/GET requests to URLs

WireHttp enables you to send HTTP requests to URLs, download files, and more.
$http
$http = new WireHttp();
~~~~~
// Get the contents of a URL
$response = $http->get("http://domain.com/path/");
if($response !== false) {
  echo "Successful response: " . $sanitizer->entities($response);
} else {
  echo "HTTP request failed: " . $http->getError();
}
~~~~~

Thanks to @horst for his assistance with several methods in this class.

ProcessWire 3.x, Copyright 2025 by Ryan Cramer
https://processwire.com

Groups:
Group: [other](group-other.md)

Methods:
Method: [__construct()](method-__construct.md)
Method: [post()](method-post.md)
Method: [get()](method-get.md)
Method: [head()](method-head.md)
Method: [status()](method-status.md)
Method: [statusText()](method-statustext.md)
Method: [delete()](method-delete.md)
Method: [patch()](method-patch.md)
Method: [put()](method-put.md)
Method: [___send()](method-___send.md)
Method: [sendOptions()](method-sendoptions.md)
Method: [sendFopen()](method-sendfopen.md)
Method: [sendCURL()](method-sendcurl.md)
Method: [sendSocket()](method-sendsocket.md)
Method: [___download()](method-___download.md)
Method: [downloadCURL()](method-downloadcurl.md)
Method: [downloadFopen()](method-downloadfopen.md)
Method: [downloadSocket()](method-downloadsocket.md)
Method: [openWritableFile()](method-openwritablefile.md)
Method: [setHeaders()](method-setheaders.md)
Method: [setHeader()](method-setheader.md)
Method: [getHeaders()](method-getheaders.md)
Method: [setCookie()](method-setcookie.md)
Method: [setData()](method-setdata.md)
Method: [getResponseHeader()](method-getresponseheader.md)
Method: [getResponseHeaders()](method-getresponseheaders.md)
Method: [getResponseHeaderValues()](method-getresponseheadervalues.md)
Method: [setResponseHeader()](method-setresponseheader.md)
Method: [setResponseHeaderValues()](method-setresponseheadervalues.md)
Method: [___sendFile()](method-___sendfile.md)
Method: [sendFileRange()](method-sendfilerange.md)
Method: [sendStatusHeader()](method-sendstatusheader.md)
Method: [resetResponse()](method-resetresponse.md)
Method: [resetRequest()](method-resetrequest.md)
Method: [getError()](method-geterror.md)
Method: [getHttpCode()](method-gethttpcode.md)
Method: [getHttpCodes()](method-gethttpcodes.md)
Method: [getSuccessCodes()](method-getsuccesscodes.md)
Method: [getErrorCodes()](method-geterrorcodes.md)
Method: [setAllowSchemes()](method-setallowschemes.md)
Method: [getAllowSchemes()](method-getallowschemes.md)
Method: [setValidateURLOptions()](method-setvalidateurloptions.md)
Method: [getUserAgent()](method-getuseragent.md)
Method: [setUserAgent()](method-setuseragent.md)
Method: [setTimeout()](method-settimeout.md)
Method: [getTimeout()](method-gettimeout.md)

Constants:
Const: [defaultPostContentType](const-defaultpostcontenttype.md)
