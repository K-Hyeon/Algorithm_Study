{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "5a1b57b5-c982-40b6-8803-4ecafdc51f40",
   "metadata": {},
   "outputs": [],
   "source": [
    "import sys\n",
    "input = sys.stdin.readline\n",
    "\n",
    "N, M = map(int, input().split())\n",
    "array = [int(input()) for _ in range(N)]\n",
    "array.sort()\n",
    "\n",
    "min_sub = 1e9 * 2\n",
    "left, right = 0, 1\n",
    "while right < N:\n",
    "    sub = array[right] - array[left]\n",
    "    if sub < M:\n",
    "        right += 1\n",
    "    elif sub > M:\n",
    "        min_sub = min(min_sub, sub)\n",
    "        left += 1\n",
    "    else:\n",
    "        min_sub = M\n",
    "        break\n",
    "print(min_sub)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
