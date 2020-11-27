# captcha-research
#### captcha-statistics.py
A script for captcha recognition.
###### The script recieves an image of some captcha, and attempts to remove the noise surrounding the alphanumeric characters. At that point, OCR tools [such as this one](https://github.com/tesseract-ocr/tesseract) can read it with reasonable accuracy. My aim, assuming the captcha is of the same "style" as some others previously stored and analyzed, is to compare letters _(in an admittetedly primitive way)_, perhaps with hints from an OCR tool, and determine with much more reliability the text of the captcha. This only works ofcourse, only when characters can be "untangled" from the mess, in a way that keeps the "macro" features of the character intact.
##### It is still a work in progress. I haven't yet figured out how best to do that.
