# GitHub Project Analyzer

A Python script to fetch and analyze various metrics from GitHub repositories, such as the number of issues, pull requests, stars, forks, and more. It provides insights such as the total and unresolved issues, average time to close pull requests, and the oldest unresolved issue date.

## Features
- Analyze general repository statistics:
    - Stars ⭐
    - Forks 🍴
    - Watchers 👀
    - Last updated timestamp 📅

- Fetch and analyze issues:
    - Total issues
    - Unresolved issues
    - Oldest unresolved issue date

- Fetch and analyze pull requests:
    - Total pull requests
    - Resolved pull requests
    - Average time to close a pull request

- Handles pagination to process repositories with a large number of issues or pull requests.

## Requirements
- **Python >= 3.6**
- The following Python libraries:
    - `requests`
    - `pandas`
    - `python-dotenv`

You can install the required libraries with:
``` bash
pip install -r requirements.txt
```
## Usage
Before running the script, create a `.env` file in the root directory of your project and add your GitHub personal access token like this:
``` 
GITHUB_TOKEN=your_personal_github_token
```
Then, run the `evaluation.py` script to analyze a repository. You can modify the repository owner and name in the script's `get_github_project_info` call. For example:
``` python
get_github_project_info('owner', 'repo')
```
### Running the Script
Once your `.env` file is created, run the script as follows:
``` bash
python evaluation.py
```
### Example Output
Here’s what you might see when analyzing a repository:
``` 
Last updated on: 2023-10-10T10:00:00Z
Total issues: 152, Unresolved issues: 32
Oldest unresolved issue date: 2022-12-01T12:15:30Z
Pull requests: 50
Resolved pulls: 46
Average time to close a pull request: 3.5 days
Watchers: 205, Stars: 1300, Forks: 180
```
## Important Notes and Limitations
1. **GitHub API Rate Limits**:
    - Without a personal access token, GitHub API requests are limited to **60 requests per hour** per IP address.
    - For repositories with a large number of issues or pull requests, the script will hit the **rate limit quickly** if a token is not provided.
    - Adding a personal access token in the `.env` file increases the **rate limit to 5,000 requests per hour**.

2. **Performance**:
    - Analyzing repositories with a large number of pull requests or issues can be time-consuming due to GitHub API pagination. Be patient with large repositories!

3. **Error Handling**:
    - The script currently does not handle errors like invalid repository names or expired tokens gracefully. Make sure your inputs are correct.

## How to Get a GitHub Token
Follow these steps to create a GitHub personal access token:
1. Go to [GitHub Settings](https://github.com/settings/tokens).
2. Select **"Personal Access Tokens"** under **"Developer Settings"**.
3. Click **"Generate new token"** and enable the `repo` scope.
4. Copy the token and add it to the `.env` file as shown above.

## License
This project is open-source and available under the [MIT License](LICENSE).
