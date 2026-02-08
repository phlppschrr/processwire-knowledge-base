# ProcessWire templates and how they work

Source: https://processwire.com/docs/start/structure/templates/

## Summary

Every Page has a template which defines the type of Page and what fields are present on pages using it. Every template may be used by one or more pages.

## Key Points

- Every Page has a template which defines the type of Page and what fields are present on pages using it. Every template may be used by one or more pages.
- Each Page in ProcessWire is a storage container for content, and each Page also has a map for the structure of that content, called the “template.” The primary role of these templates is to define what fields are present on pages using them, but they also do much more.
- We refer to the template when talking about the type of a Page. For example, a template called “product” might represent a product being sold that has a title, description and price. Every page that uses the "product" template would represent a single product having the ability to store each of those fields (title, description, price). When a Page uses the "product" template, we would refer to it as a “Product Page”, since the template defines the type of Page that it is.

## Sections


## Templates in ProcessWire

Every Page has a template which defines the type of Page and what fields are present on pages using it. Every template may be used by one or more pages.


### What is a template?

Each Page in ProcessWire is a storage container for content, and each Page also has a map for the structure of that content, called the “template.” The primary role of these templates is to define what fields are present on pages using them, but they also do much more.

We refer to the template when talking about the type of a Page. For example, a template called “product” might represent a product being sold that has a title, description and price. Every page that uses the "product" template would represent a single product having the ability to store each of those fields (title, description, price). When a Page uses the "product" template, we would refer to it as a “Product Page”, since the template defines the type of Page that it is.

If you are familiar with databases, you can think of the template as the database table that defines the fields for each row (schema), while each Page is one of those rows. While this isn't actually how ProcessWire maps pages and tables to the database, it can be a helpful metaphor in this case.


### Template files

Each template may also be represented with a PHP file in the /site/templates/ directory of a ProcessWire installation. Each template file is responsible for handling the output of pages that use the corresponding template. To repeat our earlier example, the “product” template would be represented by a file named /site/templates/product.php. That file could output the title, description and price of any product.

Template files are only required for pages that must produce output when accessed at their URL. Without a template file to output a Page's content, there's nothing to output, so ProcessWire will produce a "404 page not found" error if the URL is accessed from the browser, regardless of whether a Page actually exists at that URL.

Even in a default installation, many pages in ProcessWire have no template file. For instance, users, roles and permissions have no corresponding template file by default. That's because those Page types are used for access control, and we don't need or want them to produce any output.


### Examples of templates

Earlier we used an example of a “product” template, but let’s look at more common examples. It's common in websites to have a template named "home" to represent the homepage, and another called "basic-page" to represent basic content pages, like those you might use in an “About Us” section. These templates will always have corresponding home.php and basic-page.php template files to handle their output.

If the site has a blog, we might have a template named “blog-post” to represent each post in the blog section of the site. If our site as a search engine or contact page, we'll likely use separate templates for those as well, as their content and/or implementation needs are likely to be unique relative to other pages in the site. For instance, our "search" template needs to have a template file (search.php) that takes user input and uses it to search on our content, then output links to the matching pages.


### Scalability and customizability

You can create as many templates as you need, and there is no limit to the number of pages you can create using any given template. Likewise, you can assign as many fields as you need to any template. This means the possibilities are endless in terms of custom content types and scalability. ProcessWire makes no assumptions about what your needs are and thus, all content types are custom content types.

Needs change over time, and templates are built for this. You can add or remove fields from your template at any time. Those changes are immediately reflected upon any any pages using the template.


### Other Page settings managed by templates

The primarily role of a template is to represent a Page's type, defining the fields of pages using it. But templates also define a lot more about the page, when and where needed:


### Access control

A template can define access control for pages using it. This is used to limit what roles can view, edit, move or delete pages using the template, what roles are allowed to create new pages of that type, and what roles are allowed add new child pages to them. The template can also dictate whether or not that access control gets inherited by its children, grandchildren, and so on.


### Family

A template can dictate whether or not pages using it support children, as well as what templates are allowed for those children. Likewise, a template can indicate whether it is allowed to be used for new pages, and if so, where those pages can be created.


### URLs

A template defines the style of URLs used by pages using it, and whether those URLs support pagination, URL segments, trailing slashes, and more. It can also dictate whether pages using it may only be accessed by HTTPS.


### Files

If a template has a corresponding template file, it can indicate what its content-type will be on the front-end, whether that is HTML, XML, JSON, plain text, or any other user definable content-type. It can also indicate any other file that should be automatically prepended or appended to its output.


### Cache

A template can be configured to cache its output on the front-end, so that it only reloads its PHP template-file at certain intervals, and delivers cached content the rest of the time. Several other settings accompany the details of how the caching should work.


### Advanced

A template can be categorized with tags, it can customize the page editor (when an edited page is using the template), it can dictate how required fields are handled, it can control how using it appear in the page list, and more.
