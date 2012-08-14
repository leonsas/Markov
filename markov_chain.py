import random

class Markov:
	
	chain_dict={}
	def generate_chain(self):
		f=open("test.txt","r")
		words=[""]*2
		
		for line in f:
			for word in line.split():
				curr_key=words[0]+' '+words[1]
				if curr_key in self.chain_dict:
					self.chain_dict[curr_key].append(word)
				else:
					self.chain_dict[curr_key]=[word]
				words[0]=words[1]
				words[1]=word
				
	def generate_sentence(self, length=26):
		sentence=""
		debug_chain=[]
		#set seed(first word)
		key=random.choice(self.chain_dict.keys())
		w=[""]*2
		
		for i in range(0,length):
			w[0]=key.split()[0]
			w[1]=key.split()[1]
			word=random.choice(self.chain_dict[w[0]+" "+w[1]])
			sentence+=" "+word
			key=w[1]+" "+word
			debug_chain.append((key,word))
			
		print sentence
		#print debug_chain	