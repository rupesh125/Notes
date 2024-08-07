Git Cheat Sheet

Stage & Snapshot

git status: Show modified files in the working directory, staged for your next commit
git add [file]: Add a file as it looks now to your next commit (stage)
git reset [file]: Unstage a file while retaining the changes in the working directory
git diff: Diff of what is changed but not staged
git diff --staged: Diff of what is staged but not yet committed
git commit -m “[descriptive message]”: Commit your staged content as a new commit snapshot

Setup

git config --global user.name “[firstname lastname]”: Set a name that is identifiable for credit when reviewing version history
git config --global user.email “[valid-email]”: Set an email address that will be associated with each history marker
git config --global color.ui auto: Set automatic command line coloring for Git for easy reviewing

Setup & Init

git init: Initialize an existing directory as a Git repository
git clone [url]: Retrieve an entire repository from a hosted location via URL

Branch & Merge

git branch: List your branches. A * will appear next to the currently active branch
git branch [branch-name]: Create a new branch at the current commit
git checkout: Switch to another branch and check it out into your working directory
git merge [branch]: Merge the specified branch’s history into the current one
git log: Show all commits in the current branch’s history

Installation & GUIs

GitHub for Windows
GitHub for Mac
Git for All Platforms

Share & Update

git remote add [alias] [url]: Add a git URL as an alias
git fetch [alias]: Fetch down all the branches from that Git remote
git merge [alias]/[branch]: Merge a remote branch into your current branch to bring it up to date
git push [alias] [branch]: Transmit local branch commits to the remote repository branch
git pull: Fetch and merge any commits from the tracking remote branch

Tracking Path Changes

git rm [file]: Delete the file from the project and stage the removal for commit
git mv [existing-path] [new-path]: Change an existing file path and stage the move
git log --stat -M: Show all commit logs with indication of any paths that moved

Temporary Commits

git stash: Save modified and staged changes
git stash list: List stack-order of stashed file changes
git stash pop: Write working from top of stash stack
git stash drop: Discard the changes from top of stash stack

Rewrite History

git rebase [branch]: Apply any commits of the current branch ahead of the specified one
git reset --hard [commit]: Clear staging area, rewrite working tree from the specified commit

Inspect & Compare

git log: Show the commit history for the currently active branch
git log branchB..branchA: Show the commits on branchA that are not on branchB
git log --follow [file]: Show the commits that changed the file, even across renames
git diff branchB...branchA: Show the diff of what is in branchA that is not in branchB
git show [SHA]: Show any object in Git in a human-readable format

Ignoring Patterns

git config --global core.excludesfile [file]: System-wide ignore pattern for all local repositories
logs/
*.notes
pattern*/

Save a file with desired patterns as .gitignore with either direct string matches or wildcard globs.
