using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;

namespace HelloWorld
{
    class Word 
    {
        // Definition of variables
        public string word {get; set;}
        public List<string> subwords {get; set;}

        // Initialization
        public Word(string word)
        {
            this.word = word;
            this.subwords = makeSubwords(word);
        }

        private List<string> makeSubwords(string word)
        //Create a list of subwords for a word
        //    word:: string, a word
        //>> list of subwords
        
        {
            var subwordsList = new List<string> {};
            for(int i = 0; i <= word.Length; i++)
                {
                    subwordsList.Add(word.Substring(0,i));
                }
            return subwordsList;

        }
    }

    class Autofill
    {
        // Definitions of variables (new here not in Python)
        public List<Word> data {get; set;}
        public List<string> outputWords {get; set;}

        // Construction of variables (init in Python)
        Autofill()
        {
            this.data = new List<Word>() {};
            this.outputWords = new List<string> {};
        }

        
        public void Build(List<string> inputWords)
        {
            foreach(string w in inputWords)
            {   
                Word i = new Word(w);
                data.Add(i);
            }
        }

        public void Find(string input)
        {
            foreach(Word w in data)
            {
                if (w.subwords.Contains(input))
                {
                    outputWords.Add(w.word);
                }
            }
        }

        public void getResult()
        {
            Console.WriteLine("The following words are found:");
            foreach(string w in outputWords)
            {
                Console.WriteLine(w);
            }
        }
        

        static void Main(string[] args)
        {
            List<string> words = new List<string> {"foo", "bar", "help", "falcon", "flipper", "jargon", "business", "hooray", "hell"};
            
            Autofill test = new Autofill();
            test.Build(words);
            test.Find("he");
            test.getResult();
        }
    
    }
}
