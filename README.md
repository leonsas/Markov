Markov
======

Very simple sentence generator using Markov chains.

To test it, run the following from a python console:

    from markov_chain import Markov
    gen=Markov()
    gen.generate_chain()
    gen.generate_sentence()
    
To change the length of the generated text, simply pass the desired length to the generate_sentence() method:

    gen.generate_sentence(50)