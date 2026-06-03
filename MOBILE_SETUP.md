# Mobile Development Setup Guide

This guide covers how to get started with development on your mobile device using VS Code and the GitHub mobile app.

## Table of Contents

1. [VS Code on Mobile](#vs-code-on-mobile)
2. [GitHub Mobile App Setup](#github-mobile-app-setup)
3. [Recommended Workflows](#recommended-workflows)
4. [Tips & Tricks](#tips--tricks)

---

## VS Code on Mobile

### Option 1: GitHub Codespaces (Recommended)

**GitHub Codespaces** provides a cloud-based VS Code experience accessible from any device, including mobile.

**Steps:**

1. Go to your GitHub repository on mobile
2. Press `.` (period key) or click the **Code** button → **Codespaces** → **Create codespace on main**
3. Wait for the environment to initialize (usually 1-2 minutes)
4. VS Code will load in your browser with full terminal and editor access
5. Edit files, commit, and push changes directly from Codespaces

**Pros:**
- Full VS Code experience in the browser
- Pre-configured development environment
- No local setup required
- Automatic saving

**Cons:**
- Requires internet connection
- Limited by browser performance on mobile
- May incur Codespaces usage minutes

### Option 2: VS Code on iPad with SSH

**Requirements:**
- iPad with iPad OS 15+
- Git installed on your development machine or server
- SSH key configured

**Steps:**

1. Install **"VS Code for iPad"** or use **"Prompt 3"** app (terminal SSH client)
2. Connect via SSH to a remote development machine/server
3. Use the terminal to clone the repo: `git clone https://github.com/colleenpridemore/Molten.git`
4. Edit files using nano, vim, or VS Code remote extension
5. Use git commands via terminal to commit and push

**Pros:**
- Works offline (once connected to remote machine)
- Full coding capabilities
- Direct SSH access

**Cons:**
- Requires remote server setup
- More complex configuration
- iPad-specific apps may have limitations

### Option 3: Mobile Code Editors (Browser-based)

**Free Alternatives:**

- **Repl.it / Replit** — Cloud IDE accessible from any browser
- **GitPod** — Browser-based VS Code with GitHub integration
- **CloudIDE** — Remote development environment

**Steps:**

1. Visit [Gitpod.io](https://www.gitpod.io) and sign in with GitHub
2. Paste your repository URL: `https://github.com/colleenpridemore/Molten`
3. Click "Continue" → A cloud VS Code instance opens
4. Start developing with full terminal access
5. Changes auto-sync to your GitHub repository

---

## GitHub Mobile App Setup

### Initial Setup

1. **Download the App:**
   - iOS: [GitHub App on App Store](https://apps.apple.com/us/app/github/id1477376905)
   - Android: [GitHub App on Google Play](https://play.google.com/store/apps/details?id=com.github.android)

2. **Sign In:**
   - Launch the app
   - Tap **Sign In**
   - Authenticate with your GitHub credentials or biometric login
   - Grant necessary permissions

3. **Add Your Repository:**
   - Tap the **profile icon** (bottom right)
   - Select **Repositories** → Search for "Molten"
   - Tap to view your repository

### Essential Mobile App Features

| Feature | What It Does | How to Access |
|---------|-------------|---------------|
| **Browse Code** | View files and file contents | Tap file names in repository tree |
| **View Issues** | See all open/closed issues | **Issues** tab at top |
| **Create Issues** | Report bugs or feature requests | **+** button → New Issue |
| **Review PRs** | Comment on and approve pull requests | **Pull Requests** tab → Select PR |
| **Commit History** | View commit logs and changes | **Commits** tab in any branch |
| **Manage Branches** | Switch between and compare branches | Tap branch name at top |
| **Notifications** | See mentions, reviews, and updates | Bell icon (top left) |

### Common Mobile Workflows

#### Reading Issues/PRs
1. Open GitHub app → your repository
2. Tap **Issues** or **Pull Requests**
3. Tap any item to view details
4. Scroll to see description, comments, and checks

#### Commenting on Issues
1. Open an issue in the GitHub app
2. Scroll to the bottom
3. Tap the **comment field**
4. Type your response (supports Markdown)
5. Tap **Comment**

#### Creating a Quick Issue
1. Tap **+** button (bottom toolbar)
2. Select **New Issue**
3. Fill in **Title** and **Description**
4. Add labels or assignees if needed
5. Tap **Create Issue**

#### Reviewing a Pull Request
1. Go to **Pull Requests** tab
2. Select a PR
3. Review the **Files Changed** tab
4. Tap any line to add inline comments
5. Submit your review with approval or requested changes

---

## Recommended Workflows

### Workflow 1: Mobile-Only (Minimal Coding)
**Best for:** Browsing, reviewing, and managing issues

1. Use **GitHub Mobile App** to:
   - Read and respond to issues
   - Review and comment on pull requests
   - Manage project tasks
2. Use **Codespaces** when you need to:
   - Make quick edits to configuration files
   - Write documentation
   - Fix typos

### Workflow 2: Mobile + Remote Development (Full Coding)
**Best for:** Serious development work

1. Set up **Codespaces** or **GitPod** as your development environment
2. Use **GitHub Mobile App** for:
   - Committing and pushing changes
   - Creating pull requests
   - Managing reviews
3. Use **browser-based VS Code** for:
   - Coding and debugging
   - Running tests
   - Terminal access

### Workflow 3: Hybrid (Desktop + Mobile)
**Best for:** Using mobile as a secondary device

1. **On Desktop:**
   - Perform heavy development
   - Run complex builds and tests
   - Push to your branch

2. **On Mobile:**
   - Monitor CI/CD pipelines
   - Review and respond to feedback
   - Keep documentation updated
   - Check notifications

---

## Tips & Tricks

### Mobile-Specific Tips

✅ **DO:**
- Use Codespaces for serious coding—it's the best mobile experience
- Enable dark mode in GitHub app for easier reading
- Use keyboard shortcuts in Codespaces (Cmd+Shift+P for command palette)
- Pin important repositories to your home screen for quick access
- Set notifications to only alert for mentions and PRs assigned to you

❌ **DON'T:**
- Attempt large refactorings on mobile without a proper IDE
- Ignore merge conflicts—resolve them on desktop if possible
- Try to run heavy processes in Codespaces (they have resource limits)
- Keep the app open in the background—it drains battery quickly

### Keyboard Shortcuts in Codespaces (iPad/Phone Browser)

| Shortcut | Action |
|----------|--------|
| `Ctrl/Cmd + S` | Save file |
| `Ctrl/Cmd + Z` | Undo |
| `Ctrl/Cmd + Y` | Redo |
| `Ctrl/Cmd + /` | Toggle comment |
| `Ctrl/Cmd + Shift + P` | Open command palette |
| `Ctrl/Cmd + K Ctrl/Cmd + C` | Add comment (block) |

### Battery & Data Saving

- **Codespaces:** Codespaces sessions close after 30 minutes of inactivity to save resources
- **GitHub App:** Disable image previews in settings to reduce data usage
- **WiFi First:** Always use WiFi for large operations (cloning, syncing)
- **Low Power Mode:** iOS/Android low power mode is compatible with most workflows

---

## Troubleshooting

### Issue: Codespaces Takes Too Long to Load
**Solution:** Refresh the page, or check your internet connection. Codespaces typically loads in 1-2 minutes.

### Issue: Can't Push Changes from Mobile
**Solution:** 
- Ensure you're authenticated in Codespaces
- Try the Git: Pull command first to sync latest changes
- Check that your SSH key is configured in GitHub settings

### Issue: Mobile Browser Keeps Freezing
**Solution:**
- Close unnecessary tabs
- Clear browser cache
- Try a different browser (Chrome, Safari, Firefox)
- Use the native GitHub app instead of browser

### Issue: GitHub App Won't Sync Changes
**Solution:**
- Force close and reopen the app
- Re-authenticate (log out and log back in)
- Check internet connection
- Ensure repository isn't in a read-only mode

---

## Next Steps

1. **Try Codespaces first** — it's the quickest way to get started
2. **Bookmark this guide** on your mobile device for quick reference
3. **Explore the GitHub app** to familiarize yourself with mobile workflows
4. **Customize your notifications** to stay updated without distractions

Happy coding on the go! 🚀