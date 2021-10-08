import unittest
from unittest import mock
import GithubApi


class GithubApiTest(unittest.TestCase):
    @mock.patch('GithubApi.parse_github_info')
    def test_parse_github_info(self, mock_parse_github_info):
        mock_parse_github_info.return_value = \
            ["Repo: 001, Number of commits: 0", "Repo: GitHubApi567, Number of commits: 6",
             "Repo: myTensorflow, Number of commits: 0", "Repo: So_We_Date, Number of commits: 15",
             "Repo: SSW567WS, Number of commits: 10", "Repo: Steps, Number of commits: 7",
             "Repo: Student-Repository, Number of commits: 6"]
        right_str = ["Repo: 001, Number of commits: 0", "Repo: GitHubApi567, Number of commits: 6",
                     "Repo: myTensorflow, Number of commits: 0", "Repo: So_We_Date, Number of commits: 15",
                     "Repo: SSW567WS, Number of commits: 10", "Repo: Steps, Number of commits: 7",
                     "Repo: Student-Repository, Number of commits: 6"]
        for i in range(len(right_str)):
            self.assertEqual(right_str[i], mock_parse_github_info()[i])


if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)
