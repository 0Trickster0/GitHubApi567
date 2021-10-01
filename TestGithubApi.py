import unittest
from GithubApi import *


class GithubApiTest(unittest.TestCase):
    def test_parse_github_info(self):
        right_str = ["Repo: 001, Number of commits: 0", "Repo: GitHubApi567, Number of commits: 6",
                     "Repo: myTensorflow, Number of commits: 0", "Repo: So_We_Date, Number of commits: 15",
                     "Repo: SSW567WS, Number of commits: 8", "Repo: Steps, Number of commits: 7",
                     "Repo: Student-Repository, Number of commits: 6"]
        i = 0
        for commit_info in parse_github_info('0Trickster0'):
            self.assertEqual(right_str[i], commit_info)
            i += 1


if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)
