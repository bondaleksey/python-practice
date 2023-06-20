# if in Win need start in GitBash
import subprocess, locale

procObj = subprocess.run(["ls", "-al"], stdout=subprocess.PIPE)
# procObj = subprocess.run(["DIR", ".", "AH"], stdout=subprocess.PIPE)
outputStr = procObj.stdout.decode(locale.getdefaultlocale()[1])
print(outputStr)
