## Revert
```bash
# Revert that one specific commit
git revert <commit_hash>

# This will create three separate revert commits:
git revert a867b4af 25eee4ca 0766c053

# Revert the range of changes
git revert <oldest_commit_hash>..<latest_commit_hash>
git revert HEAD~2..HEAD

# Revert the range of changes with one commit
git revert --no-commit 0766c053..HEAD
git commit

# To get just one, you could use `rebase -i` to squash them afterwards
# Or, you could do it manually (be sure to do this at top level of the repo)
# get your index and work tree into the desired state, without changing HEAD:
git checkout 0d1d7fc32 .

# Reverting a merge commit
git revert -m 1 <merge_commit_sha>
```
* http://stackoverflow.com/a/4114122
* https://github.com/blog/2019-how-to-undo-almost-anything-with-git
* http://schacon.github.io/git/howto/revert-a-faulty-merge.txt

## Abandon local changes
```bash
git reset --hard <destination_commit>
```

## Move a single commit from another branch
```bash
git cherry-pick <commit_hash>

# Inclusive: Including older_commit
git cherry-pick <older_commit>^..<newer_commit>

# Exclusive
git cherry-pick <older_commit>..<newer_commit>
```
* https://backlogtool.com/git-guide/kr/stepup/stepup7_4.html

## [Remove partially from old commits](http://stackoverflow.com/a/15321456)
```bash
git reset --soft HEAD~1
// or
git reset --soft HEAD^

// Then
git reset HEAD path/to/unwanted_file

// Finally
git commit -c ORIG_HEAD  
```
**Thanks for this. It's worth adding that if you have already pushed your earlier (wrong) commit, and now try to `git push` your fix up to your repo, it will complain `Updates were rejected because the tip of your current branch is behind its remote counterpart.`. If you're sure that you want to push them (e.g. it's your fork) then you could use the -f option to force the push, e.g. `git push origin master -f`. (Do not do this to an upstream repo that others are fetching from) "
##
```bash

```

##
```bash

```

##
```bash

```

##
```bash

```

##
```bash

```

##
```bash

```

##
```bash

```

##
```bash

```

##
```bash

```

##
```bash

```

##
```bash

```

##
```bash

```
