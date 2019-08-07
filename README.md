# visitor-count-badge

[简体中文](README_cn.md)

A badge generator for count visitor of your README, it support 2 endpoints now:

1. total.svg
> count total visitors to your README or Issue

2. today.svg
> count visitors only in current day(server timezone), and be noted: this will **NOT** increase the total count

## Demo
See below badge, try to refresh current page then see again :tada:

[![](https://visitor-count-badge.herokuapp.com/total.svg?repo_id=jwenjian.visitor-count-badge)](https://github.com/jwenjian/ghiblog/issues/43)
[![](https://visitor-count-badge.herokuapp.com/today.svg?repo_id=jwenjian.visitor-count-badge)](https://github.com/jwenjian/ghiblog/issues/43)

## Install dependencies

1. `pip install -r requirements.txt`

## IDE run
`FLASK_APP=main.py flask run`

## How to use

Add a image to your README file:

```markdown
![Total visitor](https://visitor-count-badge.herokuapp.com/total.svg?repo_id=)
![Visitors in today](https://visitor-count-badge.herokuapp.com/today.svg?repo_id=)
```

in which:

`repo_id`:

An unique string represent your current README, recommend as following pattern

- For README:

{your.github.login}.{your.repo.id}, for example: repo_id=`jwenjian.ghiblog`

- For Issue:

{repo.owner.login}.{repo.id}.issue.{your.issue.id}, for example, repo_id=`jwenjian.ghiblog.issue.1`
