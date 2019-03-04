# -*- coding: utf-8 -*-

"""
explorations.py is a short set of python scripts which currently compare two sets
of brain wave recordings and show the difference between them.

In a more finilized version, one would upload any neural oscillation data set(s)
and analyze them in a few ways.
"""

from mne import Epochs, find_events, set_log_level
from mne.io import read_raw_edf

import pprint
pp = pprint.PrettyPrinter()

from collections import defaultdict

# set logging level
set_log_level(verbose="WARNING")

###############
# Import Data #
###############

# Define Paths
# TODO: automate based on brefix names (with muse, prefixes are before the underscore)
filePath = "MuseData/"
beforePracticeFile = filePath + "Before Mindfulness_Muse-BE53_2019-01-26--15-44-02_1548546368888.edf"
afterPracticeFile = filePath + "Post Muse 5 min v4.2_Muse-BE53_2019-01-26--15-56-03_1548547065702.edf"


# Read Raw Data
# TODO 1: This should be all that is needed. There is a chance I need to mess with the
# channels or annotate the data to get at least more detailed readings.
# TODO 2 automate based on Path automation above and add it to the class.

beforePracticeRawData = read_raw_edf(beforePracticeFile, stim_channel="auto", preload=True)
afterPracticeRawData = read_raw_edf(afterPracticeFile, stim_channel="auto", preload=True)

#############
# Read Data #
#############

class BasicBrainData(object):
    """
    Description:
        This is a basic class whose purpose is to look at electrical impulses from
        the brain and do basic analytics to it

    Attributes:
        Editable (two raw edf files to compare):
            before: edf file from readings *before* some event
            after: edf file from readings *after* some event
        Static:
            bands: the frequeny bands most neural oscillations are catagorized into
        Returned:
            averagedData:
                data that has been flattened and averaged to see in which bands the
                most neural oscillations happened in
    """

    # TODO: make more flexable for other kinds of comparison and explorations
    #       e.g. delete before and after and allow for any amount of annotated data
    def __init__(self, before, after):
        """Returns a BasicBrainData Object with provided before & after attributes"""
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
        """iterate over bands to find the average volts per band over time."""
        # TODO 1: make sure the data has been correctly preprocessed.
        # TODO 2: evaluate this agaist known good analysis.
        # TODO 3: try a version with this split up into 1hz bands from .5 to 100.5
        #         and see if the Delta, Theta, etc bands make sense as constructs.
        # initialize dictionary
        averagedData = {
            "Delta": 0,
            "Theta": 0,
            "Alpha": 0,
            "Beta": 0,
            "Gamma": 0
        }
        for fmin, fmax, name in self.bands:
            filteredData = data.filter(fmin, fmax, verbose=None)
            flattenedData = [y for x in filteredData.get_data() for y in x]
            average = sum(flattenedData) / float(len(flattenedData))
            averagedData[name] = average

        return averagedData

    def compareBeforeAfter(self):
        """compares two data sets and returns data plus diffrenes"""
        compareData = defaultdict(list)
        beforeDataAveraged = self.getAveragesOverBrainWaves(self.before)
        afterDataAveraged = self.getAveragesOverBrainWaves(self.after)
        #TODO: break printing out into seperate function; make pretty
        for data in beforeDataAveraged, afterDataAveraged:
            for key, value in data.items():
                compareData[key].append(value)
        for key, values in compareData.items():
            difference = values[0] - values[1]
            compareData[key].append(difference)
        print("Data in the form: {'band': [before, after, difference]}")
        pp.pprint(compareData)


mindfulnessData = BasicBrainData(beforePracticeRawData, afterPracticeRawData)
mindfulnessData.compareBeforeAfter()
