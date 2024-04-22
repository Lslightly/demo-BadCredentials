import pickle
import tomllib
from github import BadCredentialsException
import pytest
from github.Issue import Issue

def test_bad_credentials():
    with open("badCredentials.pickle", "rb") as pickelf:
        issue: Issue = pickle.load(pickelf) # broken issue
        with pytest.raises(BadCredentialsException):
            print(issue.repository.full_name) # will raise Bad Credentials Exception because of expired/invalid token
        try:
            issue._requester.auth._token = "ghp_xxxx" # TODO new token
            print(issue.repository.full_name)
            assert True     # replacing with generated token should now work.
        except Exception as e:
            assert False, f"replace token still raise exception:\n{e}"
            