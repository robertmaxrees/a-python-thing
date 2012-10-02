x = raw_input ("Would you like a sandwich? (y/n) ")

makeSand = 1
while makeSand == 1:
	if x.lower() == "y":
		print ""
		print "                   _.---._ "
		print "               _.-~       ~-._ "
		print "           _.-~               ~-._ "
		print "       _.-~                       ~---._ "
		print "   _.-~                                 ~\ "
		print ".-~                                    _.; "
		print ":-._                               _.-~ ./ "
		print "}-._~-._                   _..__.-~ _.-~) "
		print "`-._~-._~-._              / .__..--~_.-~ "
		print "    ~-._~-._\.        _.-~_/ _..--~~ "
		print "        ~-. \`--...--~_.-~/~~ "
		print "           \.`--...--~_.-~ "
		print "             ~-..----~ "
		print ""
		yum = raw_input ("Was that delicious? ")
		if yum.lower() == "y":
			print ("Good, I'm glad! ")
		elif yum.lower() == "n":
			print ("Oh, I'm sorry! ")
		raw_input ("Press Return to exit")
		makeSand = 2
	elif x.lower() == "n":
		print "No sandwich for you :("
		raw_input ("Press Return to exit")
		makeSand = 2