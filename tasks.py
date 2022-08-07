from pathlib import Path
import sys
from invoke import task


@task(name="list_tasks", default=True)
def _tasks(c):
    """Show the current list of tasks"""
    filepath = Path(__file__)
    with c.cd(filepath.parent):
        c.run(f"{sys.executable} -m invoke -c {filepath.stem} -l")


@task
def init(c):
    """Ensure hugo theme git submodule is present"""
    c.run("git submodule update --init --recursive")


@task
def new_post(c, name):
    """Create a new post specifying the name of it"""
    c.run(f"hugo new content/post/{name}/index.md")


@task
def run(c, rebuild=True):
    """Run local server"""
    ops = "--disableFastRender" if rebuild else ""
    c.run(f"hugo server -D {ops}")
