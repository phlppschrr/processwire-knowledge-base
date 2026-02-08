# Pages in ProcessWire

Source: https://processwire.com/docs/start/structure/pages/

## Summary

Almost everything in ProcessWire is represented by a Page. The term “Page” refers to a webpage, though in ProcessWire it’s also much more.

## Key Points

- Almost everything in ProcessWire is represented by a Page. The term “Page” refers to a webpage, though in ProcessWire it’s also much more.
- Page is the primarily type used in ProcessWire, representing everything from the pages on your website to the users that access it. But there's nothing complex about a Page, in fact, it's really very simple.
- A webpage has a dedicated URL that you can type in your web browser and view. That accurately describes a ProcessWire Page too. A webpage usually has content, so does a Page in ProcessWire. Though in ProcessWire, a Page is not just something for the browser to load or the eyes to look at. It is a dedicated location with a unique URL where content is stored, whether visible to the browser or not.

## Sections


### What is a Page?

Page is the primarily type used in ProcessWire, representing everything from the pages on your website to the users that access it. But there's nothing complex about a Page, in fact, it's really very simple.


### Page types

What content is stored on any given Page depends on what fields the Page contains. These fields are dictated by the Page's template. The template in essence defines the Page's type. Without a template to define the Page's type, a Page would just be an abstract empty container with no content (which we refer to as a NullPage).


### Page family tree

All the pages in a ProcessWire installation exist within a family tree structure. Every Page has a parent Page (except the homepage), and every page can optionally have children. The homepage is the root of the family tree and it has children that are the first level of descendants in that family tree. Those descendants can have their own children, and so on.


### Page buckets

While all pages exist within a family tree structure, that's not the only way that pages can be referenced. Pages can be identified and/or loaded based on any property common to them, regardless of where they are in the family tree.


### Pages can reference one another

Another highly useful aspect of Pages is that they can cross reference each other in one-to-many, many-to-one, or many-to-many relationships, regardless of where they are in the family tree structure. We call these Page references.


### Almost everything in ProcessWire is a Page

Since every Page can have a defined type (template), the utility of Pages goes far beyond just your website content. It's also what ProcessWire uses to represent individual users, roles, permissions, languages, and more. In addition, they represent every Page in ProcessWire's admin, which is itself a website built in ProcessWire.


### Page scalability

There is no hard limit to the number of pages you can have in ProcessWire, and they are designed to scale infinitely, within the limits of the database. A given page might be packed with fields, content and files, or it might only have a simple title field. Pages are highly flexible and likely to be your best choice for managing content, no matter how much or little is needed on any given Page.
