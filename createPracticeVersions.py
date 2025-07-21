# Script that creates "duplicate" versions of the exercise problems
# Run simply as `python createPracticeVersions.py`
import os
import re

idRegex = re.compile("(xml:id|label)=\"([^\"]*)\"")
titleRegex = re.compile(r"\<title\>HW(\d+)</title>")
allFiles = os.listdir("source")
practiceFiles = [f for f in allFiles if "practice" in f.lower()]
for f in practiceFiles:
  os.remove(os.path.join("source", f))
sectionFiles = [f for f in allFiles if f.startswith("sec-") if "practice" not in f.lower()]
for fname in sectionFiles:
  fullName = os.path.join("source", fname)
  with open(fullName, "r") as f:
    contents = "".join(f.readlines())
  newContents = idRegex.sub(lambda m: f"{m.group(1)}=\"{m.group(2)}-practice\"", contents)
  newContents2 = titleRegex.sub(lambda m: f"<title>HW{m.group(1)} Practice</title>", newContents)
  newFileName = os.path.join("source", fname.replace(".ptx", "-practice.ptx"))
  with open(newFileName, "w") as f:
    f.write(newContents2)
