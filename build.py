
pages = [ {
    "filename": "content/7-amazing.html",
    "output": "docs/7-amazing.html",
    "title" : "7 Amazing...",
}, 
{
    "filename": "content/a-new-start.html",
    "output": "docs/a-new-start.html",
    "title": "A New Start...",
},
{
    "filename": "content/blog.html",
    "output": "docs/blog.html",
    "title": "Blog...",
},
{
    "filename": "content/contact.html",
    "output": "docs/contact.html",
    "title": "Contact",
},
{
    "filename": "content/developers-of-color.html",
    "output": "docs/developers-of-color.html",
    "title": "Developers of Color...",
},
{
    "filename": "content/easier-way.html",
    "output": "docs/easier-way.html",
    "title": "Easier Way...",
},
{
    "filename": "content/index.html",
    "output": "docs/index.html",
    "title": "Home",
},
{
    "filename": "content/machine-learning.html",
    "output": "docs/machine-learning.html",
    "title": "Machine Learning...",
},
{
    "filename": "content/my-first.html",
    "output": "docs/my-first.html",
    "title": "My First...",
},
{
    "filename": "content/passive-income.html",
    "output": "docs/passive-income.html",
    "title": "Passive Income...",
},
{
    "filename": "content/projects.html",
    "output": "docs/projects.html",
    "title": "Projects",
},
{
    "filename": "content/recruiting.html",
    "output": "docs/recruiting.html",
    "title": "Recruiting...",
},
{
    "filename": "content/tapping-into.html",
    "output": "docs/tapping-into.html",
    "title": "Tapping into...",
},
{
    "filename": "content/wireframes.html",
    "output": "docs/wireframes.html",
    "title": "Wireframes",
}
]




def add_template(content):
    template = open("templates/base.html").read()
    finished_html = template.replace("{{content}}" , content)
    return finished_html


def main():
    for page in pages:
        file_name=page["filename"]
        output_page=page["output"]
        content = open(file_name).read()
        apply = add_template(content)
        return open(output_page , "w+").write(apply)
        #print(apply)
main()

