# Unknown

Source: https://processwire.com/docs/start/variables/

ProcessWire provides various API variables to every template file. These variables provide full access to all site content. This page provides an introduction on how to use them.

API variables can be accessed in a few different ways. The most common way is as a variable. Here are a few different ways you might access the same $page API variable (as an example):

`$page` the most common access as a variable.

`page()` accessing as a function can be very convenient, when available.

`wire('page')` This works anywhere, and with any version of ProcessWire.

`wire()->page` This works anywhere too, and is more IDE friendly.

`$this->page` This is how you might access it from within a Wire-derived class.

`$this->wire('page')` A slightly more efficient way you can access from within a Wire-derived class.

`$this->wire()->page` Like the above, but more IDE friendly.

`$pages->wire()->page` API variables can also access all other API variables, by way of their wire() method. In this example, we are accessing the $page API variable from the $pages API variable. So if you have any one API variable, then you actually have them all.

Accessing API variables as a function rather than a variable can be more convenient when the variable version may be out of scope, or if your IDE highlights API variables as undefined. So whenever we refer to an API variable, make note that access it however you'd like.

This is just an introduction to some of ProcessWire's API variables. Once you are familiar with these, you'll want to use ProcessWire's full [API reference](/api/ref/) instead.

---

### Some of ProcessWire’s most common API variables

- #### [$page](/docs/start/variables/page/)The $page variable is provided to every template, and it contains all the fields specific to the page being viewed. This includes…Learn more →
- #### [$pages](/docs/start/variables/pages/)While the $page variable holds the current page, the $pages variable is where you can get at all the other pages in your site. It…Learn more →
- #### [$input](/docs/start/variables/input/)The $input variable is your connection to GET, POST and COOKIE variables, URL segments, page (pagination) numbers, and more.Learn more →
- #### [$sanitizer](/docs/start/variables/sanitizer/)The $sanitizer functions are provided to fill the most common data sanitization needs with sites developed in ProcessWire. Always…Learn more →
- #### [$session](/docs/start/variables/session/)This API variable provides access to read/write of session variables, login and logout of users, redirects, and more.Learn more →
- #### [$fields](/docs/start/variables/fields/)$fields is an API variable that contains all the custom page fields in your site. It provides the API functions available in the…Learn more →
- #### [$user](/docs/start/variables/user/)The $user API variable is your connection to the current user viewing the page.Learn more →
- #### [$log](/docs/start/variables/log/)The $log API variable enables you to create, manage and filter log entries. Log files are stored in /site/assets/logs/.Learn more →
- #### [$templates](/docs/start/variables/templates/)The $templates API variable provides access to all of your site’s templates. Use the $templates API variable to retrieve, modify…Learn more →
- #### [$config](/docs/start/variables/config/)The $config API variable contains all the settings specific to your site configuration. This includes URLs and paths, database…Learn more →

- [API variables](/docs/start/variables/)
- [$page](/docs/start/variables/page/)
- [$pages](/docs/start/variables/pages/)
- [$input](/docs/start/variables/input/)
- [$sanitizer](/api/ref/sanitizer/)
- [$session](/docs/start/variables/session/)
- [$fields](/api/ref/fields/)
- [$user](/docs/start/variables/user/)
- [$log](/api/ref/log/)
- [$templates](/docs/start/variables/templates/)
- [$config](/docs/start/variables/config/)

- [Getting started](/docs/start/)
- [Installation](/docs/start/install/)
- [Structure](/docs/start/structure/)
- [About the API](/docs/start/api/)
- [Template files](/docs/start/templates/)
- [API variables](/docs/start/variables/)
- [API access](/docs/start/api-access/)
- [Output strategies](/docs/front-end/output/)

- [Docs](/docs/)
- [API reference](/api/ref/)
- [Getting started](/docs/start/)
- [Front-end](/docs/front-end/)
- [Tutorials](/docs/tutorials/)
- [Selectors](/docs/selectors/)
- [Modules & hooks](/docs/modules/)
- [Fields, types, input](/docs/fields/)
- [Access control](/docs/user-access/)
- [Security](/docs/security/)
- [Multi-language](/docs/multi-language-support/)
- [More topics](/docs/more/)
