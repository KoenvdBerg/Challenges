#! bin/env/user python 3

# imports:

# Definitions:
class Consensus(object):

    def __init__(self, filename):
        """
        Initializes the objects attributes:
        self.filename = the input name of the file
        self.data = the data present in the file
        self.transposedata = the transposed DNA strands
        """
        self.filename = filename
        self.data = []
        self.transposedata = []
        try:
            with open(self.filename, "r") as f:
                for line in f:
                    line = line.strip()
                    if ">" not in line:
                        self.data.append(line)
        except IOError:
            raise IOError("{} not found in working directory".format(self.filename))
                        

    def TransposeData(self):
        """
        Transposes the DNA strands as strings
        """
        self.transposedata = list("".join(i) for i in zip(*self.data))

    def PrintDNA(self):
        """
        Prints the DNA from the file to the terminal
        """
        print("\nDNA strings:")
        for i in self.data:
            print("{}".format(i))
    
    def MatrixConsensus(self):
        """
        Finds the consensus matrix for the DNA data
        """
        listACGT = []
        for item in self.transposedata:
            listACGT.append([item.count("A"), item.count("C"), item.count("G"), item.count("T")])
        listACGT = [list(i) for i in zip(*listACGT)]
        ACGT = ["A", "C", "G", "T"]
        for i in range(len(listACGT)):
            print("{}\t{}".format(ACGT[i], " ".join(str(x) for x in listACGT[i])))
            

            
    


# Main script:
if __name__ == "__main__":
    
    data = Consensus("fasta.txt") # Input filename here
    data.TransposeData()
    data.PrintDNA()
    data.MatrixConsensus()
