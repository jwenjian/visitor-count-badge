# visitor-count-badge
A badge generator for count visitor of your README

## Demo
See below badge, try to refresh current page(1 minute(exactly) later, controlled by http response header `Age`, since Github will cache the svg files, see: https://help.github.com/en/articles/about-anonymized-image-urls) then see again:

![](http://149.28.189.64:5000/)

## Install dependencies

1. `pip install -U Flask`
2. `pip install pybadges`

## How to use

Add a image to your README file:

```markdown
![Total visitor](http://localhost:5000)
```
