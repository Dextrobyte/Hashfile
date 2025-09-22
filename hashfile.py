'''

this python script calculates SHA256,SHA512,MD5
hash of a file provided as an input argument.This script only use python3 inbuilt modules so no extra dependencies needed besides python ofcourse

Author-Dextrobyte
github-https://github.com/Dextrobyte
license- GPLv3




This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or 
any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.
You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.



'''
#chunk size to read in one go 
buffer_size = 65536

import hashlib
import sys
import time

startTime = time.time()
filePath = None
try:
	filePath = sys.argv[1]
except IndexError:
	print ("\033[31mNo file path provided\033[0m")
	exit()
except :
	print("\033[31mSomething isn't right try again\033[0m")
	exit()
sha_256 = hashlib.sha256()
sha_512 = hashlib.sha512()
md_5 = hashlib.md5()


try:
	file = open(filePath, "rb")
except FileNotFoundError:
	print(f"\033[31mfile {filePath} not found try again\033[0m")
	exit()
except IsADirectoryError:
	print(f"\033[31m{filePath} is a directory not a file\033[0m")
	exit()
while True:
	if(not(bin)):
		break
	else:
		bin = file.read(buffer_size)

		sha_256.update(bin)
		sha_512.update(bin)
		md_5.update(bin)

sha256hash = sha_256.hexdigest()
sha512hash = sha_512.hexdigest()
md5hash    =    md_5.hexdigest()

print(f"SHA256: {sha256hash}\nSHA512: {sha512hash}\nMD5: {md5hash}\n")
endTime = time.time()
print(f"Time taken: {endTime-startTime}\n")