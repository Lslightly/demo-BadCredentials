# description for files

# use case

Caching `Issue` object, returned by `pygithub` `get_issues()` API with a classic personal access token,
in the file system using `pickle` library. Then the token is expired and regenerated, which makes the `Issue` object invalid.

When `pickle.load` this `Issue` object and visiting `repository.full_name` property, the exception of Bad Credentials occurs.

# steps to reproduce using files from this repository

1. install python 3.11
2. `python -m venv venv`
3. `source venv/bin/activate`
4. `pip install -r requirements.txt`
5. create a personal access token A with full permissions for testing.
6. update `TODO` in [test_bad_credentials.py](test_bad_credentials.py)
7. use `pytest` to run [test_bad_credentials.py](test_bad_credentials.py)

# steps to reproduce from scrath

1. create a personal access token A with full permissions for testing. The format of token A can be `ghp_...`.
2. cache a `pygithub` object O with token A. 
3. regenerate/expire/delete token A
4. load object O and visit its properties like `repository`/`totalCount`. Bad Credentials will occur.

# take away

The old token causes Bad Credentials. Regeneration of token invalid the object in the cache system.

**Pay much attetion to the consistency of cache system!!!**
