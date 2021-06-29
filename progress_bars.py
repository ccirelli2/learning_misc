"""
Ref : https://dev.to/rsalmei/a-cool-new-progress-bar-for-python-1c0g
"""

from alive_progress import alive_bar
import time


for i in range(10):
    print("progress", end='')
print('\n')
