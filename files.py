filename = 'test.txt'
test_text = 'this is my text!!!!!'

# f = open(filename, 'w')
f = open(filename, 'a')
# w means everything in the file will be overwritten
# a append to the end of the file
f.write(test_text)
f.close()