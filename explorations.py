"""
write things!!
"""

from mne import Epochs, find_events
from mne.io import read_raw_edf

###############
# Import Data #
###############

# Define Paths
# TODO: automate based on brefix names (with muse prefixes are before the underscore).
filePath = "MuseData/"
beforePracticeFile = filePath + "Before Mindfulness_Muse-BE53_2019-01-26--15-44-02_1548546368888.edf"
afterPracticeFile = filePath + "Post Muse 5 min v4.2_Muse-BE53_2019-01-26--15-56-03_1548547065702.edf"


# Read Raw Data
# TODO 1: This should be all that is needed. There is a chance I need to mess with the
# channels or annotate the data to get at least more detailed readings.
# TODO 2 automate based on Path automation above.

beforePracticeRawData = read_raw_edf(beforePracticeFile, stim_channel="auto", preload=True)
afterPracticeRawData = read_raw_edf(afterPracticeFile, stim_channel="auto", preload=True)

# this is just for beforePracticeRawData

#############
# Read Data #
#############

class BasicBrainData(object):
    """
    description TODO: write

    Attributes (two raw edf files to compare):
        before: edf file from readings *before* some event
        after: edf file from readings *after* some event
    """

    def __init__(self, before, after):
        """Returns a BasicBrainData Object with before and after attributes"""
        self.before = before.pick_types(eeg=True, exclude='bads')
        self.after = after.pick_types(eeg=True, exclude='bads')
        #define brain wave bands
        self.bands=[
            (.5, 4, "Delta"),
            (4, 8, "Theta"),
            (8, 12, "Alpha"),
            (12, 30, "Beta"),
            (30, 100, "Gamma")
        ]

    def getAveragesOverBrainWaves(self, data):
        # initialize dictionary
        self.averagedData = {
        "Delta": 0,
        "Theta": 0,
        "Alpha": 0,
        "Beta": 0,
        "Gamma": 0
        }

        # iterate over bands to find the average volts per band over the whole time
        for fmin, fmax, name in self.bands:
            filteredData = data.filter(fmin, fmax)
            flattenedData = [y for x in filteredData.get_data() for y in x]
            average = sum(flattenedData) / float(len(flattenedData))
            self.averagedData[name] = average

        return self.averagedData


    def compare(self):
        beforeDataAveraged = self.getAveragesOverBrainWaves(self.before)
        afterDataAveraged = self.getAveragesOverBrainWaves(self.after)
        print(beforeDataAveraged, afterDataAveraged)


mindfulnessData = BasicBrainData(beforePracticeRawData, afterPracticeRawData)
mindfulnessData.compare()
