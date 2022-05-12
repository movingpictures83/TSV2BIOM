class TSV2BIOMPlugin:
    def input(self, filename):
        self.infile = open(filename, 'r')
           

    def run(self):
        pass

    def output(self, filename):
        self.infile.readline() #First, ignore
        outfile = open(filename, 'w')
        outfile.write("#OTUid\ttaxonomy\tconfidence\n")
        for line in self.infile:
            outfile.write(line)
