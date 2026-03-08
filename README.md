# devrel-public-workshops

Archive of workshops for public events, managed by the DevRel team.

This repo contains public Airflow and Astro workshops given by Astronomer's DevRel team. To find code for your workshop, choose the appropriate branch.

Current workshops are managed in the `astronomer/devrel-public-workshops` repository.

# Restore a branch from the archive repo

## 1. Clone the main repo (if not already done)

```bash
git clone git@github.com:astronomer/devrel-public-workshops.git
cd devrel-public-workshops
```

## 2. Add the archive as a temporary remote

```bash
git remote add archive git@github.com:astronomer/devrel-public-workshops-archive.git
git fetch archive
```

## 3. Push the branch to origin

Replace `<branch-name>` with the branch you want to restore, e.g. `dbt-in-airflow`.

```bash
git push origin archive/<branch-name>:refs/heads/<branch-name>
```

## 4. Remove the archive remote

```bash
git remote remove archive
```

## 5. Verify

```bash
git branch -r
```

The restored branch should now appear as `origin/<branch-name>`.
