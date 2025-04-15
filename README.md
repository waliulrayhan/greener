# Green Commits Automation

A GitHub Actions workflow that automatically creates realistic commit patterns to maintain an active GitHub profile. This project helps you maintain a consistent commit history while focusing on your actual work.

## Features

- 🕒 Time-appropriate commit messages based on your local timezone (GMT+6)
- 📊 Realistic commit patterns that vary by time of day
- 🌙 Night owl mode for late-night coding sessions
- 📈 Increased commit frequency for better activity visualization
- 🔄 Automatic scheduling with GitHub Actions
- 🌍 Timezone-aware (supports GMT+6/Bangladesh time)

## How It Works

The project consists of two main components:

1. **Python Script (`green_commit.py`)**
   - Generates realistic commit messages based on time of day
   - Creates natural commit patterns
   - Maintains an activity log with GMT+6 timestamps
   - Adjusts commit frequency based on weekday/weekend

2. **GitHub Actions Workflow (`.github/workflows/green-commits.yml`)**
   - Runs automatically on schedule
   - Handles git operations
   - Manages authentication and permissions
   - Ensures proper synchronization

## Installation

1. Fork this repository
2. Go to your repository settings
3. Add a Personal Access Token (PAT) with `repo` permissions:
   - Go to GitHub Settings → Developer Settings → Personal Access Tokens
   - Create a new token with `repo` scope
   - Add it to your repository secrets as `PERSONAL_ACCESS_TOKEN`

### Important Note for Public Repositories
When using this in a public repository:
- The PAT should be stored as a repository secret
- The token should have minimal required permissions
- Never share or expose your PAT in the code
- Consider using a dedicated GitHub account for automation

## Configuration

The workflow is configured to run at these times (Bangladesh time/GMT+6):

- Weekdays:
  - Evening: 8:35 PM - 10:35 PM
  - Late Night: 11:15 PM - 1:15 AM
- Weekends:
  - Extended Night: 10:42 PM - 2:42 AM

You can adjust these times by modifying the cron schedules in `.github/workflows/green-commits.yml`.

## Customization

### Commit Messages

Edit `green_commit.py` to customize:
- Commit message templates
- Commit frequency
- Time-based message selection
- Session patterns

### Schedule

Modify `.github/workflows/green-commits.yml` to adjust:
- Run times
- Timezone settings
- Authentication method
- Git configuration

## Security Considerations

When using this in a public repository:
1. Use a dedicated GitHub account for automation
2. Create a PAT with minimal permissions
3. Never commit the PAT to the repository
4. Regularly rotate your PAT
5. Monitor the repository for any suspicious activity

## Contributing

Feel free to submit issues and enhancement requests!

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Disclaimer

This tool is meant to help maintain a consistent GitHub activity pattern. Use it responsibly and in accordance with GitHub's terms of service. The maintainers are not responsible for any misuse of this tool. 