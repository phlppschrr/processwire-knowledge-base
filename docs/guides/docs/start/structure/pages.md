# Pages in ProcessWire CMS and how they work

Source: https://processwire.com/docs/start/structure/pages/

## Summary

Almost everything in ProcessWire is represented by a Page. The term “Page” refers to a webpage, though in ProcessWire it’s also much more.

## Key Points

- Almost everything in ProcessWire is represented by a Page. The term “Page” refers to a webpage, though in ProcessWire it’s also much more.
- Page is the primarily type used in ProcessWire, representing everything from the pages on your website to the users that access it. But there's nothing complex about a Page, in fact, it's really very simple.
- A webpage has a dedicated URL that you can type in your web browser and view. That accurately describes a ProcessWire Page too. A webpage usually has content, so does a Page in ProcessWire. Though in ProcessWire, a Page is not just something for the browser to load or the eyes to look at. It is a dedicated location with a unique URL where content is stored, whether visible to the browser or not.

## Sections


## Pages in ProcessWire

Almost everything in ProcessWire is represented by a Page. The term “Page” refers to a webpage, though in ProcessWire it’s also much more.


### What is a Page?

Page is the primarily type used in ProcessWire, representing everything from the pages on your website to the users that access it. But there's nothing complex about a Page, in fact, it's really very simple.

A webpage has a dedicated URL that you can type in your web browser and view. That accurately describes a ProcessWire Page too. A webpage usually has content, so does a Page in ProcessWire. Though in ProcessWire, a Page is not just something for the browser to load or the eyes to look at. It is a dedicated location with a unique URL where content is stored, whether visible to the browser or not.

A Page in ProcessWire can be used to output content like a webpage, but it can also be used as a more general storage location for content. Whether it produces output at its dedicated URL or not is up to the web developer.

In a standard ProcessWire installation, most pages are both a visible webpage on the front-end, and a storage container for content on the back-end. Very often the content that is stored with the Page is the same content that is output at its dedicated URL on the front-end. Though as we'll find out below, the utility of pages goes far beyond that.


### Page types

What content is stored on any given Page depends on what fields the Page contains. These fields are dictated by the Page's template. The template in essence defines the Page's type. Without a template to define the Page's type, a Page would just be an abstract empty container with no content (which we refer to as a NullPage).

The important thing to remember for now is simply that every page has one or more fields defined by the template that it uses. We commonly refer to pages by their template. For instance, we might refer to a Page using the “blog-post” template as a “Blog post”, rather than just a Page.


### Page family tree

All the pages in a ProcessWire installation exist within a family tree structure. Every Page has a parent Page (except the homepage), and every page can optionally have children. The homepage is the root of the family tree and it has children that are the first level of descendants in that family tree. Those descendants can have their own children, and so on.

This family tree structure is consistent with the structure of URLs, where the URL “/” would be the homepage, and the URL “/about/” would be a child of the homepage. The URL “/about/staff/” would be a child of the “/about/” page, which also makes it a grandchild of the homepage.

ProcessWire’s API uses methods that are consistent with this family tree structure, so every Page has “parent” and “children” properties/methods that you can access, among several others.

Perhaps your parents have defined some aspects of your life. The same goes for pages—any parent Page can define what default order its children (which are also pages) should appear in. This order can be based on any field present in each child Page's content (like a date or title), or it can be a manual order that an editor drags and drops them to.


### Page buckets

While all pages exist within a family tree structure, that's not the only way that pages can be referenced. Pages can be identified and/or loaded based on any property common to them, regardless of where they are in the family tree.

It's common for the Page [template](../templates/) to be used as the property used to find all pages of the same type, wherever they may be. Though it can actually be any property/field common to any group of pages, anywhere in the family tree. In this manner, pages can work like the “bucket system”.

To use a metaphor, think of an outdoor family gathering where everyone that's getting hot is encouraged to jump into the pool for a swim to cool off. That would be our “bucket” of “people that were getting hot and wanted to cool off”. Who is in this bucket (a pool) has everything to do with properties of the people (those getting hot), and nothing to do with parent and child relationships.

In ProcessWire, we might ask for a bucket of pages that contains “all product pages” (all pages using the “product” template). Or we might ask for all product pages that also have a price less than 100 Euros. Or we might ask for all that, but the pages must also have a description that includes the word “Apple” somewhere within their description. In ProcessWire, the “bucket” is called a PageArray, which is a unique group of pages that can exist at runtime outside of the family tree structure.

In this manner, ProcessWire can behave as a dynamic bucket system, where everything is findable, filterable and sortable, regardless of the underlying family tree structure in the website. The entire site's content is at your fingertips. Any one Page can access any others, just as if they were already present in memory.


### Pages can reference one another

Another highly useful aspect of Pages is that they can cross reference each other in one-to-many, many-to-one, or many-to-many relationships, regardless of where they are in the family tree structure. We call these Page references.

A common example of Page references are categories, like those you might use to identify the topics for a blog post. Every blog post can have one or more of these selected to categorize it among other blog posts. For instance, there might be a category named “videos” that you'd select for all blog posts that have an embedded video. A user can click that category to view all posts that contain videos, regardless of dates or whatever else might be organizing the blog posts.


### Almost everything in ProcessWire is a Page

Since every Page can have a defined type (template), the utility of Pages goes far beyond just your website content. It's also what ProcessWire uses to represent individual users, roles, permissions, languages, and more. In addition, they represent every Page in ProcessWire's admin, which is itself a website built in ProcessWire.

The benefit of everything being a Page is that this keeps the both the admin UI and the API very simple. Once you know how to work with a Page, you know much of what's needed to work with any other type in ProcessWire. This results in clean consistency with how you work in ProcessWire, whether it's from the API or from the admin UI.


### Page scalability

There is no hard limit to the number of pages you can have in ProcessWire, and they are designed to scale infinitely, within the limits of the database. A given page might be packed with fields, content and files, or it might only have a simple title field. Pages are highly flexible and likely to be your best choice for managing content, no matter how much or little is needed on any given Page.

As scale increases, ProcessWire is ready-to-go with pagination of pages, lazy-loading pages, load-on-demand fields/content, caching of page loads and output, and more. ProcessWire is built with the assumption that your scale is large, regardless of how small or large it actually is, so that there is a quality, consistency and ease-of-use that transcends scale.
