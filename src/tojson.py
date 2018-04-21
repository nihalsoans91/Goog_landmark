import os

f = open("index.txt", "r")		# input file in which hashes are stored
op = open("hashes.json", "w")	# output json file in format {id: _, hash: _}
op.write('[\n')

_id = ""
_hash = []
imcount = 0

for word in f.read().split():
	if ':' in word:  			# start of new hash
        imcount += 1
        if word[-1] == '[':
            _id = word[:-3]
        else:
            _id, h = word.split('.:[')
            _hash += [float(h)]
	
	elif ']' in word:			# end of hash
		if word[0] == ']':
            pass
        else:
            h = float(word[:-1])
            _hash += [h]

        # write to file after last line of each hash is read
        op.write('{\n')
        op.write('\t"id": "%s",\n' % _id)
        op.write('\t"hash": [')

        for h in _hash[:-1]:
            op.write('%.5f,' % h)
        op.write('%.5f]\n' % _hash[-1])  # last element of hash (should avoid ',')
        op.write('},\n')

		# reset id and hash
		_id = ""
		_hash = []
		
		# signal for every 1000 images
    	if imcount % 1000 == 0:
        	print(imcount, "images converted")

	else:						# internal hash values
		_hash += [float(word)]

op.write(']')
print("# of images: ", imcount)

op.close()
f.close()