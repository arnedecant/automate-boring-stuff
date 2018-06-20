#! python3

import os

totalSize = 0
workingDir = 'd:\\Cloudstation\\Afbeeldingen'

for filename in os.listdir(workingDir):
	if not (os.path.isfile(os.path.join(workingDir, filename))):
		continue
	totalSize = totalSize + os.path.getsize(workingDir + '\\' + filename)

print('The total filesize in ' + workingDir + ' is:')
print(str(totalSize) + ' Bytes (' + str(round(totalSize / 1024 / 1024, 2)) + ' MB)');
