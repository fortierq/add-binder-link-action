# add-binder-link-action

This GitHub action automatically adds a Binder link to every notebook in a repository, and push the changes.  
It works by looking at the first line of the form `# ...`

Example:

```
name: add binder links

on:
  push:
    branches: [main]

jobs:
  add_link:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2

      - name: add_link
        uses: fortierq/add-binder-link-action@v1
        with:
          env: 'fortierq/binder-mp2i' # binder environment to use
          branch-env: 'main' # corresponding branch
```

Examples of Binder environments for `env` :
- https://github.com/fortierq/binder-mp2i (Python, C++, OCaml)  
- https://github.com/fortierq/itc-binder (Python, Matplotlib, NumPy...)
