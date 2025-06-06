from list_files import list_files_in_branch


def test_list_files_in_branch_contains_project_files():
    files = list_files_in_branch('HEAD')
    assert 'README.md' in files
    assert 'requirements.txt' in files
