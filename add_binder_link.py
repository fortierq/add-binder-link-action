import re
import sys

def add_link(repo, nb, env, branch_repo, branch_env, force):
    """Add a link to binder in the title of nb
    Args:
        repo: repository of the notebook
        nb: path to the notebook relative to repo
        env: repository for the Binder environment
        branch_repo: branch for repo
        branch_env: branch for env
    """    
    with open(nb, 'r') as f:
        lines = f.read()
        m = re.search('"# (.*)\\\\n', lines)
        if not m:
            print(f"Error: {nb} does not have a title")
            return
        i, j = m.start(1), m.end(1)
        if "binder" in m.string:
            print(f"Binder link is already in {nb}")
            if not force:
                return
            m = re.search("'>([^<]*)", m.string)
        title = m.group(1)
        repo_nb = repo.split("/")[-1] + "/" + nb
        def F(s): return s.replace('/', '%252F')
        url = f"https://mybinder.org/v2/gh/{ env }/{ branch_env }?urlpath=git-pull%3Frepo%3Dhttps%253A%252F%252Fgithub.com%252F{ F(repo) }%26urlpath%3Dlab%252Ftree%252F{ F(repo_nb) }%26branch%3D{ branch_repo }"
        title = f"<center><a href='{url}'>{title} <img src=https://mybinder.org/badge.svg></a></center>"

    with open(nb, 'w') as f:
        f.write(lines[:i] + title + lines[j:])

add_link(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5], sys.argv[6].lower() == 'true')
