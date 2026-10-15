# Cowork capability check

**How to use this:**
1. In the Claude desktop app, open **Cowork** and start a new task.
2. Connect a folder: create `~/DelOps/cowork-check` (an empty folder) and connect it.
3. Paste everything below the line into the chat.

The check only reads information and writes one report file. It doesn't install, change or delete anything.

---

Please run a read-only capability check of this Cowork environment and write the results to a file named `cowork-capabilities.md` in the connected folder. Don't install, change or delete anything. If a check needs something unavailable, record "not available" and move on. Don't print any tokens, passwords or secrets, and summarize auth status as "signed in" or "not signed in" only.

Check and report, one short line each:

1. **Session:** is this a local session (running on my computer) or a cloud session? What OS and CPU architecture does the shell report?
2. **Folder access:** the full path of the connected folder as you see it. Can you create a file there? (Writing the report proves it.)
3. **Shell and languages:** which shell tool you use to run commands, plus the versions of `python3`, `node`, `npm`, `git`, `gh` and `pip` (or "not available").
4. **Python packages:** for each of `yaml`, `jsonschema`, `docx`, `reportlab`, `openpyxl`, `PIL`, `matplotlib`, say whether it imports.
5. **Document tools:** whether each of these is on the PATH: `pandoc`, `soffice` (LibreOffice), `pdftoppm`, `convert` or `magick` (ImageMagick), `chromium` or `google-chrome`, `rsvg-convert`, `mmdc`.
6. **Node packages:** whether `npx --yes` would be allowed (don't run an install). Also report `npm config get registry`, and whether `node -e "require('docx')"`, `require('pptxgenjs')` and `require('sharp')` succeed.
7. **Network:** for each URL, the HTTP status of a HEAD request with a 10-second timeout, or "blocked": https://pypi.org, https://registry.npmjs.org, https://github.com, https://api.github.com, https://mcp.monday.com/mcp, https://storage.googleapis.com
8. **Git and GitHub:** is `gh auth status` signed in (yes/no only)? Could `git ls-remote` against a non-existent repository under the user's GitHub account authenticate? Just report the error type.
9. **Built-in skills:** list the skills and plugins you can see (names only), and say whether docx, pdf and pptx skills are available.
10. **Subagents:** can you start a subagent or task agent in this session (yes/no, and the tool name)?
11. **monday connector:** is it connected? If so, the exact tool-name prefix of one of its read tools (for example the full name of the tool that gets user context). Don't call any monday tool that changes anything.
12. **Web:** are web search and web fetch available (yes/no, tool names)?
13. **Memory and instructions:** do you see any project instructions or memory for this task (yes/no)?

End the file with a one-paragraph plain-English summary of what this environment can and can't do for:
- running small Python or Node scripts
- making Word, PDF and slide files
- turning diagrams into images
- pushing to a private GitHub repo
