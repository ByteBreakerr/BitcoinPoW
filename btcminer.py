from hashlib import sha256
from argparse import ArgumentParser

def mine_btc(target,difficulty,limit=None):
	nonce = 0
	while(True):
		if limit != None:
			if nonce == limit:
				return "Limit reached"

		our_hash = sha256(("string" + str(nonce)).encode()).hexdigest() 

		if our_hash.startswith(target[:int(difficulty)]):
			print("[+] HASH FOUND!")
			print("Given hash: " + "\033[91m" + target[:difficulty] + '\033[0m' + target[difficulty:])
			return f"Hash: \033[91m{our_hash[:int(difficulty)]}\033[0m{our_hash[int(difficulty):]}\n\033[92mNonce:{nonce:,}\033[0m"
		nonce += 1

def main():
	parser = ArgumentParser(description="BTC miner demo")
	parser.add_argument('-t','--target',dest='target',help='target hash')
	parser.add_argument('-d','--difficulty',dest='difficulty',help='difficulty level of network',type=int)
	parser.add_argument('-l','--limit',dest='limit',help='nonce limit',type=int)

	args = parser.parse_args()

	if (args.target and args.difficulty):
		print("INPUT HASH:",args.target)
		print("FINDING THE HASH....")
		if args.limit:
			print(mine_btc(args.target,args.difficulty,args.limit))
		else:
			print(mine_btc(args.target,args.difficulty))
	else:
		parser.print_usage()

if __name__ == "__main__":
	main()