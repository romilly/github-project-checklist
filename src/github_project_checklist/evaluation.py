import requests

def get_github_project_info(owner, repo, token):
    # Define the headers with the token for authentication
    headers = {
        'Authorization': f'token {token}',
        'Accept': 'application/vnd.github.v3+json'
    }

    # API endpoints
    repo_url = f'https://api.github.com/repos/{owner}/{repo}'
    issues_url = f'{repo_url}/issues'
    pulls_url = f'{repo_url}/pulls'

    # Get general repository information
    repo_info = requests.get(repo_url, headers=headers).json()
    last_update = repo_info.get('updated_at')
    watchers_count = repo_info.get('subscribers_count')
    stars_count = repo_info.get('stargazers_count')
    forks_count = repo_info.get('forks_count')

    # Get issues information
    issues = requests.get(issues_url, headers=headers, params={'state': 'all'}).json()
    total_issues = len(issues)
    unresolved_issues = len([issue for issue in issues if issue['state'] == 'open'])
    oldest_issue_date = min(issues, key=lambda x: x['created_at'])['created_at'] if issues else None

    # Get pull requests information
    pulls = requests.get(pulls_url, headers=headers, params={'state': 'all'}).json()
    resolved_pulls = [pull for pull in pulls if pull['state'] == 'closed']
    average_time_to_close_pr = (sum((pd.to_datetime(pull['closed_at']) - pd.to_datetime(pull['created_at'])).days for pull in resolved_pulls) / len(resolved_pulls)) if resolved_pulls else 0

    # Output the results
    print(f"Last updated on: {last_update}")
    print(f"Total issues: {total_issues}, Unresolved issues: {unresolved_issues}")
    print(f"Oldest unresolved issue date: {oldest_issue_date}")
    print(f"Average time to close a pull request: {average_time_to_close_pr} days")
    print(f"Watchers: {watchers_count}, Stars: {stars_count}, Forks: {forks_count}")

# Example usage
get_github_project_info('owner_name', 'repo_name', 'your_github_token')
