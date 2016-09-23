# Author: Jason Mazzatenta

from matplotlib import pyplot
import scipy.io as sio


class Data:
    def __init__(self, n, r, elecI, seq, data):
        self.n = n
        self.r = r
        self.elecI = elecI
        self.seq = seq
        self.data = data

    def Debug(self):
        print(self.n, self.r, self.elecI, self.seq, self.data)

    def ShowData(self, elecI):
        self.MakeChart(elecI)
        pyplot.show()

    def SaveFig(self, elecI, seq):
        self.MakeChart(elecI)
        pyplot.savefig("C:/Users/jdm_2/Downloads/train_1/charts/1_" +
                       str(seq) + "_0.png")
        pyplot.clf()  # clear canvas

    def MakeChart(self, elecI):
        elecI -= 1
        if elecI < 0:
            print("Invalid electrode")
            return
        elecIData = []
        rng = range(0, len(self.data))
        for i in rng:
            elecIData.append(self.data[i, elecI])
        time = [x / (self.r * 60) for x in range(0, len(elecIData))]
        pyplot.plot(time, elecIData)
        pyplot.xlabel("Time (min)")
        pyplot.ylabel("Electrode Reading (" + str(elecI + 1) + ")")


for j in range(1, 1153):
    filepath = "C:/Users/jdm_2/Downloads/train_1/train_1/1_" + str(j) + "_0.mat"
    matfile = sio.loadmat(filepath, squeeze_me=True, struct_as_record=False)
    md = matfile["dataStruct"]
    d1 = Data(md.nSamplesSegment, md.iEEGsamplingRate, md.channelIndices,
              md.sequence, md.data)
    d1.Debug()
    # d1.ShowData(1)
    d1.SaveFig(1, j)
